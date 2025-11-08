Python code for visualizing and analyzing Bose–Einstein (BE) and Fermi–Dirac (FD) distributions in 3D identical particle systems.

This repository contains the computational model developed for:
*“Visualization and Analysis of Bose–Einstein and Fermi–Dirac Distributions in a 3D Identical Particle System Using Python.”*

The project includes five Python scripts for simulation, validation, and visualization. Each file performs a specific computational task, allowing the distributions to be compared and analyzed both numerically and graphically.

- `main.py` — main execution script that integrates all components.
- `be_distribution.py` — computes Bose–Einstein distribution function.
- `fd_distribution.py` — computes Fermi–Dirac distribution function.
- `visualization.py` — generates 2D and 3D plots of the results.
- `validation.py` — compares numerical and analytical solutions.

To install dependencies, run:
```bash
pip install -r requirements.txt

python src/main.py

jupyter notebook notebooks/simulation.ipynb
