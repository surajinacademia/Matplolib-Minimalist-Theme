"""
Minimalist Package Demo

Compares Science vs Base styles side-by-side for:
1. Line plots (with negative values)
2. Log scale plots
3. Heatmaps
4. Scatter plots

All use CMU Sans Serif font with Computer Modern math.
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

# =============================================================================
# Demo 1: Line Plots with Negative Values
# =============================================================================
print("Demo 1: Line plots with negative values...")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(minimalist.FW, minimalist.FW_3))

x = np.linspace(-2, 2, 100)

# Science style (left)
minimalist.use_style('science')
for i in range(4):
    ax1.plot(x, np.sin(2*x + i*np.pi/4), label=rf'$\phi = {i}\pi/4$')
ax1.set_xlabel(r'Position $x$')
ax1.set_ylabel(r'$\sin(2x + \phi)$')
ax1.set_title('Science')
ax1.legend(fontsize=6, ncol=2)

# Base style (right)
minimalist.use_style('base')
for i in range(4):
    ax2.plot(x, np.cos(2*x + i*np.pi/4), label=rf'$\phi = {i}\pi/4$')
ax2.set_xlabel(r'Position $x$')
ax2.set_ylabel(r'$\cos(2x + \phi)$')
ax2.set_title('Base')
ax2.legend(fontsize=6, ncol=2)

plt.tight_layout()
plt.savefig('plots/demo_line.pdf')
print("  Saved: plots/demo_line.pdf")
plt.show()


# =============================================================================
# Demo 2: Log Scale Plots
# =============================================================================
print("Demo 2: Log scale plots...")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(minimalist.FW, minimalist.FW_3))

x = np.logspace(-1, 2, 100)

# Science style (left)
minimalist.use_style('science')
for i in range(4):
    ax1.loglog(x, x**(-(i+1)/2), label=rf'$x^{{-{i+1}/2}}$')
ax1.set_xlabel(r'$x$')
ax1.set_ylabel(r'$f(x)$')
ax1.set_title('Science (log-log)')
ax1.legend(fontsize=6)
ax1.xaxis.set_major_formatter(ScalarFormatter())
ax1.yaxis.set_major_formatter(ScalarFormatter())

# Base style (right)
minimalist.use_style('base')
for i in range(4):
    ax2.loglog(x, x**(-(i+1)/2), label=rf'$x^{{-{i+1}/2}}$')
ax2.set_xlabel(r'$x$')
ax2.set_ylabel(r'$f(x)$')  
ax2.set_title('Base (log-log)')
ax2.legend(fontsize=6)
ax2.xaxis.set_major_formatter(ScalarFormatter())
ax2.yaxis.set_major_formatter(ScalarFormatter())

plt.tight_layout()
plt.savefig('plots/demo_logscale.pdf')
print("  Saved: plots/demo_logscale.pdf")
plt.show()


# =============================================================================
# Demo 3: Heatmaps
# =============================================================================
print("Demo 3: Heatmaps...")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(minimalist.FW, minimalist.FW_3))

# Generate data
x_grid = np.linspace(-3, 3, 100)
y_grid = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x_grid, y_grid)
data = np.sin(X) * np.cos(Y)

# Science style (left)
minimalist.use_style('science')
im1 = ax1.imshow(data, aspect='auto', interpolation='bilinear', 
                  extent=[-3, 3, -3, 3])
ax1.set_xlabel(r'$x$')
ax1.set_ylabel(r'$y$')
ax1.set_title('Science')
plt.colorbar(im1, ax=ax1, shrink=0.8)

# Base style (right)
minimalist.use_style('base')
im2 = ax2.imshow(data, aspect='auto', interpolation='bilinear',
                  extent=[-3, 3, -3, 3])
ax2.set_xlabel(r'$x$')
ax2.set_ylabel(r'$y$')
ax2.set_title('Base')
plt.colorbar(im2, ax=ax2, shrink=0.8)

plt.tight_layout()
plt.savefig('plots/demo_heatmap.pdf')
print("  Saved: plots/demo_heatmap.pdf")
plt.show()


# =============================================================================
# Demo 4: Scatter Plots
# =============================================================================
print("Demo 4: Scatter plots...")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(minimalist.FW, minimalist.FW_3))

np.random.seed(42)

# Science style (left)
minimalist.use_style('science')
for i, color in enumerate(minimalist.BASE_COLORS):
    x = np.random.randn(20) + i * 1.5 - 3
    y = np.random.randn(20) + i * 0.5
    ax1.scatter(x, y, c=color, s=15, label=f'$G_{i+1}$')
ax1.set_xlabel(r'$\alpha$ [units]')
ax1.set_ylabel(r'$\beta$ [units]')
ax1.set_title('Science')
ax1.legend(fontsize=5, ncol=3)

# Base style (right)
minimalist.use_style('base')
for i, color in enumerate(minimalist.BASE_COLORS):
    x = np.random.randn(20) + i * 1.5 - 3
    y = np.random.randn(20) + i * 0.5
    ax2.scatter(x, y, c=color, s=15, label=f'$G_{i+1}$')
ax2.set_xlabel(r'$\alpha$ [units]')
ax2.set_ylabel(r'$\beta$ [units]')
ax2.set_title('Base')
ax2.legend(fontsize=5, ncol=3)

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
print("  minimalist.use_style('science')  # or 'base'")
