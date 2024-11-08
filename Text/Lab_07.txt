import numpy as np

# Given values
hte = 100  # Effective transmitter (base station) antenna height in meters
hre = 2    # Effective receiver (mobile) antenna height in meters
fc = 900   # Frequency in MHz
d = 4      # T-R separation distance in kilometers

# The correction factor using the Okumura-Hata model
a_hre = 3.2 * (np.log10(11.75 * hre))**2 - 4.97

# Path Loss in urban areas
Lp = (69.55 + 26.16 * np.log10(fc) - 13.82 * np.log10(hte)
      - a_hre + (44.9 - 6.55 * np.log10(hte)) * np.log10(d))

print(f'The path loss in urban areas, Lp = {Lp:.2f} dB')
