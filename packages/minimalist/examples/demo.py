"""
Demo script for the minimalist matplotlib style package
Base style: Default for everyday use
Science style: For publications only
"""

import numpy as np
import matplotlib.pyplot as plt
import minimalist

# Create plots directory
import os
os.makedirs('plots', exist_ok=True)

# Example 1: Base style (default) with Greek letters
minimalist.use_style('base')

x = np.linspace(0, 2*np.pi, 100)
fig, ax = plt.subplots()
for i in range(5):
    ax.plot(x, np.sin(x + i*np.pi/5), label=r'$\sin(x + %d\pi/5)$' % i)
ax.set_xlabel(r'$x$ [radians]')
ax.set_ylabel(r'$\alpha$')
ax.legend()
ax.set_title('Base Style (Default) with Greek Letters')
plt.savefig('plots/base_default.pdf')
plt.show()

# Example 2: Base style with RdBuBl colors (9 lines)
minimalist.use_style(['base', 'rdbubl'])

fig, ax = plt.subplots()
for i in range(9):
    ax.plot(x, np.sin(x + i*np.pi/9), label=r'$\sin(x + %d\pi/9)$' % i)
ax.set_xlabel(r'$\theta$ [radians]')
ax.set_ylabel(r'$\phi(\theta)$')
ax.legend(ncol=3, fontsize=9)
ax.set_title('Base Style with RdBuBl Colors (9 lines)')
plt.savefig('plots/base_rdbubl.pdf')
plt.show()

# Example 3: Smooth heatmap
from matplotlib.colors import LinearSegmentedColormap

# Create smooth heatmap data
x_grid = np.linspace(-3, 3, 50)
y_grid = np.linspace(-3, 3, 50)
X, Y = np.meshgrid(x_grid, y_grid)
data = np.sin(X) * np.cos(Y)

# Get colormap
rdbu_w_colors = minimalist.get_palette('Rdbu_w')
rdbu_w_cmap = LinearSegmentedColormap.from_list('rdbu_w', rdbu_w_colors)

fig, ax = plt.subplots()
im = ax.imshow(data, cmap=rdbu_w_cmap, aspect='auto', interpolation='bilinear')
plt.colorbar(im)
ax.set_title('Smooth Heatmap with Rdbu_w Colormap')
ax.set_xticks([])
ax.set_yticks([])
plt.savefig('plots/heatmap_rdbu_w.pdf')
plt.show()

# Example 4: Science style for publications only
minimalist.use_style('science')
fig, ax = plt.subplots()
for i in range(5):
    ax.plot(x, np.cos(x + i*np.pi/5), label=r'$\cos(x + %d\pi/5)$' % i)
ax.set_xlabel(r'$x$ [radians]')
ax.set_ylabel(r'$\beta$')
ax.legend()
ax.set_title('Science Style (Publications)')
plt.savefig('plots/science_publication.pdf')
plt.show()

print("\nAll plots saved to 'plots/' directory")
print("\nColor palettes available:")
colors = minimalist.get_palette('RdBuYe_q')
print(f"RdBuYe_q colors: {colors}")
print("\nStyle Usage:")
print("- Base: Default style for everyday use (no LaTeX, mathtext for Greek letters)")
print("- Science: For publications only (full LaTeX support)") 