import numpy as np

rms = lambda v : np.sqrt(np.mean(v**2))

x = np.array([-2, 5, 0, 7, 10])         # Define a vector
print("Vector:", x)
print("Mean:", np.mean(x))              # Compute Average (Mean)
print("Standard Deviation:", np.std(x)) # Compute Standard Deviation
print("RMS:", rms(x))                   # Compute Root Mean Square (RMS)
