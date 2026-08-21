import pytest
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
import minimalist


def test_version():
    assert minimalist.__version__ == "2.1.0"


def test_figsize_scaling():
    # Test default full width
    width, height = minimalist.figsize()
    assert width == minimalist.TEXT_WIDTH
    assert height == width  # Default aspect ratio is 1 (square)

    # Test half width
    width, height = minimalist.figsize(0.5)
    assert width == minimalist.TEXT_WIDTH * 0.5
    assert height == width

    # Test custom aspect ratio
    width, height = minimalist.figsize(1, 0.5)
    assert width == minimalist.TEXT_WIDTH
    assert height == width * 0.5


def test_get_cmap():
    # Test qualitative returns list
    qualitative = minimalist.get_cmap("qualitative")
    assert isinstance(qualitative, list)
    assert qualitative == minimalist.BASE_COLORS

    # Test custom minimalists maps are returned
    mini = minimalist.get_cmap("minimalist")
    assert isinstance(mini, LinearSegmentedColormap)

    mini_r = minimalist.get_cmap("minimalist_r")
    assert isinstance(mini_r, LinearSegmentedColormap)


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_white_style():
    # Clean matplotlib state
    plt.rcdefaults()

    # Assert values changed
    minimalist.use_style("white")

    assert plt.rcParams["figure.figsize"] == [3.53, 3.53]
    assert plt.rcParams["font.family"] == ["CMU Sans Serif"]
    assert plt.rcParams["font.size"] == 8
    assert plt.rcParams["axes.labelsize"] == 8
    assert plt.rcParams["axes.titlesize"] == 8
    assert plt.rcParams["xtick.labelsize"] == 8
    assert plt.rcParams["ytick.labelsize"] == 8
    assert plt.rcParams["legend.fontsize"] == 8
    assert plt.rcParams["legend.title_fontsize"] == 8
    assert plt.rcParams["figure.titlesize"] == 8
    assert plt.rcParams["axes.spines.top"] is True
    assert plt.rcParams["axes.spines.right"] is True
    assert plt.rcParams["figure.facecolor"] == "white"
    assert plt.rcParams["axes.facecolor"] == "white"
    assert plt.rcParams["savefig.facecolor"] == "white"
    assert plt.rcParams["savefig.transparent"] is False


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_black_style():
    plt.rcdefaults()
    minimalist.use_style("black")

    assert plt.rcParams["figure.facecolor"] == "black"
    assert plt.rcParams["axes.facecolor"] == "black"
    assert plt.rcParams["savefig.facecolor"] == "black"
    assert plt.rcParams["text.color"] == "white"
    assert plt.rcParams["axes.edgecolor"] == "white"
    assert plt.rcParams["axes.labelcolor"] == "white"
    assert plt.rcParams["xtick.color"] == "white"
    assert plt.rcParams["ytick.color"] == "white"


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_default_style_is_white():
    plt.rcdefaults()
    minimalist.use_style()

    assert plt.rcParams["figure.facecolor"] == "white"
    assert plt.rcParams["text.color"] == "black"


def test_unknown_style_lists_available_styles():
    with pytest.raises(ValueError, match="Available: 'white', 'black'"):
        minimalist.use_style("science")


def _errorbar_center_rgb(marker_gap=None):
    fig, ax = plt.subplots(figsize=(3, 3), dpi=100)
    kwargs = {}
    if marker_gap is not None:
        kwargs["marker_gap"] = marker_gap
    container = ax.errorbar(
        [0],
        [0],
        yerr=[1],
        fmt="o",
        markerfacecolor="none",
        markeredgecolor="black",
        markersize=20,
        ecolor="red",
        elinewidth=4,
        capsize=0,
        **kwargs,
    )
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1.5, 1.5)
    fig.canvas.draw()

    rgba = np.asarray(fig.canvas.buffer_rgba())
    cx, cy = ax.transData.transform((0, 0))
    row = rgba.shape[0] - 1 - int(round(cy))
    col = int(round(cx))
    center_rgb = rgba[row, col, :3]
    markerfacecolor = container.lines[0].get_markerfacecolor()
    plt.close(fig)
    return center_rgb, markerfacecolor


def _errorbar_crossing_count(marker_gap=None):
    fig, ax = plt.subplots(figsize=(3, 3), dpi=100)
    kwargs = {}
    if marker_gap is not None:
        kwargs["marker_gap"] = marker_gap
    container = ax.errorbar(
        [0],
        [0],
        yerr=[1],
        fmt="o",
        markerfacecolor="none",
        markeredgecolor="black",
        markersize=20,
        ecolor="red",
        elinewidth=4,
        capsize=0,
        **kwargs,
    )
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1.5, 1.5)
    fig.canvas.draw()

    crossings = 0
    x_marker = float(container.lines[0].get_xdata()[0])
    y_marker = float(container.lines[0].get_ydata()[0])
    for collection in ax.collections:
        if not hasattr(collection, "get_segments"):
            continue
        for segment in collection.get_segments():
            if len(segment) != 2 or not np.isclose(segment[0, 0], segment[1, 0]):
                continue
            x_bar = float(segment[0, 0])
            y_low, y_high = np.sort(segment[:, 1].astype(float))
            if np.isclose(x_bar, x_marker) and y_low < y_marker < y_high:
                crossings += 1
    markerfacecolor = container.lines[0].get_markerfacecolor()
    plt.close(fig)
    return crossings, markerfacecolor


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_use_style_enables_errorbar_marker_gap_by_default():
    plt.rcdefaults()
    minimalist.use_style("white")

    center_rgb, markerfacecolor = _errorbar_center_rgb()

    assert markerfacecolor == "none"
    assert np.linalg.norm(center_rgb.astype(float) - np.array([255, 255, 255])) < 10


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_errorbar_marker_gap_splits_line_segments():
    plt.rcdefaults()
    minimalist.use_style("white")
    plt.rcParams.update({"figure.facecolor": "none", "axes.facecolor": "none"})

    crossings, markerfacecolor = _errorbar_crossing_count()

    assert markerfacecolor == "none"
    assert crossings == 0


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_errorbar_marker_gap_can_be_disabled():
    plt.rcdefaults()
    minimalist.use_style("white")

    center_rgb, markerfacecolor = _errorbar_center_rgb(marker_gap=False)
    crossings, _ = _errorbar_crossing_count(marker_gap=False)

    assert markerfacecolor == "none"
    assert crossings == 1
    assert center_rgb[0] > 200
    assert center_rgb[1] < 80
    assert center_rgb[2] < 80
