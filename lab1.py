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


