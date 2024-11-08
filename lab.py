# 1..........................



# Import necessary libraries
import numpy as np

# Define cluster sizes as a list of integers
cluster_sizes = [4, 7, 12]  # Example cluster sizes; adjust as needed

# Define bandwidth and channel parameters
bw = 33000  # Total Bandwidth in kHz
sim_ch_bw = 25  # Simplex channel bandwidth in kHz
dup_ch_bw = 2 * sim_ch_bw  # Duplex channel bandwidth in kHz
t_ch = bw / dup_ch_bw  # Total available channels
cc_bw = 1000  # Control channel bandwidth in kHz
t_cc = cc_bw / dup_ch_bw  # The number of available control channels

# Calculate and display results for each cluster size
for N in cluster_sizes:
    ch_per_cell = round(t_ch / N)  # Channels available per cell
    vc = round((t_ch - t_cc) / N)  # Voice channels per cell
    cc = ch_per_cell - vc  # Control channels per cell

    # Display the results
    print(f"For Cluster size N = {N}")
    print("-------------------------")
    print(f"Total number of channels available per cell: {ch_per_cell} channels")
    print(f"Voice Channels: {vc} channels")
    print(f"Control Channels: {cc} channels\n\n")


# 2..........................
 
import math 
 
def calculate_frequency_reuse_factor(N): 
    Q = math.sqrt(3 * N) 
    return Q 
 
def calculate_SIR(io, n, Q): 
    SI = 10 * math.log10((1 / io) * (Q ** n)) 
    return SI 
 
def find_optimal_parameters(R_SI, io, N): 
    for n in [4, 3]: 
        Q = calculate_frequency_reuse_factor(N) 
        SI = calculate_SIR(io, n, Q) 
        print(f"For n = {n}:") 
        print(f"Frequency reuse factor (Q): {Q}") 
        print(f"Signal to interference ratio (SI): {SI} dB") 
 
        if SI < R_SI: 
            # Adjusting parameters 
            i = 2 
            j = 2 
            N = i ** 2 + i * j + j ** 2 
            Q = calculate_frequency_reuse_factor(N) 
            SI = calculate_SIR(io, n, Q) 
            print("Adjusting parameters:") 
            print(f"New Frequency reuse factor (Q): {Q}") 
            print(f"New Signal to interference ratio (SI): {SI} dB") 
        print() 
 
# Given parameters 
R_SI = 15  # Required signal to interference ratio (dB) 
io = 6  # Path loss exponent 
 
# Finding optimal parameters 
find_optimal_parameters(R_SI, io, 7) 




# 3...................................................


import numpy as np

# Define constants
GOS = 0.5 / 100  # Blocking probability (0.5%)
Au = 0.1  # Traffic intensity per user

# Offered Traffic Intensity, A (from Erlang B chart)
A = np.array([0.005, 1.13, 3.96, 11.1, 80.9])

# Trunked Channels, C
C = np.array([1, 5, 10, 20, 100])

# Calculate total number of users
U = np.round(A / Au).astype(int)  # Total number of users

# Print results
print(f"Grade of Service, GOS = {GOS:.3f}")
print("Trunked Channels, C:")
print(C)
print("From table 3.1, we obtain Offered Traffic Intensity, A For all Channels, C:")
print(A)
print("Total number of users, U")
print("---------------------------")
print(U)




# 4.............................................


# Define constants
blocking_probability = 2 / 100  # GOS
population = 2000000
Au = (2 / 60) * 3  # Traffic intensity per user

# System A calculations
print("For system A:")
print("--------------")
C1 = 19  # Number of channels per cell for System A
A1 = 12  # Total traffic intensity from Erlang B chart for GOS=0.02, C=19
U1 = A1 / Au  # Total number of users for System A
Aa = U1 * 394  # Total number of subscribers for System A
percentage_A = (Aa / population) * 100  # Market penetration percentage for System A

print(f"Total number of users for system A: {int(Aa)}")
print(f"Percentage market penetration for System A: {percentage_A:.3f}%\n\n")

# System B calculations
print("For system B:")
print("--------------")
C2 = 57  # Number of channels per cell for System B
A2 = 45  # Total traffic intensity from Erlang B chart for GOS=0.02, C=57
U2 = A2 / Au  # Total number of users for System B
Bb = U2 * 98  # Total number of subscribers for System B
percentage_B = (Bb / population) * 100  # Market penetration percentage for System B

print(f"Total number of users for system B: {int(Bb)}")
print(f"Percentage market penetration for System B: {percentage_B:.3f}%\n\n")

# System C calculations
print("For system C:")
print("--------------")
C3 = 100  # Number of channels per cell for System C
A3 = 88  # Total traffic intensity from Erlang B chart for GOS=0.02, C=100
U3 = A3 / Au  # Total number of users for System C
Cc = U3 * 49  # Total number of subscribers for System C
percentage_C = (Cc / population) * 100  # Market penetration percentage for System C

print(f"Total number of users for system C: {int(Cc)}")
print(f"Percentage market penetration for System C: {percentage_C:.3f}%\n\n")

