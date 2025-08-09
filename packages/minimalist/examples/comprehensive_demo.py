"""
Comprehensive demo of the minimalist matplotlib style package
Creates a multi-page PDF with all color palettes and plot types
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.colors import LinearSegmentedColormap
import minimalist
import os

# Create plots directory
os.makedirs('plots', exist_ok=True)

# Set random seed for reproducibility
np.random.seed(42)

# Create PDF for all plots
pdf_filename = 'plots/minimalist_showcase.pdf'

with PdfPages(pdf_filename) as pdf:
    
    # Page 1: Science style (publications only)
    minimalist.use_style('science')
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    fig.suptitle('Science Style - For Publications Only', fontsize=14, y=0.95)
    
    x = np.linspace(0, 2*np.pi, 100)
    colors = minimalist.get_palette('RdBuYe_q')
    
    # Top subplot - sine waves
    for i, color in enumerate(colors):
        y = np.sin(x + i*np.pi/5)
        ax1.plot(x, y, color=color, linewidth=2, label=r'$\sin(x + %d\pi/5)$' % i)
    
    ax1.set_xlabel(r'$x$ [radians]')
    ax1.set_ylabel('Amplitude')
    ax1.set_title('Sine Waves with Phase Shifts', pad=10)
    ax1.legend(loc='upper right', fontsize=9)
    
    # Bottom subplot - exponential decay
    t = np.linspace(0, 5, 1000)
    for i, color in enumerate(colors):
        y = np.exp(-t/2) * np.cos(2*np.pi*t + i*np.pi/5)
        ax2.plot(t, y, color=color, linewidth=2, label=r'$\tau = %d$' % (i+1))
    
    ax2.set_xlabel('Time [s]')
    ax2.set_ylabel('Amplitude')
    ax2.set_title('Damped Oscillations', pad=10)
    ax2.legend(loc='upper right', fontsize=9)
    
    fig.text(0.02, 0.02, 'Features: LaTeX rendering, all spines visible, minor ticks', 
             fontsize=9, style='italic', bbox=dict(boxstyle="round,pad=0.3", facecolor="wheat", alpha=0.5))
    
    plt.tight_layout(rect=[0, 0.08, 1, 0.92])
    pdf.savefig(fig)
    plt.close()
    
    # Page 2: Base style (default for everyday use)
    minimalist.use_style('base')
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle('Base Style - Default for Everyday Use', fontsize=14, y=0.95)
    
    colors = minimalist.get_palette('RdBuBl_q')
    
    # Left subplot - mathematical functions (using 6 colors to avoid clutter)
    x = np.linspace(-1.5, 1.5, 100)
    functions = [
        (lambda x, i=i: x**(i+1) / (i+1), r'$x^{%d}$' % (i+1)) for i in range(4)
    ] + [
        (lambda x: np.exp(x/2), r'$e^{x/2}$'),
        (lambda x: np.tanh(2*x), r'$\tanh(2x)$')
    ]
    
    for i, (func, label) in enumerate(functions):
        y = func(x)
        ax1.plot(x, y, color=colors[i], linewidth=2, label=label)
    
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_title('Mathematical Functions', pad=10)
    ax1.legend(loc='upper left', fontsize=8, ncol=2)
    
    # Right subplot - Gaussian distributions with Greek letters
    x_gauss = np.linspace(-4, 4, 100)
    for i, color in enumerate(colors[:5]):  # Use only 5 colors to avoid clutter
        mu = i - 2
        sigma = 0.6 + i*0.1
        y = (1/(sigma*np.sqrt(2*np.pi))) * np.exp(-0.5*((x_gauss-mu)/sigma)**2)
        ax2.plot(x_gauss, y, color=color, linewidth=2, label=r'$\mu$=%.0f, $\sigma$=%.1f' % (mu, sigma))
    
    ax2.set_xlabel('x')
    ax2.set_ylabel('Probability Density')
    ax2.set_title('Gaussian Distributions', pad=10)
    ax2.legend(loc='upper right', fontsize=8)
    
    fig.text(0.02, 0.02, 'Features: No LaTeX, mathtext for Greek letters, only bottom/left spines', 
             fontsize=9, style='italic', bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue", alpha=0.5))
    
    plt.tight_layout(rect=[0, 0.08, 1, 0.92])
    pdf.savefig(fig)
    plt.close()
    
    # Page 3: Smooth heatmaps with diverging colormaps
    minimalist.use_style('base')
    
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    fig.suptitle('Smooth Heatmaps with Diverging Color Palettes', fontsize=14, y=0.95)
    
    # Generate smooth sample data
    x_heat = np.linspace(-3, 3, 50)
    y_heat = np.linspace(-3, 3, 50)
    X, Y = np.meshgrid(x_heat, y_heat)
    data = np.sin(X) * np.cos(Y) + 0.3 * np.sin(3*X) * np.cos(2*Y)
    
    diverging_palettes = [
        ('RdBuYe', 'Red-Blue-Yellow'),
        ('RdBuYe_r', 'Reversed'),
        ('Rdbu_bl', 'Black Center'),
        ('Rdbu_bl_r', 'Black Center Rev.'),
        ('Rdbu_w', 'White Center'),
        ('Rdbu_w_r', 'White Center Rev.')
    ]
    
    for idx, (palette_name, title) in enumerate(diverging_palettes):
        ax = axes[idx // 3, idx % 3]
        colors = minimalist.get_palette(palette_name)
        cmap = LinearSegmentedColormap.from_list(palette_name, colors)
        
        im = ax.imshow(data, cmap=cmap, aspect='auto', vmin=-2, vmax=2, interpolation='bilinear')
        ax.set_title(f'{title}', fontsize=10, pad=5)
        cbar = plt.colorbar(im, ax=ax, shrink=0.8)
        cbar.ax.tick_params(labelsize=8)
        ax.set_xticks([])
        ax.set_yticks([])
    
    fig.text(0.02, 0.02, 'Features: Smooth interpolated heatmaps for diverging data', 
             fontsize=9, style='italic', bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.5))
    
    plt.tight_layout(rect=[0, 0.08, 1, 0.92])
    pdf.savefig(fig)
    plt.close()
    
    # Page 4: Style comparison
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Style Comparison: Base vs Science', fontsize=14, y=0.95)
    
    x_comp = np.linspace(0, 2*np.pi, 100)
    y1 = np.sin(x_comp)
    y2 = np.cos(x_comp)
    
    # Base style (default)
    minimalist.use_style('base')
    ax = axes[0, 0]
    ax.plot(x_comp, y1, label=r'$\sin(x)$')
    ax.plot(x_comp, y2, label=r'$\cos(x)$')
    ax.set_xlabel(r'$x$ [radians]')
    ax.set_ylabel(r'$f(x)$')
    ax.set_title('Base Style', pad=10)
    ax.legend(fontsize=9)
    
    # Base style with custom colors
    minimalist.use_style(['base', 'rdbuye'])
    ax = axes[0, 1]
    ax.plot(x_comp, y1, label=r'$\sin(x)$')
    ax.plot(x_comp, y2, label=r'$\cos(x)$')
    ax.set_xlabel(r'$\theta$ [radians]')
    ax.set_ylabel(r'$\phi(\theta)$')
    ax.set_title('Base + Custom Colors', pad=10)
    ax.legend(fontsize=9)
    
    # Science style (for publications)
    minimalist.use_style('science')
    ax = axes[1, 0]
    ax.plot(x_comp, y1, label=r'$\sin(x)$')
    ax.plot(x_comp, y2, label=r'$\cos(x)$')
    ax.set_xlabel(r'$x$ [radians]')
    ax.set_ylabel(r'$f(x)$')
    ax.set_title('Science Style', pad=10)
    ax.legend(fontsize=9)
    
    # Science style with custom colors
    minimalist.use_style(['science', 'rdbuye'])
    ax = axes[1, 1]
    ax.plot(x_comp, y1, label=r'$\sin(x)$')
    ax.plot(x_comp, y2, label=r'$\cos(x)$')
    ax.set_xlabel(r'$x$ [radians]')
    ax.set_ylabel(r'$f(x)$')
    ax.set_title('Science + Custom Colors', pad=10)
    ax.legend(fontsize=9)
    
    fig.text(0.02, 0.02, 'Base: Only bottom/left spines | Science: All spines visible', 
             fontsize=9, style='italic', bbox=dict(boxstyle="round,pad=0.3", facecolor="lavender", alpha=0.5))
    
    plt.tight_layout(rect=[0, 0.08, 1, 0.92])
    pdf.savefig(fig)
    plt.close()

print(f"All plots saved to {pdf_filename}")
print("\nColor palettes used:")
print("- Qualitative: RdBuYe_q (5 colors), RdBuBl_q (9 colors)")
print("- Diverging: RdBuYe, Rdbu_bl, Rdbu_w (and their reversed versions)")
print("\nStyles:")
print("- Base: Default style for everyday use (bottom/left spines only)")
print("- Science: For publications only (all spines visible)") 