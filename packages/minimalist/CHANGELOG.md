# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-12-09

### Changed
- **Breaking**: Simplified to single color palette (`BASE_COLORS`)
- **Breaking**: Removed all old color palettes (RdBu, RdBuYe, etc.)
- **Breaking**: Removed `rdbubl`, `rdbuye`, `sans-serif` style overlays
- Switched from LaTeX to mathtext (`text.usetex: False`)
- Updated default figure size to `(FW_2, FW_3)` = `(3.53, 2.36)` inches
- Simplified API to just `use_style()` and `get_cmap()`

### Added
- `BASE_COLORS` - Single 6-color palette for all plots
- `minimalist` / `minimalist_r` colormaps for heatmaps
- Figure width constants: `FW`, `FW_2`, `FW_3`
- `figsize()` helper function
- Comprehensive README with usage examples

### Removed
- Old color palettes (RdBuYe, Rdbu_bl, Rdbu_w, etc.)
- Multiple example files (consolidated to single demo.py)
- LaTeX dependency (`text.usetex: True`)
- Legacy folders and duplicate files

## [0.2.0] - 2024-11-15

### Added
- Initial public release with science and base styles
- Multiple color palettes
- LaTeX support

## [0.1.0] - 2024-10-01

### Added
- Initial development version
