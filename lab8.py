


# 8..........................................................


import numpy as np

# Parameters
fc = 1.8  # Frequency in GHz
hb = 20   # Effective transmitter (base station) antenna height in meters
d = np.sqrt(20**2 + 30**2) / 1000  # T-R separation distance in kilometers

# Path loss in high-rise urban areas
Lp = (135.41 + (12.49 * np.log10(fc)) - (4.99 * np.log10(hb)) 
      + ((46.84 - 2.34 * np.log10(hb)) * np.log10(d)))

# Display result
print(f"The path loss in high-rise urban areas, Lp = {Lp:.2f} dB")


