"""
A minimalist matplotlib style package for scientific presentations.

This package provides two main styles:
- minimalist_science: With LaTeX support and tick marks
- minimalist_base: Minimal style without LaTeX and tick marks

It also includes custom color palettes for scientific visualization.
"""

import os
from os import listdir
from os.path import isdir, join
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib.colors import ListedColormap
from .colors import COLOR_PALETTES

__version__ = "0.2.0"

def get_palette(name):
    """
    Get a color palette by name.
    
    Parameters
    ----------
    name : str
        Name of the color palette
        
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

def get_cmap(name):
    """
    Get a matplotlib colormap from palette name.
    
    Parameters
    ----------
    name : str
        Name of the color palette
        
    Returns
    -------
    matplotlib.colors.ListedColormap
        Colormap object
    """
    palette = get_palette(name)
    return ListedColormap(palette)

def use_style(style_names):
    """
    Apply a minimalist style or styles to matplotlib.
    
    Parameters
    ----------
    style_names : str or list of str
        The style(s) to apply. Can be a base style like 'science' or 'base',
        or combined with color styles like ['science', 'rdbuye'].
        
    Raises
    ------
    ValueError
        If a style_name is not recognized
    """
    if isinstance(style_names, str):
        style_names = [style_names]
        
    style_paths = []
    for style_name in style_names:
        # Check in the base styles directory
        style_file = os.path.join(os.path.dirname(__file__), 'styles', f'{style_name}.mplstyle')
        if not os.path.exists(style_file):
            # Check in subdirectories (like 'color', 'fonts')
            for subdir in ['color', 'fonts']:
                style_file = os.path.join(os.path.dirname(__file__), 'styles', subdir, f'{style_name}.mplstyle')
                if os.path.exists(style_file):
                    break
            else:
                raise ValueError(f"Unknown style '{style_name}'.")
        
        style_paths.append(style_file)
        
    plt.style.use(style_paths)

# Register included styles in the matplotlib style library (like SciencePlots)
try:
    package_path = __path__[0]  # type: ignore[name-defined]
    styles_path = join(package_path, 'styles')
    if os.path.isdir(styles_path):
        stylesheets = plt.style.core.read_style_directory(styles_path)
        for inode in listdir(styles_path):
            new_data_path = join(styles_path, inode)
            if isdir(new_data_path):
                new_stylesheets = plt.style.core.read_style_directory(new_data_path)
                stylesheets.update(new_stylesheets)
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

# Convenience imports
__all__ = [
    'use_style',
    'get_palette', 
    'get_cmap',
    'apply_minor_ticks',
    'COLOR_PALETTES'
] 