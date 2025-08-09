# Minimalist Package Examples

This directory contains demonstration scripts showcasing the features of the minimalist matplotlib style package.

## Demo Scripts

### 1. `demo.py`
Simple demonstration of the minimalist package features:
- Base style (default) with defined colors and Greek letters
- Base style with RdBuBl colors (9 lines demonstration)
- Smooth heatmap creation
- Science style for publications only

### 2. `comprehensive_demo.py`
Comprehensive showcase of all color palettes and plot types:
- Science style demonstration (publications only)
- Base style with all 9 RdBuBl colors
- Smooth heatmaps with diverging colormaps
- Style comparison: Base vs Science

**All PDF outputs are saved to the `plots/` directory**

## Generated Files

After running the demos, you'll find these files in `plots/`:
- `base_default.pdf` - Base style with defined colors and Greek letters
- `base_rdbubl.pdf` - Base style with RdBuBl_q colors (9 lines)
- `heatmap_rdbu_w.pdf` - Smooth heatmap using Rdbu_w colormap
- `science_publication.pdf` - Science style for publications
- `minimalist_showcase.pdf` - 4-page comprehensive showcase

## Color Palettes

### Qualitative (for line plots, categorical data)
- **RdBuYe_q**: 5 distinct colors (prussian blue, cerulean, light blue, gamboge, auburn)
- **RdBuBl_q**: 9 colors including black and grays for more categories

### Diverging (for data with positive/negative values)
- **RdBuYe**: Red-Blue-Yellow diverging
- **Rdbu_bl**: Red-Blue with black center
- **Rdbu_w**: Red-Blue with white center
- All have reversed versions (_r suffix)

### Sequential (for positive-only data)
- **Rd**: Red sequential (light to dark + black)
- **Bu**: Blue sequential (light to dark + black)
- Both have reversed versions (_r suffix)

## Style Features

### Base Style (Default for Everyday Use)
- **Spines**: Only bottom and left spines visible
- **Colors**: Uses defined color palette (not matplotlib defaults)
- **LaTeX**: No LaTeX dependency - works everywhere
- **Math**: Mathtext support for Greek letters (α, β, θ, φ, etc.)
- **Design**: Minimal, clean appearance
- **Grid**: No grid lines

### Science Style (Publications Only)
- **Spines**: All spines visible (top, right, bottom, left)
- **Colors**: Uses defined color palette
- **LaTeX**: Full LaTeX rendering for mathematical expressions
- **Ticks**: All tick marks visible with minor ticks
- **Typography**: Professional CMU Sans Serif font
- **Requirements**: LaTeX installation needed

## Key Features Demonstrated

- **Defined colors**: Both styles use custom color palettes, not matplotlib defaults
- **No grid lines**: Clean appearance without distracting grid lines
- **Greek letters**: Use mathtext for symbols in base style
- **Smooth heatmaps**: Bilinear interpolation for professional appearance
- **Multiple lines**: RdBuBl_q palette supports up to 9 distinct lines
- **Organized output**: All PDFs saved to `plots/` directory

## Running the Examples

```bash
# Run basic demo
python demo.py

# Run comprehensive demo (creates multi-page PDF)
python comprehensive_demo.py
```

## Style Philosophy

- **Base style**: Use for all everyday plotting, data exploration, and presentations
- **Science style**: Use only for final publication figures requiring LaTeX

## Requirements
- matplotlib >= 3.5.0
- numpy >= 1.20.0
- LaTeX installation (for science style only)
  - macOS: `brew install --cask mactex`
  - Ubuntu/Debian: `sudo apt-get install texlive-full`
  - Windows: Install MiKTeX from https://miktex.org/ 