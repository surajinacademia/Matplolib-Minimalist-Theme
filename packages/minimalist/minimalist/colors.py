"""Color palettes for minimalist matplotlib styles."""

from matplotlib.colors import LinearSegmentedColormap, ListedColormap
import matplotlib.pyplot as plt

# Base colors for quantitative plots
BASE_COLORS = ['#AB3019', '#FE7002', '#F4B43E', '#86B4C4', '#00768C', '#003547']

# Create continuous colormap for heatmaps
BASE_CMAP = LinearSegmentedColormap.from_list('base', BASE_COLORS)
BASE_CMAP_R = LinearSegmentedColormap.from_list('base_r', BASE_COLORS[::-1])

# Register colormaps with matplotlib
try:
    plt.colormaps.register(cmap=BASE_CMAP, name='minimalist')
    plt.colormaps.register(cmap=BASE_CMAP_R, name='minimalist_r')
except ValueError:
    # Already registered
    pass

# Legacy support - keep minimal palettes
COLOR_PALETTES = {
    'base': BASE_COLORS,
    'base_r': BASE_COLORS[::-1],
}