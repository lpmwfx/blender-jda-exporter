# Changelog

All notable changes to Blender JDA Exporter will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Animation keyframe export
- Hierarchy (parent/child) support
- Custom SDF operations export
- Live link to game engines
- Material node graph analysis

---

## [1.0.0] - 2025-11-21

### Added
- Initial release of Blender JDA Exporter
- Auto-detection of SDF types from object names
- Support for 6 SDF primitives: Sphere, Box, Cylinder, Torus, Capsule, Cone
- Material extraction from Principled BSDF nodes
- Batch export functionality
- JDA v1.0 format specification
- Cross-platform JSON output
- Complete documentation suite:
  - README.md with usage guide
  - INSTALLATION.md for all platforms
  - JDA_SPEC.md format specification
  - VIDEO_SCRIPT.md for showcase videos
  - RELEASE_NOTES.md
- Example scripts:
  - bubble_tree.py procedural generator
  - Templates in examples/README.md
- MIT License
- .gitignore for Python/Blender/macOS

### Technical Details
- Addon file size: 6.9 KB
- Output file size: ~200-400 bytes per asset
- Blender compatibility: 3.0+
- Python compatibility: 3.10+

### Performance
- Export speed: < 100ms for 10 objects
- File size reduction: 250x smaller than FBX
- Test scene (8 objects): 2.5 KB total

---

## Version History

- **v1.0.0** (2025-11-21) - Initial stable release

---

## Upgrade Guide

### From Pre-release to v1.0.0
No pre-release versions existed. This is the first release.

### Future Upgrades
Upgrade instructions will be added here for each new version.

---

## Deprecation Notices

None yet.

---

## Breaking Changes

None yet.

---

## Migration Guides

### v1.0.0 → v2.0.0 (When Released)
Will be documented here when v2.0.0 is released.

---

## Links

- [Latest Release](https://github.com/lpmwfx/blender-jda-exporter/releases/latest)
- [All Releases](https://github.com/lpmwfx/blender-jda-exporter/releases)
- [Issue Tracker](https://github.com/lpmwfx/blender-jda-exporter/issues)
- [Documentation](README.md)
