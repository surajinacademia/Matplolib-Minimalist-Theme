"""
Comprehensive demo of the minimalist matplotlib style package
Creates a multi-page PDF showcasing all features
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import minimalist
import os

# Create plots directory
os.makedirs('plots', exist_ok=True)

# Set random seed for reproducibility
np.random.seed(42)

# Create PDF for all plots
pdf_filename = 'plots/minimalist_showcase.pdf'

with PdfPages(pdf_filename) as pdf:
    
    # Page 1: Science style - Line plots
    minimalist.use_style('science')
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(minimalist.FW, minimalist.FW_3))
    fig.suptitle('Science Style - With Tick Marks', fontsize=10)
    
    x = np.linspace(0, 2*np.pi, 100)
    
    # Left subplot - sine waves
    for i in range(6):
        y = np.sin(x + i*np.pi/6)
        ax1.plot(x, y, label=f'Phase {i}')
    ax1.set_xlabel(r'$x$ [radians]')
    ax1.set_ylabel('Amplitude')
    ax1.set_title('Sine Waves')
    ax1.legend(fontsize=6, ncol=2)
    
    # Right subplot - exponential decay
    t = np.linspace(0, 5, 100)
    for i in range(6):
        tau = 0.5 + i * 0.3
        y = np.exp(-t/tau)
        ax2.plot(t, y, label=rf'$\tau$={tau:.1f}')
    ax2.set_xlabel('Time [s]')
    ax2.set_ylabel('Amplitude')
    ax2.set_title('Exponential Decay')
    ax2.legend(fontsize=6, ncol=2)
    
    plt.tight_layout()
    pdf.savefig(fig)
    plt.close()
    
    # Page 2: Base style - Minimal plots
    minimalist.use_style('base')
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(minimalist.FW, minimalist.FW_3))
    fig.suptitle('Base Style - Minimal (No Tick Marks)', fontsize=10)
    
    # Left subplot - mathematical functions
    x = np.linspace(-2, 2, 100)
    functions = [
        (np.sin, r'$\sin(x)$'),
        (np.cos, r'$\cos(x)$'),
        (np.tanh, r'$\tanh(x)$'),
        (lambda x: x**2/4, r'$x^2/4$'),
        (lambda x: np.exp(-x**2), r'$e^{-x^2}$'),
        (lambda x: x/2, r'$x/2$'),
    ]
    
    for func, label in functions:
        ax1.plot(x, func(x), label=label)
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_title('Mathematical Functions')
    ax1.legend(fontsize=6, ncol=2)
    
    # Right subplot - Gaussian distributions
    x_gauss = np.linspace(-4, 4, 100)
    for i in range(6):
        mu = (i - 2.5) * 0.8
        sigma = 0.5 + i * 0.1
        y = (1/(sigma*np.sqrt(2*np.pi))) * np.exp(-0.5*((x_gauss-mu)/sigma)**2)
        ax2.plot(x_gauss, y, label=rf'$\mu$={mu:.1f}')
    ax2.set_xlabel('x')
    ax2.set_ylabel('Probability Density')
    ax2.set_title('Gaussian Distributions')
    ax2.legend(fontsize=6, ncol=2)
    
    plt.tight_layout()
    pdf.savefig(fig)
    plt.close()
    
    # Page 3: Heatmaps with minimalist colormap
    minimalist.use_style('science')
    
    fig, axes = plt.subplots(1, 2, figsize=(minimalist.FW, minimalist.FW_3))
    fig.suptitle('Continuous Colormaps for Heatmaps', fontsize=10)
    
    # Generate smooth sample data
    x_heat = np.linspace(-3, 3, 50)
    y_heat = np.linspace(-3, 3, 50)
    X, Y = np.meshgrid(x_heat, y_heat)
    data = np.sin(X) * np.cos(Y)
    
    # minimalist colormap
    ax = axes[0]
    im = ax.imshow(data, cmap='minimalist', aspect='auto', interpolation='bilinear')
    ax.set_title("cmap='minimalist'", fontsize=9)
    plt.colorbar(im, ax=ax, shrink=0.8)
    ax.set_xticks([])
    ax.set_yticks([])
    
    # minimalist_r colormap (reversed)
    ax = axes[1]
    im = ax.imshow(data, cmap='minimalist_r', aspect='auto', interpolation='bilinear')
    ax.set_title("cmap='minimalist_r'", fontsize=9)
    plt.colorbar(im, ax=ax, shrink=0.8)
    ax.set_xticks([])
    ax.set_yticks([])
    
    plt.tight_layout()
    pdf.savefig(fig)
    plt.close()
    
    # Page 4: Scatter plots and error bars
    minimalist.use_style('science')
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(minimalist.FW, minimalist.FW_3))
    fig.suptitle('Scatter Plots and Error Bars', fontsize=10)
    
    # Scatter plot
    for i in range(6):
        x_scatter = np.random.randn(20) + i
        y_scatter = np.random.randn(20) + i * 0.5
        ax1.scatter(x_scatter, y_scatter, label=f'Group {i+1}', s=15)
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_title('Scatter Plot')
    ax1.legend(fontsize=6, ncol=2)
    
    # Error bar plot
    x_err = np.arange(6)
    y_err = np.array([1.2, 2.1, 3.5, 2.8, 4.2, 3.9])
    yerr = np.array([0.2, 0.3, 0.4, 0.25, 0.35, 0.3])
    colors = minimalist.BASE_COLORS
    for i in range(6):
        ax2.errorbar(x_err[i], y_err[i], yerr=yerr[i], fmt='o', 
                     color=colors[i], markersize=5, capsize=0)
    ax2.set_xlabel('Condition')
    ax2.set_ylabel('Value')
    ax2.set_title('Error Bars (capsize=0)')
    ax2.set_xticks(x_err)
    
    plt.tight_layout()
    pdf.savefig(fig)
    plt.close()

print(f"All plots saved to {pdf_filename}")
print(f"\nFigure widths: FW={minimalist.FW:.2f}, FW_2={minimalist.FW_2:.2f}, FW_3={minimalist.FW_3:.2f}")
print(f"Base colors: {minimalist.BASE_COLORS}")
print("\nStyles:")
print("  - science: Clean style with tick marks")
print("  - base: Minimal style without tick marks")
print("\nColormaps:")
print("  - 'minimalist': Continuous colormap for heatmaps")
print("  - 'minimalist_r': Reversed version")