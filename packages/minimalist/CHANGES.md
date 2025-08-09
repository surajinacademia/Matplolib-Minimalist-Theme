# Changes

## Version 0.2.0 - Package Reorganization

### Structure Changes
- Reorganized package structure following SciencePlots conventions
- Renamed style files:
  - `minimalist_science.mplstyle` → `science.mplstyle`
  - `minimalist_base.mplstyle` → `base.mplstyle`
- Created proper subdirectory structure:
  - Base styles in `styles/`
  - Color styles in `styles/color/`
  - Font styles in `styles/fonts/`

### New Files Added
- `pyproject.toml` - Modern Python packaging configuration
- `MANIFEST.in` - Package data inclusion rules
- `.gitignore` - Git ignore patterns
- `LICENSE` - MIT License
- `colors.py` - Separated color palettes into dedicated module
- Color style files:
  - `styles/color/rdbuye.mplstyle`
  - `styles/color/rdbubl.mplstyle`
- `examples/demo.py` - Comprehensive usage examples

### Code Improvements
- Updated `__init__.py`:
  - Improved `use_style()` function to support multiple styles
  - Added support for style combinations (e.g., ['science', 'rdbuye'])
  - Moved `COLOR_PALETTES` to separate `colors.py` module
- Updated color cycle in `science.mplstyle` to use RdBuYe_q palette
- Cleaned up `base.mplstyle` to properly disable ticks and spines

### Documentation
- Completely rewrote `README.md` with:
  - Clear installation instructions
  - Usage examples
  - Style combination examples
  - Complete list of available palettes
  - Simplified and focused content 