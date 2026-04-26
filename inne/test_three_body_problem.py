import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# Definicja równań ruchu (Prawo grawitacji Newtona)
def model(y, t):
    # Pozycje (x, y) i prędkości (vx, vy) dla 3 ciał
    r1, r2, r3 = y[0:2], y[2:4], y[4:6]
    v1, v2, v3 = y[6:8], y[8:10], y[10:12]

    G = 1.0  # Stała grawitacyjna (uproszczona)
    m = 1.0  # Masy ciał

    # Obliczanie odległości
    r12 = np.linalg.norm(r2 - r1)
    r13 = np.linalg.norm(r3 - r1)
    r23 = np.linalg.norm(r3 - r2)

    # Przyspieszenia (siły działające na każde ciało)
    a1 = G * m * (r2 - r1) / r12 ** 3 + G * m * (r3 - r1) / r13 ** 3
    a2 = G * m * (r1 - r2) / r12 ** 3 + G * m * (r3 - r2) / r23 ** 3
    a3 = G * m * (r1 - r3) / r13 ** 3 + G * m * (r2 - r3) / r23 ** 3

    return [*v1, *v2, *v3, *a1, *a2, *a3]


# Warunki początkowe (delikatnie dobrane, by stworzyć chaos)
# Pozycje x, y dla trzech ciał
y0 = [
    0.97002, -0.24,  # Ciało 1
    -0.97, 0.24,  # Ciało 2
    0.0, 0.0,  # Ciało 3
    0.46, 0.43,  # Prędkość 1
    0.46, 0.43,  # Prędkość 2
    -0.93, -0.86  # Prędkość 3
]

t = np.linspace(0, 10, 1000)
sol = odeint(model, y0, t)

# Rysowanie wyniku
plt.figure(figsize=(8, 8))
plt.plot(sol[:, 0], sol[:, 1], label="Ciało 1", color='red')
plt.plot(sol[:, 2], sol[:, 3], label="Ciało 2", color='blue')
plt.plot(sol[:, 4], sol[:, 5], label="Ciało 3", color='green')
plt.legend()
plt.title("Chaos w Problemie Trzech Ciał")
plt.grid(True)
plt.show()