"""
A minimalist matplotlib style package for scientific presentations.

This package provides two main styles:
- science: Clean scientific style with small tick marks
- base: Minimal style without tick marks

It also includes custom color palettes and a continuous colormap for heatmaps.
"""

import os
from os import listdir
from os.path import isdir, join
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from .colors import COLOR_PALETTES, BASE_COLORS, BASE_CMAP, BASE_CMAP_R

__version__ = "0.3.0"

# Figure width constants based on text_width = 510/72.27 inches
TEXT_WIDTH = 510 / 72.27  # ~7.06 inches
FW = TEXT_WIDTH           # Full width
FW_2 = TEXT_WIDTH / 2     # Half width (~3.53 inches)
FW_3 = TEXT_WIDTH / 3     # Third width (~2.36 inches)


def get_palette(name='base'):
    """
    Get a color palette by name.
    
    Parameters
    ----------
    name : str
        Name of the color palette (default: 'base')
        
    Returns
    -------
    list
        List of hex color codes
        
    Raises
    ------
    ValueError
        If palette name is not found
    """
    if name not in COLOR_PALETTES:
        available = ', '.join(COLOR_PALETTES.keys())
        raise ValueError(f"Unknown palette '{name}'. Available palettes: {available}")
    return COLOR_PALETTES[name]


def get_cmap(name='minimalist'):
    """
    Get a matplotlib colormap.
    
    Parameters
    ----------
    name : str
        Name of the colormap ('minimalist' or 'minimalist_r')
        
    Returns
    -------
    matplotlib.colors.LinearSegmentedColormap
        Colormap object
    """
    if name == 'minimalist':
        return BASE_CMAP
    elif name == 'minimalist_r':
        return BASE_CMAP_R
    else:
        # Fallback to matplotlib's built-in colormaps
        return plt.get_cmap(name)


def setup_latex_path():
    """
    Setup LaTeX path for matplotlib to find the correct TeX installation.
    """
    import subprocess
    
    # Common TeX installation paths on macOS
    tex_paths = [
        "/Library/TeX/texbin",  # macOS TeX Live
        "/usr/local/texlive/2025/bin/x86_64-darwin",  # TeX Live 2025
        "/usr/local/texlive/2024/bin/x86_64-darwin",  # TeX Live 2024
        "/usr/local/texlive/2023/bin/x86_64-darwin",  # TeX Live 2023
        "/usr/texbin",  # Legacy macOS TeX
    ]
    
    # Find the correct LaTeX path
    latex_path = None
    for path in tex_paths:
        if os.path.exists(path):
            latex_path = path
            break
    
    if latex_path:
        # Add to PATH for subprocess calls
        if latex_path not in os.environ.get('PATH', ''):
            os.environ['PATH'] = latex_path + ':' + os.environ.get('PATH', '')
        
        # Configure matplotlib's texmanager to use the correct LaTeX executable
        try:
            from matplotlib import texmanager
            texmanager.TexManager.latex = os.path.join(latex_path, 'latex')
            texmanager.TexManager.dvipng = os.path.join(latex_path, 'dvipng')
            texmanager.TexManager.ghostscript = os.path.join(latex_path, 'gs')
        except:
            pass  # Non-fatal if texmanager configuration fails

def use_style(style_names):
    """
    Apply a minimalist style or styles to matplotlib.
    
    Parameters
    ----------
    style_names : str or list of str
        The style(s) to apply. Can be 'science' or 'base'.
        
    Raises
    ------
    ValueError
        If a style_name is not recognized
    """
    if isinstance(style_names, str):
        style_names = [style_names]
    
    # Setup LaTeX path if using science style
    if 'science' in style_names:
        setup_latex_path()
        
    style_paths = []
    for style_name in style_names:
        # Check in the base styles directory
        style_file = os.path.join(os.path.dirname(__file__), 'styles', f'{style_name}.mplstyle')
        if not os.path.exists(style_file):
            raise ValueError(f"Unknown style '{style_name}'. Available styles: 'science', 'base'")
        
        style_paths.append(style_file)
        
    plt.style.use(style_paths)


# Register included styles in the matplotlib style library
try:
    package_path = __path__[0]  # type: ignore[name-defined]
    styles_path = join(package_path, 'styles')
    if os.path.isdir(styles_path):
        stylesheets = plt.style.core.read_style_directory(styles_path)
        plt.style.core.update_nested_dict(plt.style.library, stylesheets)
        plt.style.core.available[:] = sorted(plt.style.library.keys())
except Exception:
    # Non-fatal: if registration fails, users can still call use_style()
    pass


def apply_minor_ticks(ax):
    """
    Apply minor ticks to an axis.
    
    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axis to apply minor ticks to
    """
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())


def figsize(width_fraction=1, aspect_ratio=None):
    """
    Calculate figure size based on text width.
    
    Parameters
    ----------
    width_fraction : float
        Fraction of text width (default: 1 for full width)
    aspect_ratio : float, optional
        Height/width ratio. If None, uses golden ratio (~0.618)
        
    Returns
    -------
    tuple
        (width, height) in inches
    """
    if aspect_ratio is None:
        aspect_ratio = (5**0.5 - 1) / 2  # Golden ratio
    width = TEXT_WIDTH * width_fraction
    height = width * aspect_ratio
    return (width, height)


# Convenience imports
__all__ = [
    'use_style',
    'setup_latex_path',
    'get_palette', 
    'get_cmap',
    'apply_minor_ticks',
    'figsize',
    'COLOR_PALETTES',
    'BASE_COLORS',
    'BASE_CMAP',
    'BASE_CMAP_R',
    'TEXT_WIDTH',
    'FW',
    'FW_2',
    'FW_3',
]