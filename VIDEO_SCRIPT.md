# Showcase Video Script

Video guide til Blender JDA Exporter demonstration.

## Video 1: Quick Start (2-3 minutter)

### Scene 1: Introduction (15 sek)
**Visuals**: Logo/title card
**Script**:
> "Tired of massive file sizes? Meet JDA - JSON Digital Assets. Export Blender scenes as ultra-lightweight JSON files, 250 times smaller than FBX."

**Text overlay**:
- FBX: 50 KB → JDA: 200 bytes ⚡

### Scene 2: Installation (20 sek)
**Visuals**: Screen recording af Blender preferences
**Script**:
> "Installation takes seconds. Edit → Preferences → Add-ons → Install. Select the JDA exporter, enable it, and you're done."

**Steps shown**:
1. Edit → Preferences
2. Add-ons → Install
3. Select `jda_exporter.py`
4. Enable checkbox

### Scene 3: Basic Usage (45 sek)
**Visuals**: Creating objects in Blender
**Script**:
> "Name your objects with SDF type prefixes. Sphere underscore Red becomes a sphere primitive. Box underscore Wall becomes a box. The exporter auto-detects the type."

**Steps shown**:
1. Create UV Sphere → rename "Sphere_Red"
2. Create Cube → rename "Box_Wall"
3. Assign Principled BSDF materials
4. Set Base Color, Roughness, Metallic

### Scene 4: Export (30 sek)
**Visuals**: Export process
**Script**:
> "Export is instant. File → Export → JDA. Choose your directory and click Export JDA. Done. Look at those file sizes - just 200 bytes per object!"

**Steps shown**:
1. File → Export → JDA (.json)
2. Select directory
3. Export JDA
4. Show file browser with sizes

### Scene 5: Results (30 sek)
**Visuals**: JSON file + rendered result in LÖVR/Unity
**Script**:
> "The exported JSON contains everything - position, size, materials. Load it in any engine: LÖVR, Unity, Godot, or the Web. GPU-native rendering with infinite detail."

**Show**:
1. Open JSON in text editor (formatted, readable)
2. Same scene running in LÖVR (real-time)
3. Performance stats: 60 FPS, 2 KB scene

### Scene 6: Closing (10 sek)
**Visuals**: GitHub link + logo
**Script**:
> "Get started today. Link in description. MIT license, free forever."

**Text overlay**:
- github.com/lpmwfx/blender-jda-exporter
- ⭐ Star if you find it useful!

---

## Video 2: Advanced - Procedural Generation (3-4 minutter)

### Scene 1: Introduction (15 sek)
**Script**:
> "Let's take it further. Generate entire scenes programmatically with Blender's Python API."

### Scene 2: BPY Script Basics (1 min)
**Visuals**: Code editor + Blender side-by-side
**Script**:
> "Here's a simple script. Import BPY, create a sphere, set its name, assign a material. Run it in Blender's scripting workspace."

**Code shown**:
```python
import bpy

# Create sphere
bpy.ops.mesh.primitive_uv_sphere_add(location=(0, 1, 0))
sphere = bpy.context.active_object
sphere.name = "Sphere_Red"

# Assign material
mat = bpy.data.materials.new("Red")
mat.use_nodes = True
bsdf = mat.node_tree.nodes["Principled BSDF"]
bsdf.inputs['Base Color'].default_value = (0.9, 0.2, 0.2, 1.0)
sphere.data.materials.append(mat)
```

### Scene 3: Bubble Tree Demo (1.5 min)
**Visuals**: Running bubble_tree.py
**Script**:
> "The bubble tree example generates a procedural tree. One cylinder trunk, six colorful sphere bubbles, materials, everything. Run the script, instant scene creation."

**Show**:
1. Open bubble_tree.py in Blender
2. Run script (Alt+P)
3. Watch objects appear
4. Export to JDA
5. Show output: 8 files, 2.5 KB total

### Scene 4: Batch Processing (45 sek)
**Visuals**: For loop creating 25 objects
**Script**:
> "Scale it up. Create a grid of spheres with a for loop. Twenty-five objects in milliseconds. Each with unique colors based on position. Export all at once."

**Code shown**:
```python
for x in range(5):
    for z in range(5):
        create_sphere(f"Sphere_{x}_{z}", (x*2, 1, z*2), (x/4, 0.5, z/4))
```

### Scene 5: Real-world Use Case (30 sek)
**Visuals**: Complete game scene
**Script**:
> "Imagine a game level. Hundreds of props. Generate them procedurally, export to JDA, load in your engine. Tiny file sizes, instant loading, infinite detail."

### Scene 6: Closing (20 sek)
**Script**:
> "Check out the examples folder for more scripts. Contribute your own. Let's build the future of lightweight game assets together."

---

## Video 3: Cross-Platform Demo (2-3 minutter)

### Scene 1: One Source, Multiple Targets (30 sek)
**Visuals**: Blender → 4 engines split screen
**Script**:
> "Export once, use everywhere. The same JDA file works in LÖVR, Unity, Godot, and Web. True cross-platform assets."

### Scene 2: LÖVR Demo (45 sek)
**Visuals**: Code + running scene
**Script**:
> "In LÖVR, load the JSON, generate shader code, instant GPU rendering. Here's the bubble tree running at 60 FPS on integrated graphics."

