"""
Demo script for the minimalist matplotlib style package
Base style: Minimal style without tick marks
Science style: Clean scientific style with tick marks
"""

import numpy as np
import matplotlib.pyplot as plt
import minimalist

# Create plots directory
import os
os.makedirs('plots', exist_ok=True)

# Example 1: Science style with line plots
minimalist.use_style('science')

x = np.linspace(0, 2*np.pi, 100)
fig, ax = plt.subplots(figsize=(minimalist.FW_2, minimalist.FW_3))
for i in range(6):
    ax.plot(x, np.sin(x + i*np.pi/6), label=f'Phase {i}')
ax.set_xlabel(r'$x$ [radians]')
ax.set_ylabel(r'$\sin(x)$')
ax.legend()
plt.savefig('plots/science_style.pdf')
plt.show()

# Example 2: Base style (minimal, no ticks)
minimalist.use_style('base')

fig, ax = plt.subplots(figsize=(minimalist.FW_2, minimalist.FW_3))
for i in range(6):
    ax.plot(x, np.cos(x + i*np.pi/6), label=f'Phase {i}')
ax.set_xlabel(r'$\theta$ [radians]')
ax.set_ylabel(r'$\cos(\theta)$')
ax.legend()
plt.savefig('plots/base_style.pdf')
plt.show()

# Example 3: Heatmap with continuous colormap
minimalist.use_style('science')

x_grid = np.linspace(-3, 3, 50)
y_grid = np.linspace(-3, 3, 50)
X, Y = np.meshgrid(x_grid, y_grid)
data = np.sin(X) * np.cos(Y)

fig, ax = plt.subplots(figsize=(minimalist.FW_2, minimalist.FW_2))
im = ax.imshow(data, cmap='minimalist', aspect='auto', interpolation='bilinear')
plt.colorbar(im)
ax.set_title('Heatmap with Minimalist Colormap')
ax.set_xticks([])
ax.set_yticks([])
plt.savefig('plots/heatmap_minimalist.pdf')
plt.show()

print("\nAll plots saved to 'plots/' directory")
print(f"\nFigure widths: FW={minimalist.FW:.2f}, FW_2={minimalist.FW_2:.2f}, FW_3={minimalist.FW_3:.2f}")
print(f"Base colors: {minimalist.BASE_COLORS}")
print("\nUsage:")
print("  minimalist.use_style('science')  # With tick marks")
print("  minimalist.use_style('base')     # Minimal, no ticks")
print("  cmap='minimalist'                # Continuous colormap for heatmaps")