#!/usr/bin/env python3
"""
Minimalist Package Demo

This script demonstrates the two styles available in the minimalist package:
- science: Clean scientific style with tick marks
- base: Minimal style without tick marks

Both styles use CMU Sans Serif font with DejaVu Sans for mathtext.
"""

import os
import warnings
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LogFormatterSciNotation, ScalarFormatter
import minimalist

# Suppress the font glyph warnings
warnings.filterwarnings('ignore', message='.*Glyph.*missing.*')
warnings.filterwarnings('ignore', message='.*does not have a glyph.*')

# Create plots directory
os.makedirs('plots', exist_ok=True)

print(f"Minimalist v{minimalist.__version__}")
print(f"Figure widths: FW={minimalist.FW:.2f}, FW_2={minimalist.FW_2:.2f}, FW_3={minimalist.FW_3:.2f}")
print(f"Base colors: {minimalist.BASE_COLORS}")
print()

# =============================================================================
# Demo 1: Science Style - Line Plots
# =============================================================================
print("Demo 1: Science style with line plots...")

minimalist.use_style('science')

fig, ax = plt.subplots(figsize=(minimalist.FW_2, minimalist.FW_3))

# Phase field / level set interface profiles
N = 200
delta = 0.6
X = np.linspace(-1, 1, N)

ax.plot(X, (1 - np.tanh(4 * X / delta)) / 2, label=r'$\phi_1$')
ax.plot(X, (1.4 + np.tanh(4 * X / delta)) / 4, label=r'$\phi_2$')
ax.plot(X, 0.3 * np.exp(-X**2 / 0.2), label=r'$\phi_3$')
ax.axhline(y=0.5, color='k', linestyle='--', linewidth=0.5, label='Reference')

ax.set_xlabel(r'Position $x$')
ax.set_ylabel(r'Phase field $\phi$')
ax.set_title('Science Style')
ax.legend(loc='upper right')

plt.tight_layout()
plt.savefig('plots/demo_science.pdf')
print("  Saved: plots/demo_science.pdf")
plt.close()


# =============================================================================
# Demo 2: Base Style - Line Plots
# =============================================================================
print("Demo 2: Base style with line plots...")

minimalist.use_style('base')

fig, ax = plt.subplots(figsize=(minimalist.FW_2, minimalist.FW_3))

# Same data, different style
ax.plot(X, (1 - np.tanh(4 * X / delta)) / 2, label=r'$\phi_1$')
ax.plot(X, (1.4 + np.tanh(4 * X / delta)) / 4, label=r'$\phi_2$')
ax.plot(X, 0.3 * np.exp(-X**2 / 0.2), label=r'$\phi_3$')
ax.axhline(y=0.5, color='k', linestyle='--', linewidth=0.5, label='Reference')

ax.set_xlabel(r'Position $x$')
ax.set_ylabel(r'Phase field $\phi$')
ax.set_title('Base Style (no ticks)')
ax.legend(loc='upper right')

plt.tight_layout()
plt.savefig('plots/demo_base.pdf')
print("  Saved: plots/demo_base.pdf")
plt.close()


# =============================================================================
# Demo 3: Color Palette - All 6 Colors
# =============================================================================
print("Demo 3: All 6 colors from BASE_COLORS...")

minimalist.use_style('science')

fig, ax = plt.subplots(figsize=(minimalist.FW_2, minimalist.FW_3))

x = np.linspace(0, 2*np.pi, 100)
for i in range(6):
    y = np.sin(x + i * np.pi / 6)
    ax.plot(x, y, label=rf'$\phi = {i}\pi/6$')

ax.set_xlabel(r'$x$ [radians]')
ax.set_ylabel(r'$\sin(x + \phi)$')
ax.set_title('Color Palette (6 colors)')
ax.legend(loc='upper right', ncol=2, fontsize=6)

plt.tight_layout()
plt.savefig('plots/demo_colors.pdf')
print("  Saved: plots/demo_colors.pdf")
plt.close()


# =============================================================================
# Demo 4: Heatmap with Continuous Colormap
# =============================================================================
print("Demo 4: Heatmap with 'minimalist' colormap...")

minimalist.use_style('science')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(minimalist.FW_2 * 2, minimalist.FW_3))

# Generate smooth data
x_grid = np.linspace(-3, 3, 100)
y_grid = np.linspace(-3, 3, 100)
X_grid, Y_grid = np.meshgrid(x_grid, y_grid)
data = np.sin(X_grid) * np.cos(Y_grid)

# Left: minimalist colormap
im1 = ax1.imshow(data, cmap='minimalist', aspect='auto', interpolation='bilinear')
ax1.set_title("cmap='minimalist'")
ax1.set_xticks([])
ax1.set_yticks([])
plt.colorbar(im1, ax=ax1, shrink=0.8)

# Right: reversed colormap
im2 = ax2.imshow(data, cmap='minimalist_r', aspect='auto', interpolation='bilinear')
ax2.set_title("cmap='minimalist_r'")
ax2.set_xticks([])
ax2.set_yticks([])
plt.colorbar(im2, ax=ax2, shrink=0.8)

