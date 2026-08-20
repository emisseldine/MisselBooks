import numpy as np

def lstsq_constraint(A, b, C, d):
    ATA = A.T @ A
    CT = (C.T).reshape((len(ATA), -1))
    n = len(CT[0])
    KKT = np.block([[2*ATA, CT], [CT.T, np.zeros((n, n))]])
    KKTb = np.hstack((2*A.T @ b, d))
    return np.linalg.lstsq(KKT, KKTb, rcond=None)[0][:-n]

V = np.array([[0.97,1.86,0.41], 
              [1.23,2.18,0.53], 
              [0.80,1.24,0.62], 
              [1.29,0.98,0.51], 
              [1.10,1.23,0.69], 
              [0.67,0.34,0.54], 
              [0.87,0.26,0.62], 
              [1.10,0.16,0.48], 
              [1.92,0.22,0.71], 
              [1.29,0.12,0.62]])
t = 1000*np.ones(10) #target impressions
B = 1284 #Budget

print("Target Impressions in each Demographic Group =\n", t, "\n")

c = np.linalg.lstsq(V,t, rcond=None)[0]
print("No Budget: Cost = $" + str(round(sum(c),2))+"\n")
print("Spending in each Channel = $", [round(cost,2) for cost in c], "\n")
print("Expected Impressions in each Demographic Group =\n", [int(round(impress, 0)) for impress in V@c], "\n")
print("Relative RMS Error = " + str(round(100*(np.linalg.norm(V@c - t)/np.linalg.norm(t)),2)) + "%\n\n")

c = lstsq_constraint(V, t, np.ones(3), B)
print("Fixed Budget: Cost = $" + str(B) +"\n")
print("Spending in each Channel = $", [round(cost,2) for cost in c], "\n")
print("Expected Impressions in each Demographic Group =\n", [int(round(impress, 0)) for impress in V@c], "\n")
print("Relative RMS Error = " + str(round(100*(np.linalg.norm(V@c - t)/np.linalg.norm(t)),2)) + "%")
