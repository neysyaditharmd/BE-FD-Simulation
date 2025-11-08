import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm, rcParams

rcParams['font.family'] = 'Times New Roman'
rcParams['font.size'] = 12
rcParams['axes.linewidth'] = 1
rcParams['axes.edgecolor'] = 'gray'

kB = 8.617333262e-5
mu = 0.5
E = np.linspace(0, 1, 400)
T = 300

def fermi_dirac(E, T):
    return 1 / (np.exp((E - mu) / (kB * T)) + 1)

def bose_einstein(E, T):
    with np.errstate(divide='ignore', invalid='ignore'):
        f = 1 / (np.exp((E - mu) / (kB * T)) - 1)
        f[E <= mu] = np.nan
    return f

f_FD = fermi_dirac(E, T)
f_BE = bose_einstein(E, T)

color_fd = cm.magma(0.65)
color_be = cm.viridis(0.75)

plt.figure(figsize=(9,6))
plt.plot(E, f_FD, color=color_fd, linewidth=2.5, label='Fermi–Dirac (FD)')
plt.plot(E, f_BE, color=color_be, linewidth=2.5, linestyle='--', label='Bose–Einstein (BE)')

plt.title('Figure 3.1. Validation of Fermi–Dirac and Bose–Einstein Distributions at 300 K', 
          fontsize=13, fontweight='bold', pad=15)
plt.xlabel('Energy (eV)', fontsize=12)
plt.ylabel('Distribution Function f(E)', fontsize=12)
plt.xlim(0, 1)
plt.ylim(0, 5)
plt.grid(alpha=0.25, linestyle='--', linewidth=0.7)

ax = plt.gca()
ax.set_facecolor('#f8f9fa')

for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_linewidth(0.8)

plt.text(0.05, 4.5, 'Fermi–Dirac (solid line)', fontsize=12, color='gray')
plt.text(0.05, 4.1, 'Bose–Einstein (dashed line)', fontsize=12, color='gray')

leg = plt.legend(loc='upper right', fontsize=10, frameon=False)
for text in leg.get_texts():
    text.set_fontfamily('Times New Roman')

plt.tight_layout()
plt.savefig("hasil31.png", dpi=600, transparent=True, bbox_inches='tight')
plt.show()
