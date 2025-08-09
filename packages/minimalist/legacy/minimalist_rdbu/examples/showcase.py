# %%
"""
Showcase of minimalist_rdbu style capabilities with CMU Sans Serif font.
"""
import numpy as np
import matplotlib.pyplot as plt
import minimalist_rdbu
from matplotlib.gridspec import GridSpec
from matplotlib.ticker import AutoMinorLocator

print("Starting showcase example...")

# Apply the style
print("Style applied successfully")

# Create figure with custom layout
fig = plt.figure(figsize=(12, 8))
gs = GridSpec(2, 3, figure=fig)

print("Creating plots...")

# Generate data
np.random.seed(42)
x = np.linspace(0, 10, 100)
y1 = np.sin(x) + 0.1 * np.random.randn(100)
y2 = np.cos(x) + 0.1 * np.random.randn(100)

# 1. Line plot with error bands
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(x, y1, label=r'$\sin(x)$')
ax1.fill_between(x, y1-0.2, y1+0.2, alpha=0.2)
ax1.plot(x, y2, label=r'$\cos(x)$')
ax1.fill_between(x, y2-0.2, y2+0.2, alpha=0.2)
ax1.set_xlabel(r'Time $t$ (s)')
ax1.set_ylabel(r'Amplitude $A$')
ax1.legend(title=r'$f(x)$')
ax1.xaxis.set_minor_locator(AutoMinorLocator())
ax1.yaxis.set_minor_locator(AutoMinorLocator())

# 2. Scatter plot
ax2 = fig.add_subplot(gs[0, 1])
sizes = np.random.uniform(20, 200, 30)
ax2.scatter(np.random.normal(0, 1, 30),
           np.random.normal(0, 1, 30),
           s=sizes, alpha=0.6, label=r'$\mu=0$')
ax2.scatter(np.random.normal(2, 1, 30),
           np.random.normal(2, 1, 30),
           s=sizes, alpha=0.6, label=r'$\mu=2$')
ax2.set_xlabel(r'$X_1$')
ax2.set_ylabel(r'$X_2$')
ax2.legend(title=r'Groups')
ax2.xaxis.set_minor_locator(AutoMinorLocator())
ax2.yaxis.set_minor_locator(AutoMinorLocator())

# 3. Box and violin plot combined
ax3 = fig.add_subplot(gs[0, 2])
data = [np.random.normal(i, 0.5, 100) for i in range(4)]
vp = ax3.violinplot(data, positions=range(4))
for pc in vp['bodies']:
    pc.set_alpha(0.3)
bp = ax3.boxplot(data, positions=range(4), widths=0.3,
                 showfliers=False, patch_artist=True)
for patch in bp['boxes']:
    patch.set_alpha(0.7)
ax3.set_xticks(range(4))
ax3.set_xticklabels([r'$\alpha$', r'$\beta$', r'$\gamma$', r'$\delta$'])
ax3.set_xlabel('Parameters')
ax3.set_ylabel(r'Value $\nu$')
ax3.yaxis.set_minor_locator(AutoMinorLocator())

# 4. Histogram
ax4 = fig.add_subplot(gs[1, 0])
data1 = np.random.normal(0, 1, 1000)
data2 = np.random.normal(2, 1.5, 1000)
ax4.hist([data1, data2], bins=30, density=True, alpha=0.7,
         label=[r'$\mathcal{N}(0,1)$', r'$\mathcal{N}(2,1.5)$'])
ax4.set_xlabel(r'$x$')
ax4.set_ylabel(r'Density $\rho(x)$')
ax4.legend()
ax4.xaxis.set_minor_locator(AutoMinorLocator())
ax4.yaxis.set_minor_locator(AutoMinorLocator())

# 5. Heatmap
ax5 = fig.add_subplot(gs[1, 1])
data = np.random.randn(10, 10)
im = ax5.imshow(data, cmap='RdBu_r', aspect='auto')
cbar = plt.colorbar(im, ax=ax5, label=r'$z$-score')
ax5.set_xlabel(r'Position $\xi$')
ax5.set_ylabel(r'Time $\tau$')
# Add minor ticks to colorbar
cbar.ax.yaxis.set_minor_locator(AutoMinorLocator())

# 6. Error bars
ax6 = fig.add_subplot(gs[1, 2])
x = np.arange(5)
y = np.exp(-x/2)
yerr = 0.1 + 0.2*np.random.random(5)
ax6.errorbar(x, y, yerr=yerr, fmt='o', capsize=3,
             label=r'Data $\pm\sigma$')
ax6.plot(x, y, '--', alpha=0.5, label=r'$y=e^{-x/2}$')
ax6.set_xlabel(r'$x$')
ax6.set_ylabel(r'$y$')
ax6.legend()
ax6.xaxis.set_minor_locator(AutoMinorLocator())
ax6.yaxis.set_minor_locator(AutoMinorLocator())

# Add a title to the figure
fig.suptitle('Minimalist RdBu Style Showcase', y=1.02)

# Adjust layout
plt.tight_layout()

# Save the figure
print("Saving figure...")
plt.savefig('minimalist_rdbu_showcase.pdf', bbox_inches='tight')
print("Figure saved as 'minimalist_rdbu_showcase.pdf'") 
# %%
