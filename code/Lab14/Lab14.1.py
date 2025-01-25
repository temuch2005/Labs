import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4, 500)
y = 5 * np.sin(10 * x) * np.sin(3 * x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label="Y(x) = 5 * sin(10x) * sin(3x)", color='blue', linewidth=2, linestyle='-')

plt.xlabel("x", fontsize=12)
plt.ylabel("Y(x)", fontsize=12)
plt.title("Графік функції Y(x) = 5 * sin(10x) * sin(3x)", fontsize=14)

plt.grid(True)
plt.legend(fontsize=12)

plt.show()
