# Minimalist

A minimalist matplotlib style package for scientific presentations and publications with custom color palettes.

## Installation

```bash
pip install -e packages/minimalist
```

## Usage

### Base Style (everyday use)
```python
import minimalist
minimalist.use_style('base')
```
- CMU Sans Serif is the default font
- No LaTeX; MathText supports Greek letters
- Minus sign warnings suppressed via `axes.unicode_minus: False`

### Science Style (publications)
```python
import minimalist
minimalist.use_style('science')
```
- Enables LaTeX with preamble: `amsmath`, `amssymb`
- Auto-detects TeX on macOS (e.g., `/Library/TeX/texbin`)
- Uses CMU Sans Serif

### Combine with Color Palettes
```python
minimalist.use_style(['base', 'rdbuye'])   # 5 colors
minimalist.use_style(['base', 'rdbubl'])   # 9 colors
minimalist.use_style(['science', 'rdbuye'])
```

## Color Palettes
- Diverging: `RdBuYe`, `RdBuYe_r`, `Rdbu_bl`, `Rdbu_bl_r`, `Rdbu_w`, `Rdbu_w_r`
- Sequential: `Rd`, `Rd_r`, `Bu`, `Bu_r`
- Qualitative: `RdBuBl_q`, `RdBuYe_q`

## Examples
See `packages/minimalist/examples/` for demos.

## Requirements
- Python >= 3.8
- matplotlib >= 3.5.0
- numpy >= 1.20.0

## License
MIT License - see LICENSE file for details.
