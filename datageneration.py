from beam import ss_center_point
import numpy as np
import pandas as pd

np.random.seed(42)

num_beams = 500
num_positions = 21


lengths = np.random.uniform(3.0, 10.0, num_beams)       
loads = np.random.uniform(10_000, 100_000, num_beams)
E_values = np.full(num_beams, 2.0e11)  
I_values = np.full(num_beams, 3.0e-4)  


positions_matrix = np.zeros((num_beams, num_positions))
deflections_matrix = np.zeros((num_beams, num_positions))


for i in range(num_beams):
    L = lengths[i]
    P = loads[i]
    E = E_values[i]
    I = I_values[i]

    x = np.linspace(0, L, num_positions)

    deflections = [ss_center_point(xi, L, P, E, I) for xi in x]
    positions_matrix[i, :] = x
    deflections_matrix[i, :] = deflections


summary_list = []
for i in range(num_beams):
    for j in range(num_positions):
        summary_list.append({
            'Beam ID': i + 1,
            'Total Length (m)': round(lengths[i], 2),
            'Load (kN)': round(loads[i] / 1000, 1),
            'E (Pa)': f"{E_values[i]:.2e}",                           
            'I (m⁴)': f"{I_values[i]:.2e}",
            'Position x (m)': round(positions_matrix[i, j], 3), # The specific coordinate out of the 21 points
            'Deflection (mm)': round(deflections_matrix[i, j] * 1000, 4) # The physical deflection at coordinate x
        })

df = pd.DataFrame(summary_list)
df.to_csv('beam_deflection_data.csv', index=False)

print(f"Successfully generated and saved {len(df)} rows to 'beam_deflection_data.csv'!")
