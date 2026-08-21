"""
Minimalist Package Demo

Demonstrates the white style for:
1. 6-Series Line Plot
2. Heatmap
3. Scatter plot

Uses CMU Sans Serif font with Computer Modern math and unified custom color cycles.
"""

import os
import numpy as np
import matplotlib.pyplot as plt

import minimalist

# Create assets directory
os.makedirs('assets', exist_ok=True)

# Apply style once globally
minimalist.use_style('white')

# =============================================================================
# Unified Demo Figure (3-Panel)
# =============================================================================
print("Generating unified 3-panel demo figure...")

# Create one large figure with 3 subplots in a row.
# Use the helper to keep sizing tied to TEXT_WIDTH with a 1:3 aspect.
fig, axes = plt.subplots(1, 3, figsize=minimalist.figsize(width_fraction=1.0, aspect_ratio=1/3))

# -----------------------------------------------------------------------------
# Panel 1: Line Plots with Error Fills
# -----------------------------------------------------------------------------
ax = axes[0]
rng = np.random.default_rng(3)
v = np.arange(0, 11, dtype=float)
e = lambda: 0.6*v + 0.5
# Use the documented qualitative palette for line/scatter colors
colors = minimalist.get_cmap('qualitative')
series = [
    (0.5*1*v**2 + rng.normal(0, 0.8*v+0.5, 11), e(), colors[0], r"$1.0$"),
    (0.5*2*v**2 + rng.normal(0, 0.8*v+0.5, 11), e(), colors[1], r"$2.0$"),
    (0.5*3*v**2 + rng.normal(0, 0.8*v+0.5, 11), e(), colors[2], r"$3.0$"),
    (0.5*4*v**2 + rng.normal(0, 0.8*v+0.5, 11), e(), colors[3], r"$4.0$"),
    (0.5*5*v**2 + rng.normal(0, 0.8*v+0.5, 11), e(), colors[4], r"$5.0$"),
    (0.5*6*v**2 + rng.normal(0, 0.8*v+0.5, 11), e(), colors[5], r"$6.0$"),
]

for y, err, col, lab in series:
    ax.errorbar(v, y, yerr=err, color=col, label=lab, linewidth=1.0)
    ax.scatter(v, y, s=8, edgecolor=col, facecolor=col, label=None)

ax.set_xlabel(r"Velocity $v$")
ax.set_ylabel(r"Energy $E_k$")
ax.set_title("Line Plot (Auto-Fill)")
ax.legend(title=r"Mass $m$", labelcolor="linecolor")

# -----------------------------------------------------------------------------
# Panel 2: Scatter Plot
# -----------------------------------------------------------------------------
ax = axes[1]
np.random.seed(42)
for i, color in enumerate(colors):
    x = np.random.randn(20) + i * 1.5 - 3
    y = np.random.randn(20) + i * 0.5
    ax.scatter(x, y, edgecolor=color, facecolor=color, linewidths=0.5, s=15, label=f'$G_{i+1}$')

ax.set_xlabel(r'$\alpha$')
ax.set_ylabel(r'$\beta$')
ax.set_title("Scatter Plot")
ax.legend(ncol=2, labelcolor="linecolor")

# -----------------------------------------------------------------------------
# Panel 3: Heatmap (Diverging 'Pride')
# -----------------------------------------------------------------------------
ax = axes[2]
cmap = minimalist.get_cmap('diverging')

x_grid = np.linspace(-3, 3, 100)
y_grid = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x_grid, y_grid)
data = np.sin(X) * np.cos(Y)

im = ax.imshow(data, cmap=cmap, aspect='auto', interpolation='bilinear', extent=[-3, 3, -3, 3])
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')
ax.set_title("Heatmap (Pride)")
plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)

plt.tight_layout()
plt.savefig('assets/demo_combined.png', dpi=300, bbox_inches='tight')
print("  Saved: assets/demo_combined.png")

# =============================================================================
print("=" * 50)
print("Demo complete! Combined figure generated in assets/.")
print("=" * 50)
