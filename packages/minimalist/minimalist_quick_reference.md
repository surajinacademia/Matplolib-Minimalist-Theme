# Minimalist Package Quick Reference

## Installation
- **Environment**: `latest_updates` conda environment
- **Status**: ✅ Installed and ready to use

## Basic Usage

### Import
```python
import minimalist
import matplotlib.pyplot as plt
import numpy as np
import os
```

### Style Philosophy
- **Base Style**: `minimalist.use_style('base')` - **USE FOR EVERYTHING** (everyday, presentations, reports)
- **Science Style**: `minimalist.use_style('science')` - **PUBLICATIONS ONLY** (papers, journals)

### Quick Start Template
```python
import minimalist
import matplotlib.pyplot as plt
import numpy as np
import os

# Create output directory
os.makedirs('plots', exist_ok=True)

# Use base style (default for everyday use)
minimalist.use_style('base')

# Your plotting code here
x = np.linspace(0, 2*np.pi, 100)
plt.plot(x, np.sin(x), label=r'$\sin(\theta)$')
plt.xlabel(r'$\theta$ [radians]')
plt.ylabel(r'$f(\theta)$')
plt.legend()
plt.savefig('plots/my_plot.pdf')
plt.show()
```

## Color Palettes

### Get Colors
```python
colors = minimalist.get_palette('RdBuYe_q')  # 5 colors (default)
colors = minimalist.get_palette('RdBuBl_q')  # 9 colors
```

### Style + Color Combinations
```python
# Base with custom colors (everyday use)
minimalist.use_style(['base', 'rdbuye'])    # 5 colors
minimalist.use_style(['base', 'rdbubl'])    # 9 colors

# Science with custom colors (publications only)
minimalist.use_style(['science', 'rdbuye'])
```

## Heatmaps
```python
from matplotlib.colors import LinearSegmentedColormap

# Create smooth colormap
colors = minimalist.get_palette('Rdbu_w')
cmap = LinearSegmentedColormap.from_list('custom', colors)

# Always use smooth interpolation
plt.imshow(data, cmap=cmap, interpolation='bilinear')
```

## Key Features
- ✅ **No Grid Lines**: Clean appearance
- ✅ **Greek Letters**: Use `r'$\alpha$'`, `r'$\beta$'`, `r'$\theta$'`, `r'$\phi$'`
- ✅ **High Quality**: 300 DPI PDF output
- ✅ **Defined Colors**: Not matplotlib defaults
- ✅ **Base Style**: Only bottom/left spines
- ✅ **Science Style**: All spines visible

## Remember
- **Base for everyday use** - data exploration, presentations, reports
- **Science for publications only** - academic papers, journals
- Always save to organized directories (`plots/` folder)
- Never use grid lines
- Use mathtext for Greek letters in base style 