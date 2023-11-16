

# Scope trace
scope_trace = [0, 0, 0.1, 0, 0.5, 0.6, 0.7, 1, 1, 1,
               0.9, 0.8, 0.5, 0.2, 0, 0, 0, 0.3, 0.5, 0.7, 1.1, 1.0]

# We want to find where the trace goes above a threshold voltage
threshold = 0.6

# Let's just apply the threshold to the points
above_thd = [int(voltage > threshold) for voltage in scope_trace]

# now just get the index of the First crossing of the threshold on rising edge
print(above_thd.index(1))

# Detect mutiple transitions (both rising and falling edges crossing the threshold)
above_thd_lag = [0] + above_thd[:-1]
transitions = [current-previous for (current, previous) in zip(above_thd, above_thd_lag)]

# indexes of the rising and falling edges
rising_edges = [n for n, v in enumerate(transitions) if v == 1]
falling_edges = [n for n, v in enumerate(transitions) if v == -1]


import numpy as np

# Scope trace
scope_trace = np.array([0, 0, 0.1, 0, 0.5, 0.6, 0.7, 1, 1, 1,
                        0.9, 0.8, 0.5, 0.2, 0, 0, 0, 0.3, 0.5, 0.7, 1.1, 1.0])

# Thresholding using NumPy
above_thd = (scope_trace > 0.6).astype(int)

# Find index of the first crossing of the threshold on rising edge
first_crossing_index = np.argmax(above_thd)
print(first_crossing_index)

# Edge detection using NumPy
above_thd_lag = np.roll(above_thd, 1)
above_thd_lag[0] = 0

transitions = above_thd - above_thd_lag

# Indexes of the rising and falling edges using NumPy
rising_edges = np.where(transitions == 1)[0]
falling_edges = np.where(transitions == -1)[0]

print("Rising Edges:", rising_edges)
print("Falling Edges:", falling_edges)
