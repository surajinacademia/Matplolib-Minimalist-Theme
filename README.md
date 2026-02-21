## Plot Styles Monorepo

This repository contains Matplotlib style packages:

- `packages/minimalist`: A minimalist Matplotlib style for scientific figures with curated color palettes.
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
- CMU Sans Serif font with Computer Modern math (no LaTeX required)
- Transparent figure/axes backgrounds for easy embedding
- Explicit black text, labels, ticks, and edges
- Thin lines (0.5pt), small markers, capsize 1.0
- Minus sign warnings suppressed via `axes.unicode_minus: False`

### Usage

```python
import matplotlib.pyplot as plt
import minimalist

minimalist.use_style('science')

fig, ax = plt.subplots(figsize=(minimalist.FW_2, minimalist.FW_3))
ax.plot([1, 2, 3], [1, 4, 9])
plt.show()
```

### Figure Width Constants

| Constant | Value | Description |
|----------|-------|-------------|
| `FW` | 7.06" | Full text width |
| `FW_2` | 3.53" | Half width |
| `FW_3` | 2.36" | Third width |
| `FW_4` | 1.77" | Quarter width |

### Repository Layout

```
packages/
  minimalist/
  minimalist_rdbu/
  scienceplots/
```

Each package is a standalone Python distribution with its own README and setup metadata.
