# JDA Specification v1.0
## JSON Digital Assets for SDF Raymarching

JDA (JSON Digital Assets) is a language-agnostic format for defining SDF (Signed Distance Field) primitives and scenes.

## Asset Format

### Primitive Asset Structure

```json
{
  "type": "sphere|box|torus|capsule|cylinder|cone|plane",
  "name": "Human-readable name",
  "position": [x, y, z],
  "params": {
    // Type-specific parameters
  },
  "material": {
    "color": [r, g, b],       // 0.0 - 1.0
    "roughness": 0.5,         // 0.0 (mirror) - 1.0 (diffuse)
    "metallic": 0.0           // 0.0 (dielectric) - 1.0 (metal)
  },
  "metadata": {
    "author": "Creator name",
    "version": "1.0",
    "tags": ["tag1", "tag2"]
  }
}
```

### Primitive Types and Parameters

#### Sphere
```json
{
  "type": "sphere",
  "params": {
    "radius": 0.5
  }
}
```

#### Box
```json
{
  "type": "box",
  "params": {
    "size": [width, height, depth]
  }
}
```

#### Torus
```json
{
  "type": "torus",
  "params": {
    "majorRadius": 0.4,
    "minorRadius": 0.15
  }
}
```

#### Capsule
```json
{
  "type": "capsule",
  "params": {
    "pointA": [x, y, z],
    "pointB": [x, y, z],
    "radius": 0.2
  }
}
```

#### Cylinder
```json
{
  "type": "cylinder",
  "params": {
    "height": 0.5,
    "radius": 0.3
  }
}
```

#### Cone
```json
{
  "type": "cone",
  "params": {
    "angle": {
      "sin": 0.8,
      "cos": 0.6
    },
    "height": 0.8
  }
}
```

#### Plane (Infinite)
```json
{
  "type": "plane",
  "params": {},
  "position": [0.0, -0.5, 0.0]  // Y position is plane height
}
```

## Scene Format

```json
{
  "name": "Scene Name",
  "version": "1.0",
  "assets": [
    "path/to/asset1.json",
    "path/to/asset2.json"
  ],
  "camera": {
    "speed": 0.2,
    "radius": 2.0,
    "height": 1.5,
    "target": [x, y, z]
  },
  "lighting": {
    "position": [x, y, z],
    "color": [r, g, b],
    "intensity": 1.5,
    "ambient": 0.3
  },
  "rendering": {
    "maxSteps": 96,
    "maxDistance": 40.0,
    "surfaceDistance": 0.001
  }
}
```

## File Size

Typical JDA asset: **~200-400 bytes**

Example breakdown:
- Sphere primitive: ~250 bytes
- Box primitive: ~280 bytes
- Torus primitive: ~300 bytes
- Scene file: ~500 bytes

## Compatibility

JDA files can be loaded by:
- ✅ LÖVR (Lua)
- ✅ Unity (C#)
- ✅ Godot (GDScript)
- ✅ Web (JavaScript/TypeScript)
- ✅ Blender (Python export)
- ✅ Any language with JSON support

## Usage in LÖVR

```lua
local json = lovr.data.decode('json', lovr.filesystem.read('asset.json'))
print(json.name)  -- "Red Sphere"
print(json.type)  -- "sphere"
```

## Future Extensions

- Animation keyframes
- Compound objects (multiple primitives)
- SDF operations (union, subtraction, intersection)
- Texture references
- Physics properties
- Collision data

---

**Version:** 1.0
**Status:** Production Ready
**License:** Open Format
