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
E = np.linspace(0.01, 1.0, 120)
T = np.linspace(100, 600, 120)
E_grid, T_grid = np.meshgrid(E, T)

def fermi_dirac(E, T):
    return 1.0 / (np.exp((E - mu) / (kB * T)) + 1.0)

f = fermi_dirac(E_grid, T_grid)
f = np.nan_to_num(f, nan=0.0)

cmap = cm.plasma
alpha_level = 0.9

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

surf = ax.contourf3D(E_grid, T_grid, f, levels=30, cmap=cmap, alpha=alpha_level, antialiased=True)

ax.set_title('Figure 3.4. 3D Contour Cloud of Fermi–Dirac Particle Distribution',
             fontsize=13, fontweight='bold', pad=20)
ax.set_xlabel('Energy (eV)', fontsize=12, labelpad=10)
ax.set_ylabel('Temperature (K)', fontsize=12, labelpad=10)
ax.set_zlabel('f(E, T)', fontsize=12, labelpad=10)

ax.view_init(elev=28, azim=-55)
ax.xaxis.pane.set_facecolor('#f8f9fa')
ax.yaxis.pane.set_facecolor('#f8f9fa')
ax.zaxis.pane.set_facecolor('#ffffff')
ax.xaxis.pane.set_alpha(0.95)
ax.yaxis.pane.set_alpha(0.95)
ax.zaxis.pane.set_alpha(1.0)

cbar = fig.colorbar(surf, ax=ax, shrink=0.6, aspect=15, pad=0.08)
cbar.set_label('Distribution Intensity', fontsize=11)

ax.text(0.8, 250, 2.8, 'Fully Occupied Fermi Region', color='black', fontsize=11)
ax.text(0.8, 450, 0.5, 'Energy Transition Region', color='black', fontsize=11)

ax.set_facecolor('#fafafa')

plt.tight_layout()

plt.savefig("hasilfigure3_4.png", dpi=600, transparent=True, bbox_inches='tight')
plt.show()
