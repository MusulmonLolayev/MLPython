import numpy as np
from ai.own.estimations import DivideIntervals

x = np.array([14.6, 12.1, 18.9, 10.7, 13.4, 11.5, 9, 21.7, 41, 22.3, 12.5, 19.8, 10, 10.7, 11.1, 25.1, 19.5, 7.7, 17, 15.1, 16.6, 21, 25, 15.2, 9.9, 11, 43.5, 16.2, 29.7, 18, 24.7, 28, 27, 22, 14.2, 11.6, 29.6, 16.1, 35.9, 19.2, 32.5, 24, 22, 11.7, 25, 12.2, 15, 9.2, 8.9, 14.3, 35.9, 10.9, 6.5, 113.8, 16.8, 16.2, 26.6, 14.2, 33.75, 19])
y = np.array([0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0])

DivideIntervals(x, y)