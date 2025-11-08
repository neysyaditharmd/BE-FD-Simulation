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
E = np.linspace(0, 1, 120)
T = np.linspace(100, 600, 120)
E_grid, T_grid = np.meshgrid(E, T)

def bose_einstein(E, T):
    with np.errstate(divide='ignore', invalid='ignore'):
        f = 1 / (np.exp((E - mu) / (kB * T)) - 1)
        f[E <= mu] = np.nan
    return f

f = bose_einstein(E_grid, T_grid)

cmap = cm.viridis
alpha_level = 0.85

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection='3d')

contours = ax.contour3D(E_grid, T_grid, f, levels=25, cmap=cmap,
                        alpha=alpha_level, linewidths=1.2)

ax.set_title('Figure 3.5. 3D Contour Cloud of Bose–Einstein Particle Distribution',
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

m = cm.ScalarMappable(cmap=cmap)
m.set_array(f)
cbar = fig.colorbar(m, ax=ax, shrink=0.6, aspect=15, pad=0.08)
cbar.set_label('Distribution Intensity', fontsize=11)

ax.text(0.75, 200, 3.5, 'Condensation Tendency', color='black', fontsize=11)
ax.text(0.75, 450, 0.8, 'Thermal Broadening', color='black', fontsize=11)

ax.set_facecolor('#fafafa')

plt.tight_layout()

plt.savefig("hasilfigure3_5.png", dpi=600, transparent=True, bbox_inches='tight')

plt.show()
