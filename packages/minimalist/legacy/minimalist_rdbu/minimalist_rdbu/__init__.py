"""
A minimalist matplotlib style package for scientific presentations.
"""

import os
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

__version__ = "0.1.0"

def use_style(style_name='all'):
    """
    Apply the minimalist RdBu style to matplotlib.
    
    Parameters
    ----------
    style_name : str, optional
        The style to apply. Options are 'all', 'base', 'sans-serif'.
        Default is 'all' which applies all styles.
    """
    style_dir = os.path.join(os.path.dirname(__file__), 'styles')
    
    if style_name == 'all':
        # Apply styles in order: base first, then color, then language-specific
        plt.style.use([
            os.path.join(style_dir, 'base.mplstyle'),
            os.path.join(style_dir, 'color', 'rdbu.mplstyle'),
            os.path.join(style_dir, 'languages', 'sans-serif.mplstyle')
        ])
    else:
        if style_name == 'base':
            plt.style.use(os.path.join(style_dir, 'base.mplstyle'))
        elif style_name == 'sans-serif':
            plt.style.use(os.path.join(style_dir, 'languages', 'sans-serif.mplstyle'))
        elif style_name == 'rdbu':
            plt.style.use(os.path.join(style_dir, 'color', 'rdbu.mplstyle'))
        else:
            raise ValueError(f"Unknown style '{style_name}'. Available styles: 'all', 'base', 'sans-serif', 'rdbu'")

def apply_minor_ticks(ax):
    """
    Apply minor ticks to an axis.
    
    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axis to apply minor ticks to.
    """
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator()) 