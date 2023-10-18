import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/meganalvord/partilcephysicsdata/main/JPsi_uu_candidates.csv')

events = [1, 3, 5, 6, 8, 10]
events = [evt - 1 for evt in events]

def calc_mass(e1, e2, px1, py1, pz1, px2, py2, pz2):
    e2 = (e1 + e2) ** 2
    p1_v = np.array([px1, py1, pz1])
    p2_v = np.array([px2, py2, pz2])
    p_v = p1_v + p2_v
    p = np.linalg.norm(p_v)
    p2 = p ** 2
    return np.sqrt(e2 - p2)

masses = [calc_mass(data['E1'][i], data['E2'][i], data['px1'][i], data['py1'][i], data['pz1'][i], data['px2'][i], data['py2'][i], data['pz2'][i]) for i in 
          events]

print("Masses: ", masses)

b = len(list(dict.fromkeys(masses)))

plt.hist(masses, bins = b) 
plt.title("Calculated JPsi masses")
plt.xlabel("JPsi mass (MeV/c^2)")
plt.ylabel("Number of events") 
plt.show()
