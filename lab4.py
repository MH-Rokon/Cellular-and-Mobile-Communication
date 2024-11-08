

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
