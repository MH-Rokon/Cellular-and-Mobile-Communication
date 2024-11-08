

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



