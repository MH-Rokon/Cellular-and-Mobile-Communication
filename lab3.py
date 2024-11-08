

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



