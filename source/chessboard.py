"""
This code uses numpy and matplotlib libraries and results in a chessboard.

-> Requirements:
    . pip install numpy
    . pip install matplotlib
"""

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

chessboard = np.tile([1, 0], (8, 4))

for i in range(chessboard.shape[0]):
    chessboard[i] = np.roll(chessboard[i], i % 2)

colormap = ListedColormap(['#000000', '#ffffff'])
plt.matshow(chessboard, cmap=colormap)
plt.xticks([])
plt.yticks([])
plt.show()
