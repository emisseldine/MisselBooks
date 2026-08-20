import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# PART A: Birth of LinearMax
# ==========================================
# The Transition Matrix A
# Column 0: Transitions FROM PyFlix
# Column 1: Transitions FROM LinearMax
A = np.array([
    [0.70, 0.20],  # TO PyFlix
    [0.30, 0.80]   # TO LinearMax
    ])

# Initial State vector x_0 (Start of first year)
# 1000K subscribers for PyFlix, 0 for LinearMax
x = np.array([1000, 0])

# Calculate eigenvalues to predict behavior before running simulation
print('Birth of LinearMax - Eigenvalues of Transition Matrix:', np.linalg.eigvals(A), '\n', '-' * 30)

# Run simulation
T = 24
pf = [x[0]]
lm = [x[1]]

for t in range(T):
    x = A @ x  
    pf.append(x[0])
    lm.append(x[1])

# Plot 1: Stabilization (Convergence to Steady State)
plt.figure(figsize=(10, 6))
plt.plot(range(T + 1), pf, label='PyFlix', marker='o', linewidth=2, color='tab:blue')
plt.plot(range(T + 1), lm, label='LinearMax', marker='x', linewidth=2, color='tab:orange')

plt.title('Part A - Market Share Stability: Birth of LinearMax', fontsize=14,fontweight='bold')
plt.xlabel('Months', fontsize=12)
plt.ylabel('Thousands of Subscribers', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.text(T/2, 650, 
         'The lines flatten out (Steady State)\nbecause one eigenvalue is ' + r'$\lambda=1.$', 
         bbox=dict(facecolor='yellow', alpha=0.2))
plt.show()

# ==========================================
# PART B: Customer Referrals
# ==========================================
# The Transition Matrix A_ref
# Column 0: Transitions FROM PyFlix
# Column 1: Transitions FROM LinearMax
A_ref = np.array([
    [0.9, 0.25],  # TO PyFlix
    [0.30, 0.70]   # TO LinearMax
    ])

# Calculate eigenvalues to predict behavior before running simulation
print('Customer Referrals - Eigenvalues of Transition Matrix:', np.linalg.eigvals(A_ref), '\n', '-' * 30)

# Run simulation
# Initial State vector x_25 (start of 3rd year)
# approximately 400K subscribers for PyFlix, 600K for LinearMax
T_ref = 24
pf_ref = [x[0]]
lm_ref = [x[1]]

for t in range(T_ref):
    x = A_ref @ x  
    pf_ref.append(x[0])
    lm_ref.append(x[1])

# ==========================================
# PART C: Death of Quantitative Literacy
# ==========================================
# The Transition Matrix A_ql
# Column 0: Transitions FROM PyFlix
# Column 1: Transitions FROM LinearMax
A_ql = np.array([
    [0.75, 0.05],  # TO PyFlix
    [0.10, 0.65]   # TO LinearMax
    ])

# Calculate eigenvalues to predict behavior before running simulation
print('Death of QL - Eigenvalues of Transition Matrix:', np.linalg.eigvals(A_ql), '\n', '-' * 30)

# Run simulation
# Initial State vector x_25 (start of 3rd year)
# approximately 400K subscribers for PyFlix, 600K for LinearMax
T_ql = 24
pf_ql = [x[0]]
lm_ql = [x[1]]

for t in range(T_ql):
    x = A_ql @ x  
    pf_ql.append(x[0])
    lm_ql.append(x[1])

# --- Visualize Parts B and C ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Plot 2: Growth (Divergence)
ax1.plot(range(T_ref + 1), pf_ref, label='PyFlix', marker='o', linewidth=2, color='tab:blue')
ax1.plot(range(T_ref + 1), lm_ref, label='LinearMax', marker='x', linewidth=2, color='tab:orange')
ax1.set_title('Part B - Market Explosion: Customer Referrals', fontsize=14, fontweight='bold')
ax1.set_xlabel('Months', fontsize=12)
ax1.set_ylabel('Thousands of Subscribers', fontsize=12)
ax1.grid(True, alpha=0.3)
ax1.legend()

# Plot 3: Decay (Convergence to Zero)
ax2.plot(range(T_ql + 1), pf_ql, label='PyFlix', marker='o', linewidth=2, color='tab:blue')
ax2.plot(range(T_ql + 1), lm_ql, label='LinearMax', marker='x', linewidth=2, color='tab:orange')
ax2.set_title('Part C - Market Collapse: Death of QL', fontsize=14, fontweight='bold')
ax2.set_xlabel('Months', fontsize=12)
ax2.set_ylabel('Thousands of Subscribers', fontsize=12)
ax2.grid(True, alpha=0.3)
ax2.legend()

plt.tight_layout()
plt.show()
