



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


