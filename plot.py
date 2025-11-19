import math
import matplotlib.pyplot as plt

x = [i / 50 for i in range(500)]
plt.plot(x,[math.sin(t) for t in x])
plt.show() 