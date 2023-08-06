"""The purpose of this script is to confirm that I can load libs from PyPI

Step 1: Create virtual environment:

  python3 -m venv day16env 

Step 2: Activate the environment (on this terminal)

   source day16env/bin/activate # terminal CLI now shows (env)

Step 3: Update pip

   pip3 install --upgrade pip  # upgraded to verion pip-22.3.1

Step 4: Install matplotlib

   pip3 install matplotlib
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
