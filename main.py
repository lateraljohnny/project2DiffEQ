import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# Ant Colony Disease Model (SIZ)
# ---------------------------------------------------------
# Susceptible: dS/dt
# Infected: dI/dt
# Immune: dZ/dt
#
# S(t): susceptible population
# I(t): infected population
# Z(t): immune population
# ---------------------------------------------------------
def predator_prey(t, vars):
S, I, Z = vars
N = S + I + Z
# Parameters
b = 0.05 # birth rate
d = 0.0001 # death rate
alpha = 0.05 # death rate by disease
beta = 0.0012 # transmission rate
gamma = 0.10 # recover rate
dSdt = (b*N) - (beta*S*I) - (d*N*S)
dIdt = (beta*S*I) - (gamma*I) - (d*N*I) - (alpha*I)
dZdt = (gamma*I) - (d*N*I)

return [dSdt, dIdt, Dzdt]

# ---------------------------------------------------------
# Solve the system
# ---------------------------------------------------------
t_span = (0, 150) # time interval
initial_conditions = [450, 20, 0] # S(0) = 450, I(0) = 20, Z(0) = 0
solution = solve_ivp(predator_prey, t_span, initial_conditions, dense_output=True)

# High-resolution time grid for plotting
t = np.linspace(0, 150, 500)
S, I, Z = solution.sol(t)

# ---------------------------------------------------------
# Plot results
# ---------------------------------------------------------
plt.figure(figsize=(12, 5))

# Population vs. time
plt.subplot(1, 2, 1)
plt.plot(t, S, label="Susceptible")
plt.plot(t, I, label="Infected")
plt.plot(t, Z, label="Immune")
plt.xlabel("Time (Days)")
plt.ylabel("Population")
plt.title("Ant Colony Disease Dynamics")
plt.grid(True)
plt.legend()

# Phase portrait
plt.subplot(1, 2, 2)
plt.plot(S, I, color='crimson', linewidth=2)
plt.xlabel("Susceptible")
plt.ylabel("Infected")
plt.title("Phase Plane (S vs I)")
plt.grid(True)

plt.tight_layout()
plt.show()
