"""
Minimalist - A clean matplotlib style package for scientific figures.

Uses CMU Sans Serif font and Computer Modern for math notation.
No LaTeX/TeX required - uses matplotlib's mathtext for Greek letters and equations.

Usage:
    import minimalist
    minimalist.use_style('white')

    # Use figure width constants based on standard text width
    fig, ax = plt.subplots(figsize=(minimalist.FW_2, minimalist.FW_3))

    # Use the continuous colormap for heatmaps
    plt.imshow(data, cmap='minimalist')
"""

import functools
import os

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

try:
    import scicomap as sc
except (AttributeError, ImportError, TypeError):
    sc = None

__version__ = "2.1.0"
__author__ = "Suraj Sahu"

# =============================================================================
# Figure Width Constants
# =============================================================================
# Based on standard LaTeX article text width: 510pt = 7.06 inches
TEXT_WIDTH = 510 / 72.27  # ~7.06 inches

FW = TEXT_WIDTH  # Full width
FW_2 = TEXT_WIDTH / 2  # Half width (~3.53 inches)
FW_3 = TEXT_WIDTH / 3  # Third width (~2.36 inches)
FW_4 = TEXT_WIDTH / 4  # Quarter width (~1.77 inches)

# =============================================================================
# Color Palette
# =============================================================================
# Qualitative color palette
BASE_COLORS = ["#AB3019", "#FE7002", "#F4B43E", "#86B4C4", "#00768C", "#003547"]
QUALITATIVE_COLORS = BASE_COLORS

# =============================================================================
# Colormaps
# =============================================================================
DIVERGING_CMAP = "pride"
SEQUENTIAL_CMAP = "inferno"

# Continuous colormap for heatmaps (interpolated from BASE_COLORS)
_BASE_CMAP = LinearSegmentedColormap.from_list("minimalist", BASE_COLORS)
_BASE_CMAP_R = LinearSegmentedColormap.from_list("minimalist_r", BASE_COLORS[::-1])

# Register colormaps with matplotlib. Older Python versions use a local
# warm-to-cool fallback because compatible scicomap releases are unavailable.
if sc is None:
    pride_cmap = LinearSegmentedColormap.from_list("pride", BASE_COLORS)
else:
    pride_cmap = sc.ScicoDiverging(cmap="pride").get_mpl_color_map()

try:
    plt.colormaps.register(cmap=pride_cmap, name="pride")
except ValueError:
    # Already registered
    pass

try:
    plt.colormaps.register(cmap=_BASE_CMAP, name="minimalist")
    plt.colormaps.register(cmap=_BASE_CMAP_R, name="minimalist_r")
except ValueError:
    # Already registered
    pass

# =============================================================================
# Style Functions
# =============================================================================
AVAILABLE_STYLES = ("white", "black")


def use_style(style_name="white"):
    """
    Apply a minimalist style to matplotlib.

    Parameters
    ----------
    style_name : str
        Style to apply: 'white' or 'black' (default: 'white')

    Examples
    --------
    >>> import minimalist
    >>> minimalist.use_style('white')
    """
    style_file = os.path.join(os.path.dirname(__file__), "styles", f"{style_name}.mplstyle")

    if not os.path.exists(style_file):
        available = ", ".join(repr(style) for style in AVAILABLE_STYLES)
        raise ValueError(f"Unknown style '{style_name}'. Available: {available}")

    plt.style.use(style_file)
    # Explicitly ensure unicode minus is disabled (some fonts lack the glyph)
    plt.rcParams["axes.unicode_minus"] = False
    enable_errorbar_marker_gap()


