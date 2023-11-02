# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import lfilter, savgol_filter

# Load Data
data = pd.read_csv('Double_Muon_Run.csv')

# Defines list + index
massList = []
charge_epsilon = 0.1
mass_limit = 5
charge_errors = 0
mass_errors = 0

# Loops through each valid trial, finds the momentum and energy of each particle in each of those trails. 
# It the net momentum and energy of both particle and uses the formula E^2 = p^2 + m^2 to find the mass 
for i in range(len(data['Run'])):
    print(i)
    momentum1 = np.array([data['px1'][i], data['py1'][i], data['pz1'][i]]) # Finds momentum of first particle
    momentum2 = np.array([data['px2'][i], data['py2'][i], data['pz2'][i]]) # Finds momentum of second particle

    netMomentum = momentum1 + momentum2 # Adds those momentums into one net momentum array
    netMomentum = np.linalg.norm(netMomentum) # Normalizes the net momentum

    netEnergy = data['E1'][i] + data['E2'][i] # Finds the net energy of both particles 
    mass = (netEnergy ** 2 - netMomentum ** 2) ** 0.5 # Finds the mass with the formula E^2 = p^2 + m^2

    netCharge = data['Q1'][i] + data['Q2'][i]
    if netCharge > charge_epsilon or netCharge < -charge_epsilon:
        charge_errors += 1
        continue
    if mass > mass_limit:
        mass_errors += 1
        continue
    massList.append(mass)

print(f"Number of events filtered by charge: {charge_errors}")
print(f"Number of events filtered by mass: {mass_errors}")

bins_step = 0.01
max_bin = max(massList) * 1.25
bins = [i * bins_step for i in range(int(max_bin / bins_step))]

# Plots a histogram of the masses
plt.hist(massList, bins) 
plt.title("Mass of j/psi Particles") 
plt.xlabel("Mass")
plt.ylabel("Count")
plt.show()