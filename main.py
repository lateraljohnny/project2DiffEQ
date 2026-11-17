import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
# ---------------------------------------------------------
# Predator{Prey Model (Lotka{Volterra)
# ---------------------------------------------------------
# Prey: dx/dt = a*x - b*x*y
# Predator: dy/dt = c*x*y - d*y
#
# x(t): prey population
# y(t): predator population
# ---------------------------------------------------------
def predator_prey(t, vars):
x, y = vars
# Parameters
a = 1.0 # prey growth rate
3
b = 0.1 # predation rate
c = 0.075 # predator reproduction efficiency
d = 1.5 # predator death rate
dxdt = a*x - b*x*y
dydt = c*x*y - d*y
return [dxdt, dydt]
# ---------------------------------------------------------
# Solve the system
# ---------------------------------------------------------
t_span = (0, 50) # time interval
initial_conditions = [40, 9] # x(0)=40 prey, y(0)=9 predators
solution = solve_ivp(predator_prey, t_span, initial_conditions, dense_output=True)
# High-resolution time grid for plotting
t = np.linspace(0, 50, 400)
x, y = solution.sol(t)
# ---------------------------------------------------------
# Plot results
# ---------------------------------------------------------
plt.figure(figsize=(12,5))
# Population vs. time
plt.subplot(1, 2, 1)
plt.plot(t, x, label="Prey")
plt.plot(t, y, label="Predators")
plt.xlabel("Time")
plt.ylabel("Population")
plt.title("Predator{Prey Dynamics")
plt.grid(True)
plt.legend()
# Phase portrait
plt.subplot(1, 2, 2)
plt.plot(x, y)
plt.xlabel("Prey")
plt.ylabel("Predators")
plt.title("Phase Plane (x vs y)")
plt.grid(True)
plt.tight_layout()
plt.show()
