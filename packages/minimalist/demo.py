"""
Minimalist Package Demo

Demonstrates the Science style for:
1. Line plots (with negative values)
2. Log scale plots
3. Heatmaps
4. Scatter plots

Uses CMU Sans Serif font with Computer Modern math.
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import minimalist

# Create plots directory
os.makedirs('plots', exist_ok=True)

print(f"Minimalist v{minimalist.__version__}")
print(f"BASE_COLORS: {minimalist.BASE_COLORS}")
print()

# Apply style once
minimalist.use_style('science')

# =============================================================================
# Demo 1: Line Plots with Negative Values
# =============================================================================
print("Demo 1: Line plots with negative values...")

fig, ax = plt.subplots(figsize=(minimalist.FW_2, minimalist.FW_3))

x = np.linspace(-2, 2, 100)
for i in range(4):
    ax.plot(x, np.sin(2*x + i*np.pi/4), label=rf'$\phi = {i}\pi/4$')
ax.set_xlabel(r'Position $x$')
ax.set_ylabel(r'$\sin(2x + \phi)$')
ax.legend(fontsize=6, ncol=2)

plt.tight_layout()
plt.savefig('plots/demo_line.pdf')
print("  Saved: plots/demo_line.pdf")
plt.show()


# =============================================================================
# Demo 2: Log Scale Plots
# =============================================================================
print("Demo 2: Log scale plots...")

fig, ax = plt.subplots(figsize=(minimalist.FW_2, minimalist.FW_3))

x = np.logspace(-1, 2, 100)
for i in range(4):
    ax.loglog(x, x**(-(i+1)/2), label=rf'$x^{{-{i+1}/2}}$')
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$f(x)$')
ax.legend(fontsize=6)
ax.xaxis.set_major_formatter(ScalarFormatter())
ax.yaxis.set_major_formatter(ScalarFormatter())

plt.tight_layout()
plt.savefig('plots/demo_logscale.pdf')
print("  Saved: plots/demo_logscale.pdf")
plt.show()


# =============================================================================
# Demo 3: Heatmaps
# =============================================================================
print("Demo 3: Heatmaps...")

fig, ax = plt.subplots(figsize=(minimalist.FW_2, minimalist.FW_3))

x_grid = np.linspace(-3, 3, 100)
y_grid = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x_grid, y_grid)
data = np.sin(X) * np.cos(Y)

im = ax.imshow(data, aspect='auto', interpolation='bilinear',
               extent=[-3, 3, -3, 3])
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')
plt.colorbar(im, ax=ax, shrink=0.8)

plt.tight_layout()
plt.savefig('plots/demo_heatmap.pdf')
print("  Saved: plots/demo_heatmap.pdf")
plt.show()


# =============================================================================
# Demo 4: Scatter Plots
# =============================================================================
print("Demo 4: Scatter plots...")

fig, ax = plt.subplots(figsize=(minimalist.FW_2, minimalist.FW_3))

np.random.seed(42)
for i, color in enumerate(minimalist.BASE_COLORS):
    x = np.random.randn(20) + i * 1.5 - 3
    y = np.random.randn(20) + i * 0.5
    ax.scatter(x, y, c=color, s=15, label=f'$G_{i+1}$')
ax.set_xlabel(r'$\alpha$ [units]')
ax.set_ylabel(r'$\beta$ [units]')
ax.legend(fontsize=5, ncol=3)

plt.tight_layout()
plt.savefig('plots/demo_scatter.pdf')
print("  Saved: plots/demo_scatter.pdf")
plt.show()


# =============================================================================
# Summary
# =============================================================================
print()
print("=" * 50)
print("Demo complete!")
print("=" * 50)
print()
print("Generated files in plots/:")
print("  - demo_line.pdf     : Line plots with negative values")
print("  - demo_logscale.pdf : Log scale plots")
print("  - demo_heatmap.pdf  : Heatmaps")
print("  - demo_scatter.pdf  : Scatter plots")
print()
print("Usage:")
print("  import minimalist")
print("  minimalist.use_style('science')")
