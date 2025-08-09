## Plot Styles Monorepo

This repository is a monorepo containing three Matplotlib style packages:

- `packages/minimalist`: A minimalist Matplotlib style with base and science variants plus curated color palettes.
- `packages/minimalist_rdbu`: A minimalist style tailored to the RdBu color scheme with CMU Sans Serif font option.
- `packages/scienceplots`: Third-party SciencePlots package vendored for convenience.

### Quick Start (development install)

From the repo root, install any package in editable mode:

```bash
pip install -e packages/minimalist
pip install -e packages/minimalist_rdbu
pip install -e packages/scienceplots
```

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
minimalist.use_style(['science', 'sans-serif'])
```

- Minimalist RdBu:
```python
import minimalist_rdbu
minimalist_rdbu.use_style('all')  # base + RdBu colors + CMU Sans Serif
```

- SciencePlots:
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