# Total subscribers across all systems
print("For all three systems:")
print("--------------------")
T = Aa + Bb + Cc  # Total subscribers for all systems
percentage_T = (T / population) * 100  # Overall market penetration percentage

print(f"Total number of users of all three systems: {int(T)}")
print(f"Percentage market penetration for all three systems: {percentage_T:.3f}%")






# 5............................................................



import numpy as np

# Question (a)
total_city_coverage_area = 1300
radius = 4
a = 2.591 * radius ** 2  # Each cell covers area a
Nc = round(total_city_coverage_area / a)  # Total number of cells, Nc
print(f"(a) Total number of cells, Nc: {Nc} cells\n")

# Question (b)
allocated_spectrum = 40000  # Allocated spectrum = 40MHz
channel_width = 60  # Full duplex channel bandwidth = 60 kHz
N = 7  # Cluster size
C = round(allocated_spectrum / (channel_width * N))  # Total channels per cell
print(f"(b) The total number of channels per cell, C: {C} channels/cell\n")

# Question (c)
A = 84  # Given traffic intensity per cell in Erlangs
print(f"(c) Traffic intensity per cell, A: {A} Erlangs/cell\n")

# Question (d)
max_c_t = Nc * A  # Maximum carried traffic
print(f"(d) Maximum carried traffic: {max_c_t} Erlangs\n")

# Question (e)
U = round(max_c_t / 0.03)  # Total number of users (traffic per user, Au = 0.03)
print(f"(e) Total number of users, U: {U} users\n")

# Question (f)
no_of_channel = allocated_spectrum // channel_width  # Total number of channels available
no_of_m_p_c = U // no_of_channel  # Number of mobiles per channel
print(f"(f) Number of mobiles per channel: {no_of_m_p_c} mobiles/channel\n")

# Question (g)
g = C * Nc  # Theoretical maximum number of users that could be served
print(f"(g) Theoretical maximum number of users that could be served: {g} users\n")







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







# 7.............................................................



import numpy as np

# Parameters
hte = 100  # Effective transmitter (base station) antenna height in meters
hre = 2    # Effective receiver (mobile) antenna height in meters
fc = 900   # Frequency in MHz
d = 4      # T-R separation distance in kilometers

# Correction factor using Okumura-Hata model
a_hre = (3.2 * (np.log10(11.75 * hre)) ** 2) - 4.97

# Path loss in urban areas
Lp = (69.55 + 26.16 * np.log10(fc) - 13.82 * np.log10(hte) 
      - a_hre + (44.9 - 6.55 * np.log10(hte)) * np.log10(d))

# Display result
print(f"The path loss in urban areas, Lp = {Lp:.2f} dB")










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







# 9..................................................




import numpy as np

# Parameters
f = 900  # Frequency in MHz
g = 2.55  # Gain of antenna in dB

# Question (a)
gain = 10 ** (g / 10)
lambda_ = (3 * 10**8) / (f * 10**6)  # Wavelength in meters
L = lambda_ / 4  # Antenna length
print("For (a)")
print("---------")
print(f"Length of the antenna: {L:.3f} m")
print(f"Gain of the antenna: {gain:.1f} = {g:.2f} dB\n")

# Question (b)
d = 5000  # T-R separation distance in meters
E0 = 10**-3  # Electric field in V/m
d0 = 1000  # Transmitter reference distance in meters
ht = 50  # Transmitting antenna height in meters
hr = 1.5  # Receiving antenna height in meters

# Electric Field
Er_d = (2 * E0 * d0 * 2 * np.pi * ht * hr) / (lambda_ * d**2)

# Effective Aperture
Ae = (gain * lambda_**2) / (4 * np.pi)

# Received Power at distance d
Pr_d = (Er_d**2 / (120 * np.pi)) * Ae
Pr_dB = 10 * np.log10(Pr_d)

print("For (b)")
print("---------")
print(f"Electric Field, Er(d): {Er_d:.9f} V/m")
print(f"Effective Aperture, Ae: {Ae:.3f} m^2")
print(f"Received power at 5 km distance, Er(5 km): {Pr_dB:.3f} dBW")









# 10...............................................





import numpy as np

# Parameters
R = 1.387  # Cell radius in km
n = 4      # Number of cells
N = 60     # Total number of channels
area = round(2.5981 * R**2)  # Area covered per cell in square km
C = N / 4  # Number of channels per cell
A = 9      # Traffic intensity for C=15, GOS=0.05, Au=0.029 from Erlang C chart

# Question (a)
Au = 0.029  # Traffic per user
U = int(A / Au)  # Total number of users
U_per = round(U / area)  # Number of users per square km
print("(a) Number of users per square km:", U_per, "users/sq km\n")

# Question (b)
lambda_ = 1  # lambda = 1 hour
H = (Au / lambda_) * 3600  # Holding time in seconds
Prb = np.exp((-(C - A) * 10) / H)  # Probability of delayed call, t=10s, C=15, A=9, H=104.4
print("(b) The probability that a delayed call will have to wait: {:.2f}%".format(Prb * 100), "\n")

# Question (c)
Prc = 0.05 * Prb * 100  # 5% probability of delayed call
print("(c) The probability that a call will be delayed:", "{:.2f}%".format(Prc), "\n")




