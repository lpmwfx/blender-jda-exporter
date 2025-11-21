# Examples

Example Blender Python (BPY) scripts for procedural JDA generation.

## bubble_tree.py

Procedural bubble tree generator.

**Creates:**
- 1 cylinder trunk
- 6 colorful sphere bubbles
- 1 ground plane
- Materials with PBR properties

**Usage:**
```bash
# In Blender Scripting workspace:
# 1. Open bubble_tree.py
# 2. Run Script (Alt+P or ▶ button)

# Or from command line:
blender --background --python bubble_tree.py
```

**Output:**
```
jda-assets/
├── cylinder_trunk.json    (280 bytes)
├── sphere_bubble1.json    (250 bytes)
├── sphere_bubble2.json    (250 bytes)
├── sphere_bubble3.json    (250 bytes)
├── sphere_bubble4.json    (250 bytes)
├── sphere_bubble5.json    (250 bytes)
├── sphere_bubble6.json    (250 bytes)
└── floor.json             (230 bytes)
```

Total: ~2.5 KB for entire scene!

## Creating Your Own

### Basic Template

```python
import bpy
import json
from datetime import datetime

# Clear scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Create sphere
bpy.ops.mesh.primitive_uv_sphere_add(
    location=(0, 1, 0),
    radius=0.5
)
sphere = bpy.context.active_object
sphere.name = "Sphere_Red"

# Create material
mat = bpy.data.materials.new(name="Red")
mat.use_nodes = True
bsdf = mat.node_tree.nodes["Principled BSDF"]
bsdf.inputs['Base Color'].default_value = (0.9, 0.2, 0.2, 1.0)
bsdf.inputs['Roughness'].default_value = 0.3
bsdf.inputs['Metallic'].default_value = 0.1

sphere.data.materials.append(mat)

# Export to JDA
jda = {
    "type": "sphere",
    "name": sphere.name,
    "position": list(sphere.location),
    "params": {
        "radius": sphere.scale[0]  # Assuming uniform scale
    },
    "material": {
        "color": list(bsdf.inputs['Base Color'].default_value[:3]),
        "roughness": bsdf.inputs['Roughness'].default_value,
        "metallic": bsdf.inputs['Metallic'].default_value
    },
    "metadata": {
        "created": datetime.now().isoformat(),
        "author": "BPY Script",
        "version": "1.0"
    }
}

# Save
with open("/tmp/sphere_red.json", "w") as f:
    json.dump(jda, indent=2, fp=f)

print("✓ Exported: /tmp/sphere_red.json")
```

### Multiple Objects

```python
import bpy
import json

def create_sphere(name, location, color, radius=0.5):
    bpy.ops.mesh.primitive_uv_sphere_add(
        location=location,
        radius=radius
    )
    obj = bpy.context.active_object
    obj.name = name

    mat = bpy.data.materials.new(name=f"Mat_{name}")
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    bsdf.inputs['Base Color'].default_value = (*color, 1.0)

    obj.data.materials.append(mat)
    return obj

# Create multiple spheres
create_sphere("Sphere_Red", (0, 1, 0), (0.9, 0.2, 0.2))
create_sphere("Sphere_Green", (2, 1, 0), (0.2, 0.9, 0.2))
create_sphere("Sphere_Blue", (4, 1, 0), (0.2, 0.2, 0.9))

# Export all using the JDA exporter addon
bpy.ops.export_scene.jda(filepath="/tmp/scene/")
```

### Procedural Grid

```python
import bpy

# Clear scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Create 5x5 grid of spheres
for x in range(5):
    for z in range(5):
        bpy.ops.mesh.primitive_uv_sphere_add(
            location=(x * 2, 1, z * 2),
            radius=0.4
        )
        sphere = bpy.context.active_object
        sphere.name = f"Sphere_Grid_{x}_{z}"

        # Gradient color based on position
        r = x / 4
        b = z / 4
        g = 1.0 - (r + b) / 2

        mat = bpy.data.materials.new(name=f"Mat_{x}_{z}")
        mat.use_nodes = True
        bsdf = mat.node_tree.nodes["Principled BSDF"]
        bsdf.inputs['Base Color'].default_value = (r, g, b, 1.0)

        sphere.data.materials.append(mat)
```

## Tips

### Object Naming
Always prefix with SDF type:
```python
sphere.name = "Sphere_MyObject"  # ✓ Good
sphere.name = "MyObject"         # ✗ Bad - won't detect type
```

### Scale vs Parameters
```python
# For spheres, use scale
sphere.scale = (0.5, 0.5, 0.5)  # radius = 0.5

# For boxes, scale determines size
box.scale = (1.0, 2.0, 0.5)  # width=1, height=2, depth=0.5
```

### Materials
Always use Principled BSDF:
```python
bsdf = mat.node_tree.nodes["Principled BSDF"]
bsdf.inputs['Base Color'].default_value = (r, g, b, 1.0)
bsdf.inputs['Roughness'].default_value = 0.5
bsdf.inputs['Metallic'].default_value = 0.0
```

### Batch Export
```python
import os

output_dir = "/tmp/jda-assets"
os.makedirs(output_dir, exist_ok=True)

# Export will create individual JSON files
bpy.ops.export_scene.jda(filepath=output_dir + "/scene.json")
```

## More Examples

See the [SDF_LUA examples](https://github.com/lpmwfx/SDF_LUA/tree/main/examples/bubble_tree) for complete working demos.
