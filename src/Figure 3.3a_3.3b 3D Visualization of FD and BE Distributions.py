import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm, rcParams
from mpl_toolkits.mplot3d import Axes3D

rcParams['font.family'] = 'Times New Roman'
rcParams['font.size'] = 12
rcParams['axes.linewidth'] = 1
rcParams['axes.edgecolor'] = 'gray'

kB = 8.617333262e-5
mu = 0.5
E = np.linspace(0, 1, 200)
T = np.linspace(100, 600, 200)
E_grid, T_grid = np.meshgrid(E, T)

def fermi_dirac(E, T):
    return 1 / (np.exp((E - mu) / (kB * T)) + 1)

def bose_einstein(E, T):
    with np.errstate(divide='ignore', invalid='ignore'):
        f = 1 / (np.exp((E - mu) / (kB * T)) - 1)
        f[E <= mu] = np.nan
    return f

f_FD = fermi_dirac(E_grid, T_grid)
f_BE = bose_einstein(E_grid, T_grid)

fig = plt.figure(figsize=(13, 6))

ax1 = fig.add_subplot(1, 2, 1, projection='3d')
surf_fd = ax1.plot_surface(E_grid, T_grid, f_FD, cmap=cm.magma, 
                           linewidth=0, antialiased=True, alpha=0.9)

ax1.set_title('(a) Fermi–Dirac Distribution', fontsize=13, fontweight='bold', pad=15)
ax1.set_xlabel('Energy (eV)', fontsize=12, labelpad=10)
ax1.set_ylabel('Temperature (K)', fontsize=12, labelpad=10)
ax1.set_zlabel('f(E, T)', fontsize=12, labelpad=10)
ax1.view_init(elev=30, azim=-60)
ax1.xaxis.pane.set_facecolor('#f8f9fa')
ax1.yaxis.pane.set_facecolor('#f8f9fa')
ax1.zaxis.pane.set_facecolor('#ffffff')
ax1.xaxis.pane.set_alpha(0.95)
ax1.yaxis.pane.set_alpha(0.95)
ax1.zaxis.pane.set_alpha(1.0)
ax1.text(0.8, 250, 3.0, 'Fermions', color='black', fontsize=11)

cbar1 = fig.colorbar(cm.ScalarMappable(cmap=cm.magma), ax=ax1, shrink=0.6, aspect=15, pad=0.08)
cbar1.set_label('Distribution Intensity', fontsize=11)

ax2 = fig.add_subplot(1, 2, 2, projection='3d')
surf_be = ax2.plot_surface(E_grid, T_grid, f_BE, cmap=cm.viridis,
                           linewidth=0, antialiased=True, alpha=0.9)

ax2.set_title('(b) Bose–Einstein Distribution', fontsize=13, fontweight='bold', pad=15)
ax2.set_xlabel('Energy (eV)', fontsize=12, labelpad=10)
ax2.set_ylabel('Temperature (K)', fontsize=12, labelpad=10)
ax2.set_zlabel('f(E, T)', fontsize=12, labelpad=10)
ax2.view_init(elev=30, azim=-60)
ax2.xaxis.pane.set_facecolor('#f8f9fa')
ax2.yaxis.pane.set_facecolor('#f8f9fa')
ax2.zaxis.pane.set_facecolor('#ffffff')
ax2.xaxis.pane.set_alpha(0.95)
ax2.yaxis.pane.set_alpha(0.95)
ax2.zaxis.pane.set_alpha(1.0)
ax2.text(0.8, 250, 3.0, 'Bosons', color='black', fontsize=11)

cbar2 = fig.colorbar(cm.ScalarMappable(cmap=cm.viridis), ax=ax2, shrink=0.6, aspect=15, pad=0.08)
cbar2.set_label('Distribution Intensity', fontsize=11)

fig.suptitle('Figure 3.3. 3D Visualization of Fermi–Dirac and Bose–Einstein Distributions', 
             fontsize=14, fontweight='bold', y=0.96)

plt.tight_layout()

plt.savefig("hasil.png", dpi=600, transparent=True, bbox_inches='tight')
plt.show()