plt.tight_layout()
plt.savefig('plots/demo_heatmap.pdf')
print("  Saved: plots/demo_heatmap.pdf")
plt.close()


# =============================================================================
# Demo 5: Math Notation (without TeX)
# =============================================================================
print("Demo 5: Math notation using mathtext (no TeX)...")

minimalist.use_style('science')

fig, ax = plt.subplots(figsize=(minimalist.FW_2, minimalist.FW_3))

# Mathematical functions
x = np.linspace(-2, 2, 200)
ax.plot(x, np.exp(-x**2), label=r'$e^{-x^2}$')
ax.plot(x, np.tanh(x), label=r'$\tanh(x)$')
ax.plot(x, x**2 / 4 - 0.5, label=r'$\frac{x^2}{4} - \frac{1}{2}$')

# Add equation text
ax.text(0.05, 0.95, r'$\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}$',
        transform=ax.transAxes, fontsize=10, verticalalignment='top')

ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$f(x)$')
ax.set_title('Math Notation (mathtext)')
ax.legend(loc='lower right')

plt.tight_layout()
plt.savefig('plots/demo_math.pdf')
print("  Saved: plots/demo_math.pdf")
plt.close()


# =============================================================================
# Demo 6: Log Scale
# =============================================================================
print("Demo 6: Log scale plots...")

minimalist.use_style('science')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(minimalist.FW, minimalist.FW_3))

# Left: semi-log y
x = np.linspace(0, 5, 100)
for i in range(4):
    ax1.semilogy(x, np.exp(-(i+1)*x), label=rf'$e^{{-{i+1}x}}$')
ax1.set_xlabel(r'$x$')
ax1.set_ylabel(r'$y$')
ax1.set_title('Semilogy')
ax1.legend(fontsize=6)

# Right: log-log
x = np.logspace(-1, 2, 100)
for i in range(4):
    ax2.loglog(x, x**(-(i+1)/2), label=rf'$x^{{-{i+1}/2}}$')
ax2.set_xlabel(r'$x$')
ax2.set_ylabel(r'$y$')
ax2.set_title('Log-log')
ax2.legend(fontsize=6)

plt.tight_layout()
plt.savefig('plots/demo_logscale.pdf')
print("  Saved: plots/demo_logscale.pdf")
plt.close()


# =============================================================================
# Demo 7: Scatter Plot
# =============================================================================
print("Demo 7: Scatter plot...")

minimalist.use_style('science')

fig, ax = plt.subplots(figsize=(minimalist.FW_2, minimalist.FW_3))

np.random.seed(42)
for i, color in enumerate(minimalist.BASE_COLORS):
    x = np.random.randn(15) + i * 1.5
    y = np.random.randn(15) + i * 0.5
    ax.scatter(x, y, c=color, s=20, label=f'Group {i+1}')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Scatter Plot')
ax.legend(loc='upper left', fontsize=6, ncol=2)

plt.tight_layout()
plt.savefig('plots/demo_scatter.pdf')
print("  Saved: plots/demo_scatter.pdf")
plt.close()


# =============================================================================
# Demo 8: Side-by-Side Style Comparison
# =============================================================================
print("Demo 8: Side-by-side style comparison...")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(minimalist.FW, minimalist.FW_3))

x = np.linspace(0, 2*np.pi, 100)

# Science style (left)
minimalist.use_style('science')
for i in range(3):
    ax1.plot(x, np.sin(x + i*np.pi/3))
ax1.set_xlabel(r'$x$')
ax1.set_ylabel(r'$\sin(x)$')
ax1.set_title('Science')

# Base style (right) - manually hide ticks
for i in range(3):
    ax2.plot(x, np.cos(x + i*np.pi/3))
ax2.set_xlabel(r'$x$')
ax2.set_ylabel(r'$\cos(x)$')
ax2.set_title('Base')
ax2.tick_params(axis='both', which='major', length=0)

plt.tight_layout()
plt.savefig('plots/demo_comparison.pdf')
print("  Saved: plots/demo_comparison.pdf")
plt.close()


# =============================================================================
# Summary
# =============================================================================
print()
print("=" * 60)
print("Demo complete!")
print("=" * 60)
print()
print("Generated files in plots/:")
print("  - demo_science.pdf    : Science style")
print("  - demo_base.pdf       : Base style (no ticks)")
print("  - demo_colors.pdf     : All 6 colors")
print("  - demo_heatmap.pdf    : Continuous colormap")
print("  - demo_math.pdf       : Math notation")
print("  - demo_logscale.pdf   : Log scale plots")
print("  - demo_scatter.pdf    : Scatter plot")
print("  - demo_comparison.pdf : Style comparison")
print()
print("Usage:")
print("  import minimalist")
print("  minimalist.use_style('science')  # or 'base'")
print("  fig, ax = plt.subplots(figsize=(minimalist.FW_2, minimalist.FW_3))")