def enable_errorbar_marker_gap(default=True):
    """
    Make Matplotlib error bars stop behind hollow markers by default.

    Parameters
    ----------
    default : bool
        Default value for Matplotlib's ``marker_gap`` errorbar option.
    """
    from matplotlib.axes import Axes

    if getattr(Axes.errorbar, "_minimalist_marker_gap_default", None) == default:
        return

    original_errorbar = getattr(Axes.errorbar, "_minimalist_original_errorbar", Axes.errorbar)
    original_draw = getattr(Axes.draw, "_minimalist_original_draw", Axes.draw)

    @functools.wraps(original_errorbar)
    def patched_errorbar(self, *args, **kwargs):
        marker_gap = kwargs.pop("marker_gap", default)
        container = original_errorbar(self, *args, **kwargs)
        if marker_gap:
            _register_marker_gap_errorbar(self, container)
        return container

    @functools.wraps(original_draw)
    def patched_draw(self, renderer):
        apply_errorbar_marker_gap(self)
        return original_draw(self, renderer)

    patched_errorbar._minimalist_original_errorbar = original_errorbar
    patched_errorbar._minimalist_marker_gap_default = default
    Axes.errorbar = patched_errorbar
    patched_draw._minimalist_original_draw = original_draw
    Axes.draw = patched_draw


def apply_errorbar_marker_gap(ax):
    """
    Apply marker-footprint gaps to error bars registered on an Axes.

    This is called automatically during drawing after ``use_style()``.
    """
    for container in getattr(ax, "_minimalist_marker_gap_containers", []):
        _apply_marker_gap_to_errorbar(ax, container)


def _register_marker_gap_errorbar(ax, container):
    if not hasattr(ax, "_minimalist_marker_gap_containers"):
        ax._minimalist_marker_gap_containers = []
    ax._minimalist_marker_gap_containers.append(container)

    _, _, barlinecols = container.lines
    for barlinecol in barlinecols:
        if not hasattr(barlinecol, "_minimalist_marker_gap_original_segments"):
            barlinecol._minimalist_marker_gap_original_segments = [
                segment.copy() for segment in barlinecol.get_segments()
            ]


def _apply_marker_gap_to_errorbar(ax, container):
    """Split errorbar line segments so they stop at the marker footprint."""
    data_line = container.lines[0]
    if data_line is None:
        return

    x_data = np.asarray(data_line.get_xdata(), dtype=float)
    y_data = np.asarray(data_line.get_ydata(), dtype=float)
    if len(x_data) == 0:
        return

    marker_radius_points = 0.5 * float(data_line.get_markersize()) + 0.5 * float(
        data_line.get_markeredgewidth()
    )
    marker_radius_pixels = ax.figure.dpi * marker_radius_points / 72.0
    point_pixels = ax.transData.transform(np.column_stack([x_data, y_data]))

    _, _, barlinecols = container.lines
    for barlinecol in barlinecols:
        split_segments = []
        original_segments = getattr(
            barlinecol,
            "_minimalist_marker_gap_original_segments",
            barlinecol.get_segments(),
        )
        for segment in original_segments:
            if len(segment) != 2:
                split_segments.append(segment)
                continue

            x0, y0 = segment[0].astype(float)
            x1, y1 = segment[1].astype(float)
            if np.isclose(x0, x1):
                split_segments.extend(
                    _split_marker_gap_segment(
                        ax,
                        segment,
                        point_pixels,
                        x_data,
                        y_data,
                        marker_radius_pixels,
                        axis="y",
                    )
                )
            elif np.isclose(y0, y1):
                split_segments.extend(
                    _split_marker_gap_segment(
                        ax,
                        segment,
                        point_pixels,
                        x_data,
                        y_data,
                        marker_radius_pixels,
                        axis="x",
                    )
                )
            else:
                split_segments.append(segment)

        barlinecol.set_segments(split_segments)


