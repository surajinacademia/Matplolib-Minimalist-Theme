# Minimalist

A minimalist matplotlib style package for scientific presentations and publications with custom color palettes.

## Installation

```bash
pip install minimalist
```

For LaTeX support (publications only), install with:
```bash
pip install minimalist[latex]
```

## Usage

### Basic Usage

```python
import matplotlib.pyplot as plt
import minimalist  # registers bundled styles on import

# Use the base style (default for everyday use)
plt.style.use('base')  # or minimalist.use_style('base')

# Create your plots with Greek letters support
plt.plot([1, 2, 3], [1, 4, 9], label=r'$\alpha$ data')
plt.xlabel(r'$\theta$')
plt.ylabel(r'$\phi$')
plt.legend()
plt.show()
```

### Available Styles

#### Base Styles
- `base`: **Default style for everyday use** - No LaTeX, mathtext for Greek letters, minimal design
- `science`: **For publications only** - Full LaTeX support with all tick marks

#### Color Styles
- `rdbuye`: RdBuYe qualitative palette (5 colors: prussian blue, cerulean, light blue, gamboge, auburn)
- `rdbubl`: RdBuBl qualitative palette (9 colors: blue to red with black and grays)

#### Font Styles
- `sans-serif`: CMU Sans Serif font with LaTeX support (publications only)

### Combining Styles

You can combine multiple styles:

```python
# Base style with custom colors (everyday use)
minimalist.use_style(['base', 'rdbuye'])

# Science style with custom colors (publications only)
minimalist.use_style(['science', 'rdbubl', 'sans-serif'])
```

### Using Color Palettes

Access color palettes directly for smooth heatmaps:

```python
# Get a color palette
colors = minimalist.get_palette('RdBuYe_q')

# Create a smooth colormap
from matplotlib.colors import LinearSegmentedColormap
cmap = LinearSegmentedColormap.from_list('custom', colors)

# Use with smooth interpolation
plt.imshow(data, cmap=cmap, interpolation='bilinear')
```

Available color palettes:
- **Diverging**: `RdBuYe`, `RdBuYe_r`, `Rdbu_bl`, `Rdbu_bl_r`, `Rdbu_w`, `Rdbu_w_r`
- **Sequential**: `Rd`, `Rd_r`, `Bu`, `Bu_r`
- **Qualitative**: `RdBuBl_q`, `RdBuYe_q`

### Examples

See the `examples/` directory for detailed examples.

## Features

- **Base style**: Default for everyday use with mathtext support for Greek letters
- **Science style**: Publications only with full LaTeX support
- Custom color palettes designed for clarity and aesthetics
- Smooth heatmap interpolation
- No grid lines for clean appearance
- High-quality PDF output with proper DPI settings

## Style Philosophy

- **Base style**: Use this for all everyday plotting, data exploration, and presentations
- **Science style**: Use only for final publication figures that require LaTeX rendering

## Requirements

- Python >= 3.8
- matplotlib >= 3.5.0
- numpy >= 1.20.0

## License

MIT License - see LICENSE file for details.
