"""
Blender JDA Exporter v1.0
Export Blender objects to JDA (JSON Digital Assets) format for SDF raymarching

Installation:
1. Open Blender
2. Edit → Preferences → Add-ons → Install
3. Select this file
4. Enable "Import-Export: JDA Exporter"

Usage:
1. Select object(s) in Blender
2. File → Export → JDA (.json)
3. Use in LÖVR/Unity/Godot/Web
"""

bl_info = {
    "name": "JDA Exporter",
    "author": "SDF_LUA",
    "version": (1, 0, 0),
    "blender": (3, 0, 0),
    "location": "File > Export > JDA (.json)",
    "description": "Export to JDA (JSON Digital Assets) for SDF raymarching",
    "category": "Import-Export",
}

import bpy
import json
import math
from bpy.props import StringProperty, BoolProperty
from bpy_extras.io_utils import ExportHelper


def object_to_jda(obj):
    """Convert Blender object to JDA format"""

    # Get object type and approximate as SDF primitive
    obj_type = obj.type

    jda = {
        "name": obj.name,
        "position": list(obj.location),
        "metadata": {
            "author": "Blender",
            "version": "1.0",
            "blender_type": obj_type,
            "tags": []
        }
    }

    # Determine SDF primitive type based on object
    if obj_type == 'MESH':
        mesh = obj.data

        # Check mesh type by name or vertex count
        if 'sphere' in obj.name.lower() or 'ball' in obj.name.lower():
            # Sphere - use average scale as radius
            avg_scale = (obj.scale.x + obj.scale.y + obj.scale.z) / 3.0
            jda["type"] = "sphere"
            jda["params"] = {
                "radius": avg_scale
            }

        elif 'torus' in obj.name.lower():
            jda["type"] = "torus"
            # Approximate from mesh dimensions
            jda["params"] = {
                "majorRadius": obj.dimensions.x / 2.0,
                "minorRadius": obj.dimensions.z / 4.0
            }

        elif 'cylinder' in obj.name.lower() or 'cyl' in obj.name.lower():
            jda["type"] = "cylinder"
            jda["params"] = {
                "height": obj.dimensions.z / 2.0,
                "radius": (obj.dimensions.x + obj.dimensions.y) / 4.0
            }

        elif 'cone' in obj.name.lower():
            jda["type"] = "cone"
            # Cone angle approximation
            angle_rad = math.atan2(obj.dimensions.x, obj.dimensions.z)
            jda["params"] = {
                "angle": {
                    "sin": math.sin(angle_rad),
                    "cos": math.cos(angle_rad)
                },
                "height": obj.dimensions.z
            }

        else:
            # Default to box
            jda["type"] = "box"
            jda["params"] = {
                "size": [
                    obj.dimensions.x / 2.0,
                    obj.dimensions.y / 2.0,
                    obj.dimensions.z / 2.0
                ]
            }

    elif obj_type == 'EMPTY':
        # Empty as plane/marker
        jda["type"] = "plane"
        jda["params"] = {}

    else:
        # Unknown type, default to sphere
        jda["type"] = "sphere"
        jda["params"] = {"radius": 0.5}

    # Material properties
    material = {
        "color": [0.7, 0.7, 0.7],
        "roughness": 0.5,
        "metallic": 0.0
    }

    # Extract material if exists
    if obj.active_material:
        mat = obj.active_material

        # Get base color (Principled BSDF)
        if mat.use_nodes:
            for node in mat.node_tree.nodes:
                if node.type == 'BSDF_PRINCIPLED':
                    # Base Color
                    base_color = node.inputs['Base Color'].default_value
                    material["color"] = [base_color[0], base_color[1], base_color[2]]

                    # Roughness
                    material["roughness"] = node.inputs['Roughness'].default_value

                    # Metallic
                    material["metallic"] = node.inputs['Metallic'].default_value
                    break
        else:
            # Legacy material
            material["color"] = list(mat.diffuse_color[:3])

    jda["material"] = material

    return jda


def export_scene_jda(context, filepath, selected_only=True):
    """Export scene or selection to JDA scene file"""

    objects = context.selected_objects if selected_only else context.scene.objects

    if not objects:
        return {'CANCELLED'}, "No objects to export"

    # Export individual assets
    asset_files = []

    for obj in objects:
        if obj.type not in ['MESH', 'EMPTY']:
            continue

        jda_data = object_to_jda(obj)

        # Generate filename
        asset_filename = f"{obj.name.lower().replace(' ', '_')}.json"
        asset_path = filepath.replace('.json', f'_assets/{asset_filename}')

        # Save asset
        import os
        os.makedirs(os.path.dirname(asset_path), exist_ok=True)

        with open(asset_path, 'w') as f:
            json.dump(jda_data, f, indent=2)

        asset_files.append(f"jda-assets/{asset_filename}")
        print(f"Exported: {asset_filename}")

    # Create scene file
    scene_data = {
        "name": context.scene.name,
        "version": "1.0",
        "assets": asset_files,
        "camera": {
            "speed": 0.2,
            "radius": 2.0,
            "height": 1.5,
            "target": [0.0, 0.0, 0.0]
        },
        "lighting": {
            "position": [5.0, 5.0, 5.0],
            "color": [1.0, 1.0, 1.0],
            "intensity": 1.5,
            "ambient": 0.3
        },
        "rendering": {
            "maxSteps": 96,
            "maxDistance": 40.0,
            "surfaceDistance": 0.001
        }
    }

    with open(filepath, 'w') as f:
        json.dump(scene_data, f, indent=2)

    return {'FINISHED'}, f"Exported {len(asset_files)} objects to JDA"


class ExportJDA(bpy.types.Operator, ExportHelper):
    """Export to JDA (JSON Digital Assets)"""
    bl_idname = "export_scene.jda"
    bl_label = "Export JDA"

    filename_ext = ".json"

    filter_glob: StringProperty(
        default="*.json",
        options={'HIDDEN'},
    )

    selected_only: BoolProperty(
        name="Selected Only",
        description="Export only selected objects",
        default=True,
    )

    def execute(self, context):
        result, message = export_scene_jda(context, self.filepath, self.selected_only)

        if result == {'FINISHED'}:
            self.report({'INFO'}, message)
        else:
            self.report({'ERROR'}, message)

        return result


def menu_func_export(self, context):
    self.layout.operator(ExportJDA.bl_idname, text="JDA (.json)")


def register():
    bpy.utils.register_class(ExportJDA)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)


def unregister():
    bpy.utils.unregister_class(ExportJDA)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)


if __name__ == "__main__":
    register()