def _split_marker_gap_segment(
    ax,
    segment,
    point_pixels,
    x_data,
    y_data,
    marker_radius_pixels,
    axis,
):
    if axis == "y":
        const_index, var_index = 0, 1
    else:
        const_index, var_index = 1, 0

    const_value = float(segment[0, const_index])
    var_low, var_high = np.sort(segment[:, var_index].astype(float))
    segment_mid = np.array([[0.0, 0.0]])
    segment_mid[0, const_index] = const_value
    segment_mid[0, var_index] = 0.5 * (var_low + var_high)
    segment_mid_pixel = ax.transData.transform(segment_mid)[0]

    const_pixel_axis = const_index
    var_pixel_axis = var_index
    idx = int(
        np.argmin(np.abs(point_pixels[:, const_pixel_axis] - segment_mid_pixel[const_pixel_axis]))
    )
    marker_center = np.array([[x_data[idx], y_data[idx]]])
    marker_center_value = float(marker_center[0, var_index])
    if not (var_low < marker_center_value < var_high):
        return [segment]

    marker_center_pixel = ax.transData.transform(marker_center)[0]
    low_pixel = marker_center_pixel.copy()
    high_pixel = marker_center_pixel.copy()
    low_pixel[var_pixel_axis] -= marker_radius_pixels
    high_pixel[var_pixel_axis] += marker_radius_pixels
    gap_low = ax.transData.inverted().transform(low_pixel)[var_index]
    gap_high = ax.transData.inverted().transform(high_pixel)[var_index]
    gap_low, gap_high = np.sort([gap_low, gap_high])

    split_segments = []
    if var_low < gap_low:
        low_segment = segment.astype(float).copy()
        low_segment[:, var_index] = [var_low, min(gap_low, var_high)]
        split_segments.append(low_segment)
    if gap_high < var_high:
        high_segment = segment.astype(float).copy()
        high_segment[:, var_index] = [max(gap_high, var_low), var_high]
        split_segments.append(high_segment)
    return split_segments


def get_cmap(type_="diverging"):
    """
    Get the recommended colormap based on data type.

    Parameters
    ----------
    type_ : str
        Type of data: 'diverging', 'sequential', or 'qualitative'.
        Defaults to 'diverging' ('pride').

    Returns
    -------
    matplotlib.colors.Colormap or list
        The colormap object, or list of colors for qualitative.

    Examples
    --------
    >>> cmap = minimalist.get_cmap('diverging')
    >>> plt.imshow(data, cmap=cmap)
    """
    if type_ == "diverging":
        return mpl.colormaps.get_cmap(DIVERGING_CMAP)
    elif type_ == "sequential":
        return mpl.colormaps.get_cmap(SEQUENTIAL_CMAP)
    elif type_ == "qualitative":
        return QUALITATIVE_COLORS
    elif type_ in ["minimalist", "minimalist_r"]:
        return mpl.colormaps.get_cmap(type_)
    else:
        return mpl.colormaps.get_cmap(type_)


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
        aspect_ratio = 1  # Square ratio
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
        if hasattr(handle, "get_color"):
            color = handle.get_color()
        elif hasattr(handle, "get_facecolor"):
            color = handle.get_facecolor()
        else:
            continue

        # Handle array colors (from scatter plots)
        if hasattr(color, "__len__") and not isinstance(color, str) and len(color) > 0:
            color = color[0] if hasattr(color[0], "__len__") else color

        text.set_color(color)


def remove_all_clipping(fig):
    """
    Remove clipping from all artists in a figure.
    This allows elements (like lines or markers) to be drawn outside the axes boundaries.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        The figure to remove clipping from.

    Examples
    --------
    >>> fig, ax = plt.subplots()
    >>> ax.plot([-1, 2], [-1, 2], clip_on=True)
    >>> minimalist.remove_all_clipping(fig)
    """
    for artist in fig.findobj():
        if hasattr(artist, "set_clip_path"):
            artist.set_clip_path(None)
        if hasattr(artist, "set_clip_box"):
            artist.set_clip_box(None)


# =============================================================================
# Alpha Constants
# =============================================================================
FILL_ALPHA = 0.1


# =============================================================================
# Public API
# =============================================================================
__all__ = [
    "AVAILABLE_STYLES",
    "BASE_COLORS",
    "DIVERGING_CMAP",
    "FILL_ALPHA",
    "FW",
    "FW_2",
    "FW_3",
    "FW_4",
    "QUALITATIVE_COLORS",
    "SEQUENTIAL_CMAP",
    "TEXT_WIDTH",
    "__version__",
    "apply_errorbar_marker_gap",
    "color_legend_text",
    "enable_errorbar_marker_gap",
    "figsize",
    "get_cmap",
    "remove_all_clipping",
    "use_style",
]
