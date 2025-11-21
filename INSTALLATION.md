# Installation Guide

Complete guide til at installere Blender JDA Exporter.

## Prerequisites

- Blender 3.0+ (tested on 3.6, 4.0+)
- Python 3.10+ (comes with Blender)

## Quick Install (Recommended)

### Step 1: Download Addon

Download `jda_exporter.py` from:
- GitHub releases: https://github.com/lpmwfx/blender-jda-exporter/releases
- Or clone: `git clone https://github.com/lpmwfx/blender-jda-exporter.git`

### Step 2: Install in Blender

1. Open Blender
2. **Edit** → **Preferences** (or **Blender** → **Settings** on macOS)
3. Go to **Add-ons** tab
4. Click **Install...** button (top right)
5. Navigate to `jda_exporter.py` and select it
6. Click **Install Add-on**

### Step 3: Enable Addon

1. Search for "JDA" in the addons search box
2. Check the box next to **Import-Export: JDA Exporter**
3. Close Preferences

### Step 4: Verify Installation

1. Go to **File** → **Export**
2. You should see **JDA (.json)** in the export menu

✅ Installation complete!

---

## Manual Install (Advanced)

### Find Blender Addons Directory

**macOS:**
```bash
~/Library/Application Support/Blender/{version}/scripts/addons/
# Example: ~/Library/Application Support/Blender/4.0/scripts/addons/
```

**Linux:**
```bash
~/.config/blender/{version}/scripts/addons/
# Example: ~/.config/blender/4.0/scripts/addons/
```

**Windows:**
```
%APPDATA%\Blender Foundation\Blender\{version}\scripts\addons\
# Example: C:\Users\YourName\AppData\Roaming\Blender Foundation\Blender\4.0\scripts\addons\
```

### Copy Addon

```bash
# Navigate to the directory
cd ~/Library/Application\ Support/Blender/4.0/scripts/addons/

# Copy the addon
cp /path/to/jda_exporter.py .
```

### Restart Blender

1. Quit Blender completely
2. Relaunch Blender
3. Enable addon in Preferences (see Step 3 above)

---

## Troubleshooting

### "No module named 'jda_exporter'"

**Solution:** Make sure you installed from the `.py` file, not a `.zip` or directory.

### Addon doesn't appear in preferences

**Solution:**
1. Check Blender version is 3.0+
2. Verify the file is in the correct addons directory
3. Check the addon file has no syntax errors:
   ```bash
   python3 jda_exporter.py
   ```
4. Restart Blender

### Export menu doesn't show JDA option

**Solution:**
1. Make sure addon is **enabled** (checkbox checked)
2. Look for **File → Export → JDA (.json)**
3. Try restarting Blender

### Exported JSON is empty or invalid

**Solution:**
1. Check object names contain valid SDF type prefix (Sphere_, Box_, etc.)
2. Verify objects have materials assigned
3. Check Blender console for error messages: **Window → Toggle System Console**

### Permission errors on macOS

**Solution:**
```bash
# Give read/write permissions
chmod +x jda_exporter.py
```

---

## Updating

### Update via Preferences

1. Download new version of `jda_exporter.py`
2. **Edit → Preferences → Add-ons**
3. Find **JDA Exporter** and click **Remove**
4. Click **Install...** and select new version
5. Enable the addon

### Update Manually

```bash
# Replace the file in addons directory
cp /path/to/new/jda_exporter.py ~/Library/Application\ Support/Blender/4.0/scripts/addons/
```

Restart Blender.

---

## Uninstall

### Via Preferences

1. **Edit → Preferences → Add-ons**
2. Search for "JDA"
3. Click **Remove** next to **JDA Exporter**

### Manual Uninstall

```bash
# Delete the file
rm ~/Library/Application\ Support/Blender/4.0/scripts/addons/jda_exporter.py
```

---

## Developer Install (For Contributing)

### Setup Development Environment

```bash
# Clone the repo
git clone https://github.com/lpmwfx/blender-jda-exporter.git
cd blender-jda-exporter

# Symlink to Blender addons directory (easier for development)
ln -s $(pwd)/jda_exporter.py ~/Library/Application\ Support/Blender/4.0/scripts/addons/
```

Now changes to `jda_exporter.py` will be reflected after Blender restart.

### Reload During Development

Add to Blender's Python console:
```python
import sys
import importlib

# Reload addon without restarting Blender
if 'jda_exporter' in sys.modules:
    importlib.reload(sys.modules['jda_exporter'])
```

---

## Support

Issues? Report at: https://github.com/lpmwfx/blender-jda-exporter/issues
