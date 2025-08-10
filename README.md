## Plot Styles Monorepo

This repository is a monorepo containing three Matplotlib style packages:

- `packages/minimalist`: A minimalist Matplotlib style with base and science variants plus curated color palettes.
- `packages/minimalist/legacy/minimalist_rdbu`: Older minimalist RdBu variant preserved as a legacy subpackage.
- `packages/scienceplots`: Third-party SciencePlots package vendored for convenience.

### Quick Start (development install)

From the repo root, install any package in editable mode:

```bash
pip install -e packages/minimalist
# Legacy package (optional)
pip install -e packages/minimalist/legacy/minimalist_rdbu
pip install -e packages/scienceplots
```

### What's configured by default
- CMU Sans Serif is the default font for both base and science styles (no manual font setup needed)
- Science style enables LaTeX and will auto-detect a TeX installation on macOS (e.g., `/Library/TeX/texbin`)
- Base style uses MathText (no LaTeX) for Greek letters
- Minus sign warnings are suppressed via `axes.unicode_minus: False`

### Usage

- Minimalist (everyday plots, no LaTeX):
```python
import matplotlib.pyplot as plt
import minimalist

minimalist.use_style('base')
plt.plot([1,2,3],[1,4,9])
plt.show()
```

- Minimalist (publication style with LaTeX):
```python
import minimalist
minimalist.use_style('science')
```

- Minimalist with RdBu color cycles:
```python
import minimalist
minimalist.use_style(['base', 'rdbuye'])   # 5-color cycle
minimalist.use_style(['base', 'rdbubl'])   # 9-color cycle
```

- SciencePlots (vendored example set):
```python
import matplotlib.pyplot as plt
import scienceplots
plt.style.use('science')
```

### Repository Layout

```
packages/
  minimalist/
  minimalist_rdbu/
  scienceplots/
```

Each package is a standalone Python distribution with its own README and setup metadata.