### Scene 3: Unity Demo (45 sek)
**Visuals**: Unity editor + C# code
**Script**:
> "Unity? Parse the JSON, instantiate primitives, apply materials. Same scene, same data, different engine."

### Scene 4: Web Demo (45 sek)
**Visuals**: Browser + Three.js code
**Script**:
> "Even the web. Fetch the JSON, render with WebGL. Two kilobytes downloaded, entire scene loaded."

### Scene 5: Closing (15 sek)
**Script**:
> "One format, infinite possibilities. Start building today."

---

## YouTube Description Template

```markdown
# Blender JDA Exporter - Ultra-Lightweight Game Assets

Export Blender scenes as JSON Digital Assets (JDA) - 250x smaller than traditional formats!

## 🚀 Features
✅ 200-400 bytes per asset (vs 50 KB for FBX)
✅ Auto-detect SDF types from object names
✅ Extract PBR materials from Principled BSDF
✅ Cross-platform: LÖVR, Unity, Godot, Web
✅ GPU-native rendering with infinite detail
✅ Procedural generation with Python

## 📥 Download
GitHub: https://github.com/lpmwfx/blender-jda-exporter
Documentation: https://github.com/lpmwfx/blender-jda-exporter#readme

## ⏱️ Timestamps
0:00 Introduction
0:15 Installation
0:35 Basic Usage
1:20 Export Process
1:50 Cross-Platform Results
2:20 Procedural Generation (Advanced)

## 📚 Resources
- Installation Guide: https://github.com/lpmwfx/blender-jda-exporter/blob/main/INSTALLATION.md
- JDA Specification: https://github.com/lpmwfx/blender-jda-exporter/blob/main/JDA_SPEC.md
- Example Scripts: https://github.com/lpmwfx/blender-jda-exporter/tree/main/examples
- LÖVR Integration: https://github.com/lpmwfx/SDF_LUA

## 💡 Use Cases
- Indie game development
- Procedural content generation
- Lightweight web games
- VR/AR applications
- Rapid prototyping

## 🎮 Supported Engines
- LÖVR (Lua)
- Unity (C#)
- Godot (GDScript)
- Web (JavaScript/Three.js)
- Any JSON-capable engine!

## 📄 License
MIT License - Free forever!

## ⭐ Support
Star the repo if you find it useful!
Report issues: https://github.com/lpmwfx/blender-jda-exporter/issues

#blender #gamedev #indiedev #3d #json #sdf #raymarching #procedural
```

---

## Social Media Posts

### Twitter/X
```
🎨 Blender JDA Exporter - Export 3D assets as JSON

📦 250x smaller than FBX
⚡ 200 bytes per object
🌍 Cross-platform (Unity, Godot, Web)
♾️ Infinite detail with SDF raymarching

Free & open source!
github.com/lpmwfx/blender-jda-exporter

#gamedev #blender3d #indiedev
```

### Reddit (r/blender, r/gamedev)
```markdown
# I made a Blender addon that exports scenes as ultra-lightweight JSON files

Traditional formats like FBX are huge (50+ KB for a simple sphere). I built JDA (JSON Digital Assets) - same scene, 200 bytes.

**Features:**
- Auto-detects SDF primitives from object names
- Extracts PBR materials from Principled BSDF
- Works with Unity, Godot, LÖVR, Web
- GPU-native rendering with mathematical surfaces
- Procedural generation support

**Example:** Bubble tree scene (8 objects) = 2.5 KB total

**Free & MIT licensed:** github.com/lpmwfx/blender-jda-exporter

Would love feedback! What use cases would you want?
```

### LinkedIn
```
Excited to share my latest open-source project: Blender JDA Exporter!

Traditional 3D asset formats are bloated. A simple sphere in FBX? 50 KB. With JDA (JSON Digital Assets)? 200 bytes.

This Blender addon enables:
✅ Ultra-lightweight game assets
✅ Cross-platform compatibility (Unity, Godot, Web)
✅ GPU-native rendering with SDF raymarching
✅ Procedural content generation workflows

Perfect for indie devs, web games, and rapid prototyping.

Built with Python, fully open source (MIT).

Check it out: github.com/lpmwfx/blender-jda-exporter

#GameDevelopment #Blender #OpenSource #3DAssets
```

---

## Demo Scene Ideas for Video

### Scene 1: Size Comparison
Split screen:
- Left: Traditional export (FBX/OBJ) with file size
- Right: JDA export with file size
- Giant vs tiny visual representation

### Scene 2: Performance Test
- Load 100 objects from FBX: X seconds, Y MB
- Load 100 objects from JDA: 0.1 seconds, 20 KB
- Side-by-side loading bars

### Scene 3: Cross-Platform Matrix
Grid showing same assets in:
```
         LÖVR    Unity   Godot    Web
Sphere   ✓        ✓       ✓       ✓
Box      ✓        ✓       ✓       ✓
Scene    ✓        ✓       ✓       ✓
```

### Scene 4: Procedural Magic
Timelapse:
1. Empty Blender scene
2. Run script
3. Hundreds of objects appear
4. Export
5. Running in game engine

All in 10 seconds!
