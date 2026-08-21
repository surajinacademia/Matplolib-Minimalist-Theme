## Minimalist White and Black Styles

Clean, publication-ready Matplotlib styles for scientific figures, centered on a custom color palette, square layouts, and soft uncertainty visualization.

Two styles are available:

- `white` (the default): white background with black text, ticks, and axes.
- `black`: black background with white text, ticks, and axes.

---

### Core Principles

- **Minimal visual clutter**: Thin axes, short inward ticks, no grid by default, and frameless legends.
- **Publication-ready defaults**: Sizes and proportions tuned for LaTeX article layouts and high-resolution export.
- **Consistent visual language**: Line plots, scatter plots, and heatmaps share a unified color system.

---

### Typography

- **Main font**: `CMU Sans Serif` for all text.
- **Math text**: Computer Modern via Matplotlib’s `mathtext` (no LaTeX engine required).
- **Colors and sizes**:
  - Text color: **black**
  - **Base font size** (body text): **8 pt**
  - **Figure titles** (`figure.titlesize`): **8 pt**
  - **Axis titles and labels** (`axes.titlesize`, `axes.labelsize`): **8 pt**
  - **Tick labels** (`xtick.labelsize`, `ytick.labelsize`): **8 pt**
  - **Legend text** (`legend.fontsize`, `legend.title_fontsize`): **8 pt**
- **Unicode minus disabled** (`axes.unicode_minus: False`) to avoid missing glyphs with this font.

---

### Geometry & Figure Sizing

- **Text width basis (article layout)**: By default, figure widths are derived from a standard LaTeX article text width
  \( \text{TEXT\_WIDTH} = 510\ \text{pt} \approx 7.06\ \text{inches} \).

