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

def fermi_dirac(E, T):
    return 1 / (np.exp((E - mu) / (kB * T)) + 1)

def bose_einstein(E, T):
    with np.errstate(divide='ignore', invalid='ignore'):
        f = 1 / (np.exp((E - mu) / (kB * T)) - 1)
        f[E <= mu] = np.nan
    return f

temperatures = [100, 300, 600]

colors_fd = cm.magma(np.linspace(0.3, 0.9, len(temperatures)))
colors_be = cm.viridis(np.linspace(0.3, 0.9, len(temperatures)))

plt.figure(figsize=(9,6))

for i, T in enumerate(temperatures):
    plt.plot(E, fermi_dirac(E, T), 
             color=colors_fd[i], linestyle='-', linewidth=2.2,
             label=f'FD – {T} K')

for i, T in enumerate(temperatures):
    plt.plot(E, bose_einstein(E, T), 
             color=colors_be[i], linestyle='--', linewidth=2.2,
             label=f'BE – {T} K')

plt.title('Figure 3.2. Temperature Dependence of Fermi–Dirac and Bose–Einstein Distributions', 
          fontsize=13, fontweight='bold', pad=15)
plt.xlabel('Energy (eV)', fontsize=12)
plt.ylabel('Distribution Function f(E)', fontsize=12)
plt.xlim(0, 1)
plt.ylim(0, 5)
plt.grid(alpha=0.25, linestyle='--', linewidth=0.7)

plt.text(0.02, 4.6, 'Bosons → Dashed lines', fontsize=12, color='gray')
plt.text(0.02, 4.3, 'Fermions → Solid lines', fontsize=12, color='gray')

ax = plt.gca()
ax.set_facecolor('#fafafa')

for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_linewidth(0.8)

leg = plt.legend(loc='upper right', fontsize=10, ncol=2, frameon=False)
for text in leg.get_texts():
    text.set_fontfamily('Times New Roman')

plt.tight_layout()
plt.savefig("hasil32.png", dpi=600, transparent=True, bbox_inches='tight')
plt.show()
