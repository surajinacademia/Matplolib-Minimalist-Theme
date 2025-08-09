# Minimalist RdBu

A minimalist Matplotlib style for scientific presentations featuring a carefully curated RdBu color palette and optional CMU Sans Serif font.

## Features

- Clean, minimalist design optimized for presentations
- Optional CMU Sans Serif font with LaTeX integration
- Carefully selected RdBu color palette
- Removed chartjunk (no top and right spines, no grid)
- Optimized for PDF output

## Installation

```bash
# Optional: for CMU Sans Serif font with LaTeX
# macOS: brew install --cask mactex
# Ubuntu: sudo apt-get install texlive-full
# Windows: Install MiKTeX

# Development install
pip install -e .
```

## Requirements

- Python >= 3.8
- matplotlib >= 3.5.0
- TeX Live distribution (for CMU Sans Serif font)

## Usage

The package provides three style components that can be used individually or combined:

```python
import minimalist_rdbu

# Use all styles (default: base + rdbu + sans-serif)
minimalist_rdbu.use_style('all')

# Or use individual components
minimalist_rdbu.use_style('base')  # Base style only
minimalist_rdbu.use_style('languages/sans-serif')  # CMU Sans Serif font
minimalist_rdbu.use_style('color/rdbu')  # Color scheme only
```

See the `examples/showcase.py` for a comprehensive demonstration of available plot types.

## Style Components

1. Base Style (`base.mplstyle`):
   - Clean figure layout
   - Removed top and right spines
   - Optimized line widths and marker sizes
   - Professional legend formatting

2. Font Settings (`languages/sans-serif.mplstyle`):
   - CMU Sans Serif font with LaTeX integration
   - Optimized font sizes for presentations
   - High-quality text rendering

3. Color Scheme (`color/rdbu.mplstyle`):
   - Professional RdBu color palette
   - Colorblind-friendly
   - Excellent for scientific presentations

## License

MIT License

## Author

Suraj Sahu 
