# Blender JDA Exporter

Blender addon to export scenes to **JDA (JSON Digital Assets)** format for use with SDF (Signed Distance Field) raymarching engines.

## What is JDA?

JDA is a lightweight, language-agnostic asset format for SDF primitives:
- **~200-400 bytes** per asset (vs 40+ KB for polygon meshes)
- **Cross-platform**: LÖVR, Unity, Godot, Web, any JSON-capable engine
- **Material support**: PBR properties (color, roughness, metallic)
- **SDF primitives**: Sphere, Box, Cylinder, Torus, Capsule, Cone

## Features

✅ **Auto-detection** of SDF types from object names
✅ **Material extraction** from Principled BSDF nodes
✅ **Batch export** entire scenes
✅ **Tiny file sizes** (~200-400 bytes per object)
✅ **Scene metadata** with camera and lighting settings

## Installation

### Method 1: Quick Install

1. Download `jda_exporter.py`
2. Open Blender → Edit → Preferences → Add-ons
3. Click "Install..." → Select `jda_exporter.py`
4. Enable "Import-Export: JDA Exporter"

### Method 2: Manual Install

```bash
# Find your Blender addons directory:
# - macOS: ~/Library/Application Support/Blender/{version}/scripts/addons/
# - Linux: ~/.config/blender/{version}/scripts/addons/
# - Windows: %APPDATA%/Blender Foundation/Blender/{version}/scripts/addons/

# Copy the addon
cp jda_exporter.py /path/to/blender/addons/

# Restart Blender and enable in Preferences
```

## Usage

### Quick Start

1. **Name your objects** using SDF type prefixes:
   - `Sphere_Red` → Sphere primitive
   - `Box_Wall` → Box primitive
   - `Cylinder_Trunk` → Cylinder primitive
   - `Torus_Ring` → Torus primitive

2. **Assign materials** (Principled BSDF):
   - Base Color → JDA color
   - Roughness → JDA roughness
   - Metallic → JDA metallic

3. **Export**:
   - File → Export → JDA (.json)
   - Choose export location
   - Click "Export JDA"

### Object Naming Conventions

The exporter detects SDF type from object name:

| Blender Object Name | Detected Type | Parameters |
|---------------------|---------------|------------|
| `Sphere_*` | sphere | radius (avg scale) |
| `Box_*` | box | size (scale) |
| `Cylinder_*` | cylinder | height, radius |
| `Torus_*` | torus | major/minor radius |
| `Capsule_*` | capsule | height, radius |
| `Cone_*` | cone | height, angle |

**Examples:**
```
Sphere_Player      → sphere
Box_Wall_Large     → box
Cylinder_Column_01 → cylinder
Torus_Ring_Gold    → torus
```

### Example Output

```json
{
  "type": "sphere",
  "name": "Sphere_Player",
  "position": [0.0, 1.0, 0.0],
  "params": {
    "radius": 0.5
  },
  "material": {
    "color": [0.9, 0.2, 0.2],
    "roughness": 0.3,
    "metallic": 0.1
  },
  "metadata": {
    "created": "2025-11-21T23:00:00",
    "author": "Blender JDA Exporter",
    "version": "1.0"
  }
}
```

## Procedural Generation with BPY

You can also generate scenes programmatically:

```python
import bpy
import math

# Clear scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Create sphere
bpy.ops.mesh.primitive_uv_sphere_add(location=(0, 1, 0), radius=0.5)
sphere = bpy.context.active_object
sphere.name = "Sphere_Red"

# Assign material
mat = bpy.data.materials.new(name="Red")
mat.use_nodes = True
bsdf = mat.node_tree.nodes["Principled BSDF"]
bsdf.inputs['Base Color'].default_value = (0.9, 0.2, 0.2, 1.0)
bsdf.inputs['Roughness'].default_value = 0.3
sphere.data.materials.append(mat)

# Export
bpy.ops.export_scene.jda(filepath="/tmp/scene.json")
```

See [examples/](examples/) for complete BPY scripts.

## Use Cases

### Game Engines

**LÖVR** (Lua):
```lua
local json = require('json')
local asset = json.decode(lovr.filesystem.read('sphere_red.json'))
-- Use asset.position, asset.params.radius, asset.material
```

**Unity** (C#):
```csharp
string json = File.ReadAllText("sphere_red.json");
JDAAsset asset = JsonUtility.FromJson<JDAAsset>(json);
// Use asset.position, asset.params.radius, asset.material
```

**Godot** (GDScript):
```gdscript
var file = FileAccess.open("sphere_red.json", FileAccess.READ)
var asset = JSON.parse_string(file.get_as_text())
# Use asset.position, asset.params.radius, asset.material
```

**Web** (JavaScript):
```javascript
fetch('sphere_red.json')
  .then(r => r.json())
  .then(asset => {
    // Use asset.position, asset.params.radius, asset.material
  });
```

## JDA Specification

Full specification: [JDA_SPEC.md](JDA_SPEC.md)

**Core fields:**
- `type`: SDF primitive type (sphere, box, etc.)
- `position`: [x, y, z] in world space
- `params`: Type-specific parameters (radius, size, etc.)
- `material`: PBR material properties
- `metadata`: Creation info, version, tags

## Examples

See [examples/](examples/) directory for:
- `bubble_tree.py` - Procedural tree with colorful bubbles
- `simple_scene.blend` - Basic Blender scene to export
- Output JDA files

## Performance

**File Size Comparison:**

| Format | Size | Ratio |
|--------|------|-------|
| FBX Sphere | ~50 KB | 250x |
| OBJ Sphere | ~30 KB | 150x |
| GLTF Sphere | ~5 KB | 25x |
| **JDA Sphere** | **~200 bytes** | **1x** ✅ |

**Benefits:**
- ⚡ Ultra-fast loading
- 💾 Minimal storage/bandwidth
- 🎮 GPU-native rendering (no vertex buffers)
- ♾️ Infinite detail (mathematical surfaces)

## Roadmap

- [ ] Scene composition (parent/child hierarchies)
- [ ] Animation keyframes export
- [ ] Custom SDF operations (union, subtract, etc.)
- [ ] Blender → JDA live link
- [ ] Material node graph analysis
- [ ] Auto-generate scene.json with lighting/camera

## Contributing

Contributions welcome! Please:
1. Fork the repo
2. Create feature branch
3. Submit PR with description

## License

MIT License - see [LICENSE](LICENSE)

## Links

- **JDA Specification**: [JDA_SPEC.md](JDA_SPEC.md)
- **LÖVR Example Usage**: [SDF_LUA](https://github.com/lpmwfx/SDF_LUA)
- **Blender Python API**: [docs.blender.org](https://docs.blender.org/api/current/)

## Credits

Created for the [SDF_LUA](https://github.com/lpmwfx/SDF_LUA) project.

Inspired by:
- Inigo Quilez's SDF work
- Dreams (Media Molecule)
- Claybooks (Second Order)