- **Width constants (article layout)**:
  - `FW` – full width (≈ 7.06")
  - `FW_2` – half width (≈ 3.53")
  - `FW_3` – third width (≈ 2.36")
  - `FW_4` – quarter width (≈ 1.77")

- **Default aspect**: `figsize()` defaults to **square plots** for visual consistency, especially useful for:
  - Multi-panel figures
  - 2D fields (e.g. heatmaps, spatial maps)
  - Side-by-side comparisons

- **Output format**: `savefig.format` is set to **PDF** so all figures are saved as **vector graphics** by default, ideal for print and zooming in digital readers.

---

### LaTeX Integration & Two-Column Layouts

The style is designed to drop cleanly into common two-column conference formats (e.g. AISTATS-style).

- **Typical two-column geometry** (AISTATS example):
  - Overall text width (two columns): **6.75"**
  - Each column width: **3.25"**
  - Column gap: **0.25"**

- **LaTeX figure placement**:
  - **Single-column figure**:

    ```latex
    \begin{figure}[t]
        \centering
        \includegraphics[width=\columnwidth]{figures/myplot.pdf}
        \caption{Single-column figure caption.}
        \label{fig:single}
    \end{figure}
    ```

  - **Two-column (wide) figure**:

    ```latex
    \begin{figure*}[t]
        \centering
        \includegraphics[width=\textwidth]{figures/mywideplot.pdf}
        \caption{Two-column figure caption.}
        \label{fig:wide}
    \end{figure*}
    ```

- **Matching `figsize` in Python**:
  - For a **single-column** figure in a two-column paper:

    ```python
    import matplotlib.pyplot as plt
    import minimalist

    # 3.25 inches wide column, keep square by default
    fig, ax = plt.subplots(figsize=(3.25, 3.25))
    minimalist.use_style('white')
    ```

  - For a **two-column wide** figure:

    ```python
    import matplotlib.pyplot as plt
    import minimalist

    # 6.75 inches text width, choose a suitable aspect ratio (e.g. 1/2 height)
    fig_width = 6.75
    fig_height = fig_width * 0.5
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))
    minimalist.use_style('white')
    ```

- **Using `figsize()` with conference layouts**:
  - If you want to stay in terms of the internal `TEXT_WIDTH` while targeting a 6.75" two-column width, you can scale by the ratio
    \( r = 6.75 / 7.06 \approx 0.96 \):

    ```python
    # Two-column wide figure using internal TEXT_WIDTH scaling
    width_fraction = 6.75 / 7.06  # ≈ 0.96
    fig = plt.figure(figsize=minimalist.figsize(width_fraction, aspect_ratio=0.5))
    ```

This keeps the **visual style and line weights consistent** while letting you precisely control how figures fit into single-column or two-column slots defined by the conference template.

---

### Axes & Ticks

- **Spines**:
  - All four spines are visible: top, right, bottom, left.
  - Line width: **0.65**
  - Facecolor: **none** (transparent), so the figure-level white shows through.

- **Ticks**:
  - Directions: **inward** (`xtick.direction: in`, `ytick.direction: in`)
  - Majors only: minor ticks are hidden.
  - Size and width: small, thin ticks (major size ≈ 1.5, width ≈ 0.35).
  - Tick and label colors: **black**
  - Tick label sizes: **8 pt** (matching body text).

This yields a boxed, scientific look reminiscent of journal figures, but with restrained, modern styling.

---

### Color System

#### Qualitative Palette (`BASE_COLORS`)

A custom 6-color palette used for line and scatter plots (the default `axes.prop_cycle`):

- `#AB3019` – deep red / brick
- `#FE7002` – vivid orange
- `#F4B43E` – warm golden yellow
- `#86B4C4` – soft teal-blue
- `#00768C` – strong cyan-teal
- `#003547` – very dark blue-green

**Design intent**:

- **Warm-to-cool progression** for series ordering (red → orange → yellow → teal → cyan → dark teal).
- **High contrast** between adjacent colors but without neon or overly saturated tones.
- Works well for:
  - Multi-series line plots
  - Grouped scatter plots
  - Legends with up to ~6 groups

#### Continuous Colormaps

- **Diverging**: `pride` (from `scicomap`), recommended for signed data and deviations around a central value.
- **Sequential**: `inferno`, a perceptually uniform colormap for densities, intensities, and strictly positive quantities.
- **Custom continuous**: `minimalist` (and `minimalist_r`) created by interpolating through `BASE_COLORS`:
  - Ensures heatmaps and other continuous fields feel visually connected to line/scatter colors.
  - Gives a coherent visual identity across all plot types.

`image.cmap` is set to `pride` by default in the style file.

---

### Legends & Utilities

- **Legends**:
  - Frameless (`legend.frameon: False`)
  - Compact spacing and small fonts tuned for multi-series plots.
  - Recommended to color labels to match line colors via:

    ```python
    ax.plot(x, y1, label="Line 1")
    ax.plot(x, y2, label="Line 2")
    ax.legend(labelcolor="linecolor")  # legend text matches line colors
    ```

- **Legend text coloring utility (alternative)**:
  - `minimalist.color_legend_text(ax)` can be used if you already have a legend:

    ```python
    ax.plot(x, y1, label="Line 1")
    ax.plot(x, y2, label="Line 2")
    ax.legend()
    minimalist.color_legend_text(ax)
    ```
  - Both approaches color legend labels to match their corresponding line/marker colors and reduce the need for heavy legend markers.

- **Clipping control**:
  - Utility: `remove_all_clipping(fig)` removes clipping from all artists so elements can extend slightly beyond axes (useful for stylistic choices or custom annotations).

---

### Usage Summary

- **Activate style**:

  ```python
  import minimalist
  import matplotlib.pyplot as plt

  minimalist.use_style('white')

  # For a black background instead:
  minimalist.use_style('black')
  ```

- **Figure sizing**:

  ```python
  fig, ax = plt.subplots(figsize=minimalist.figsize(0.5))  # half text width, square
  ```

- **Colormaps**:

  ```python
  cmap_div = minimalist.get_cmap('diverging')    # 'pride'
  cmap_seq = minimalist.get_cmap('sequential')   # 'inferno'
  colors = minimalist.get_cmap('qualitative')    # BASE_COLORS list
  ```


---

### Conceptual Summary

The Minimalist white and black styles are built to:

- Produce **square, LaTeX-compatible, high-resolution** figures by default.
- Use a **coherent warm–cool custom palette** across categorical and continuous data.
- Combine **sans-serif text** with **CM math** for a contemporary but scholarly feel.
