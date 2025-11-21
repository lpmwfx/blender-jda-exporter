"""
Blender BPY Script: Create Bubble Tree
Lav et træ med cylinder stamme og sphere "blade" (bubbles)
Eksporterer automatisk til JDA format

Sådan bruges:
1. Åbn Blender
2. Scripting workspace
3. Paste denne kode i Text Editor
4. Tryk "Run Script" (Alt+P)
5. File → Export → JDA (.json)
"""

import bpy
import math
import random

# Clean scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Tree parameters
trunk_height = 3.0
trunk_radius = 0.3
bubble_count = 12
bubble_radius_min = 0.3
bubble_radius_max = 0.6

print("🌳 Creating Bubble Tree...")

# Create trunk (cylinder)
bpy.ops.mesh.primitive_cylinder_add(
    radius=trunk_radius,
    depth=trunk_height,
    location=(0, 0, trunk_height/2)
)
trunk = bpy.context.active_object
trunk.name = "Cylinder_Trunk"

# Trunk material - brown
trunk_mat = bpy.data.materials.new(name="TrunkMaterial")
trunk_mat.use_nodes = True
bsdf = trunk_mat.node_tree.nodes["Principled BSDF"]
bsdf.inputs['Base Color'].default_value = (0.4, 0.25, 0.1, 1.0)  # Brown
bsdf.inputs['Roughness'].default_value = 0.8
trunk.data.materials.append(trunk_mat)

print(f"  ✓ Trunk created")

# Create bubbles (spheres) around top of tree
bubbles = []
colors = [
    (0.9, 0.2, 0.2, 1.0),  # Red
    (0.2, 0.9, 0.2, 1.0),  # Green
    (0.2, 0.4, 0.9, 1.0),  # Blue
    (0.9, 0.9, 0.2, 1.0),  # Yellow
    (0.9, 0.2, 0.9, 1.0),  # Magenta
    (0.2, 0.9, 0.9, 1.0),  # Cyan
]

for i in range(bubble_count):
    # Position bubbles in a sphere around tree top
    angle = (i / bubble_count) * 2 * math.pi
    height_offset = random.uniform(-0.5, 1.5)
    radius_offset = random.uniform(0.8, 1.5)

    x = math.cos(angle) * radius_offset
    y = math.sin(angle) * radius_offset
    z = trunk_height + height_offset

    # Random bubble size
    bubble_radius = random.uniform(bubble_radius_min, bubble_radius_max)

    # Create sphere
    bpy.ops.mesh.primitive_uv_sphere_add(
        radius=bubble_radius,
        location=(x, y, z)
    )
    bubble = bpy.context.active_object
    bubble.name = f"Sphere_Bubble{i+1}"

    # Colorful material
    color = colors[i % len(colors)]
    bubble_mat = bpy.data.materials.new(name=f"BubbleMat{i+1}")
    bubble_mat.use_nodes = True
    bsdf = bubble_mat.node_tree.nodes["Principled BSDF"]
    bsdf.inputs['Base Color'].default_value = color
    bsdf.inputs['Roughness'].default_value = 0.2  # Shiny bubbles
    bsdf.inputs['Metallic'].default_value = 0.3
    bubble.data.materials.append(bubble_mat)

    bubbles.append(bubble)

print(f"  ✓ Created {bubble_count} bubbles")

# Add ground plane (Empty)
bpy.ops.object.empty_add(location=(0, 0, -0.5))
ground = bpy.context.active_object
ground.name = "Floor"

print(f"  ✓ Added floor")

# Select all for export
bpy.ops.object.select_all(action='SELECT')

print("\n✅ Bubble Tree complete!")
print(f"   - 1 trunk (cylinder)")
print(f"   - {bubble_count} colorful bubbles (spheres)")
print(f"   - 1 floor plane")
print("\n📤 Now export: File → Export → JDA (.json)")
print("   Save as: bubble_tree_scene.json")
