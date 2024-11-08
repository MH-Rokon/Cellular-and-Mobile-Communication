
# 6.................................................




import numpy as np

# Constants
pt = 50  # Transmitted power in watts
fc = 900  # Carrier frequency in MHz
gt = 1  # Transmitter antenna gain
gr = 1  # Receiver antenna gain
d = 100  # Free space distance in meters
L = 1  # System loss factor

# Calculate wavelength (lambda)
lambda_ = (3 * 10**8) / (fc * 10**6)  # lambda = c / f

# Question (a)
tr_dBm = np.ceil(10 * np.log10(pt * 1000))  # Transmitter power in dBm
print(f"(a) Transmitter power, Pt in dBm: {int(tr_dBm)} dBm\n")

# Question (b)
tr_dBW = np.ceil(10 * np.log10(pt))  # Transmitter power in dBW
print(f"(b) Transmitter power, Pt in dBW: {int(tr_dBW)} dBW\n")

# Question (c)
c = (pt * gt * gr * (lambda_ ** 2)) / ((4 * np.pi) ** 2 * d ** 2 * L) * 1000  # Received power in milliwatts
Pr = 10 * np.log10(c)  # Received power in dBm
print(f"(c) Received power, Pr in dBm: {Pr:.2f} dBm\n")

# Question (d)
d_10km = Pr + (20 * np.log10(d / 10000))  # Received power at 10 km in dBm
print(f"(d) Received power, Pr at 10km in dBm: {d_10km:.2f} dBm\n")




