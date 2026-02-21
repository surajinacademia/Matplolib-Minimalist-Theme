"""
Minimalist - A clean matplotlib style package for scientific figures.

Uses CMU Sans Serif font and Computer Modern for math notation.
No LaTeX/TeX required - uses matplotlib's mathtext for Greek letters and equations.

Usage:
    import minimalist
    minimalist.use_style('science')
    
    # Use figure width constants based on standard text width
    fig, ax = plt.subplots(figsize=(minimalist.FW_2, minimalist.FW_3))
    
    # Use the continuous colormap for heatmaps
    plt.imshow(data, cmap='minimalist')
"""

import os
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

__version__ = "2.0.0"
__author__ = "Suraj Sahu"

# =============================================================================
# Figure Width Constants
# =============================================================================
# Based on standard LaTeX article text width: 510pt = 7.06 inches
TEXT_WIDTH = 510 / 72.27  # ~7.06 inches

FW = TEXT_WIDTH           # Full width
FW_2 = TEXT_WIDTH / 2     # Half width (~3.53 inches)
FW_3 = TEXT_WIDTH / 3     # Third width (~2.36 inches)
FW_4 = TEXT_WIDTH / 4     # Quarter width (~1.77 inches)

# =============================================================================
# Color Palette
# =============================================================================
# Single color palette for quantitative plots
BASE_COLORS = ['#AB3019', '#FE7002', '#F4B43E', '#86B4C4', '#00768C', '#003547']

# =============================================================================
# Colormaps
# =============================================================================
# Continuous colormap for heatmaps (interpolated from BASE_COLORS)
_BASE_CMAP = LinearSegmentedColormap.from_list('minimalist', BASE_COLORS)
_BASE_CMAP_R = LinearSegmentedColormap.from_list('minimalist_r', BASE_COLORS[::-1])

# Register colormaps with matplotlib
try:
    plt.colormaps.register(cmap=_BASE_CMAP, name='minimalist')
    plt.colormaps.register(cmap=_BASE_CMAP_R, name='minimalist_r')
except ValueError:
    # Already registered
    pass

# =============================================================================
# Style Functions
# =============================================================================
def use_style(style_name='science'):
    """
    Apply the minimalist science style to matplotlib.
    
    Parameters
    ----------
    style_name : str
        Style to apply (default: 'science')
    
    Examples
    --------
    >>> import minimalist
    >>> minimalist.use_style('science')
    """
    style_file = os.path.join(os.path.dirname(__file__), 'styles', f'{style_name}.mplstyle')
    
    if not os.path.exists(style_file):
        raise ValueError(f"Unknown style '{style_name}'. Available: 'science'")
    
    plt.style.use(style_file)
    # Explicitly ensure unicode minus is disabled (some fonts lack the glyph)
    plt.rcParams['axes.unicode_minus'] = False


def get_cmap(name='minimalist'):
    """
    Get a colormap.
    
    Parameters
    ----------
    name : str
        Colormap name: 'minimalist' or 'minimalist_r'
    
    Returns
    -------
    LinearSegmentedColormap
        The colormap object
    
    Examples
    --------
    >>> cmap = minimalist.get_cmap()
    >>> plt.imshow(data, cmap=cmap)
    """
    if name == 'minimalist':
        return _BASE_CMAP
    elif name == 'minimalist_r':
        return _BASE_CMAP_R
    else:
        return plt.get_cmap(name)


def figsize(width_fraction=1, aspect_ratio=None):
    """
    Calculate figure size based on text width.
    
    Parameters
    ----------
    width_fraction : float
        Fraction of text width (default: 1 for full width)
    aspect_ratio : float, optional
        Height/width ratio. Default: golden ratio (~0.618)
    
    Returns
    -------
    tuple
        (width, height) in inches
    
    Examples
    --------
    >>> fig, ax = plt.subplots(figsize=minimalist.figsize(0.5))
    """
    if aspect_ratio is None:
        aspect_ratio = (5**0.5 - 1) / 2  # Golden ratio
    width = TEXT_WIDTH * width_fraction
    height = width * aspect_ratio
    return (width, height)


def color_legend_text(ax):
    """
    Color legend text labels to match their corresponding line/marker colors.
    
    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axes containing the legend
    
    Examples
    --------
    >>> ax.plot(x, y1, label='Data 1')
    >>> ax.plot(x, y2, label='Data 2')
    >>> ax.legend()
    >>> minimalist.color_legend_text(ax)
    """
    legend = ax.get_legend()
    if legend is None:
        return
    
    for text, handle in zip(legend.get_texts(), legend.legend_handles):
        # Get color from the handle
        if hasattr(handle, 'get_color'):
            color = handle.get_color()
        elif hasattr(handle, 'get_facecolor'):
            color = handle.get_facecolor()
        else:
            continue
        
        # Handle array colors (from scatter plots)
        if hasattr(color, '__len__') and not isinstance(color, str):
            if len(color) > 0:
                color = color[0] if hasattr(color[0], '__len__') else color
        
        text.set_color(color)


# =============================================================================
# Register styles with matplotlib
# =============================================================================
try:
    _styles_path = os.path.join(os.path.dirname(__file__), 'styles')
    if os.path.isdir(_styles_path):
        _stylesheets = plt.style.core.read_style_directory(_styles_path)
        plt.style.core.update_nested_dict(plt.style.library, _stylesheets)
        plt.style.core.available[:] = sorted(plt.style.library.keys())
except Exception:
    pass


# =============================================================================
# Public API
# =============================================================================
__all__ = [
    # Version
    '__version__',
    # Style
    'use_style',
    # Figure sizing
    'TEXT_WIDTH', 'FW', 'FW_2', 'FW_3', 'FW_4', 'figsize',
    # Colors
    'BASE_COLORS', 'get_cmap',
    # Utilities
    'color_legend_text',
]