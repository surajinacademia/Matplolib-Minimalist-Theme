# Minimalist RdBu

A clean, minimalist matplotlib style for scientific presentations featuring CMU Sans Serif font and a carefully selected RdBu color palette.

## Features

- Clean, minimalist design optimized for presentations
- Professional CMU Sans Serif font with LaTeX integration
- Carefully selected RdBu color palette
- Removed chartjunk (no top and right spines, no grid)
- Optimized for PDF output

## Installation

```bash
# First, ensure you have TeX Live installed for the CMU Sans Serif font
# macOS: brew install --cask mactex
# Ubuntu: sudo apt-get install texlive-full
# Windows: Install MiKTeX

# Then install the package
pip install .
```

## Requirements

- Python >= 3.8
- matplotlib >= 3.5.0
- TeX Live distribution (for CMU Sans Serif font)

## Usage

The package provides three style components that can be used individually or combined:

```python
import minimalist_rdbu

# Use all styles (default)
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








# Things to do

@minimalist_rdbu okay we need to update this package and make a drastic reorganization, update the information and change styles.

Here are the things I want

1. The color maps I want to use are:
   - RdBu:

2. Fonts to use:
   - Text fonts: Sans-Serif Computer Modern
   - Math fonts: 
