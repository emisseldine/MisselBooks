import numpy as np

def lstsq_constraint(A, b, C, d):
    ATA = A.T @ A
    CT = (C.T).reshape((len(ATA), -1))
    n = len(CT[0])
    KKT = np.block([[2*ATA, CT], [CT.T, np.zeros((n, n))]])
    KKTb = np.hstack((2*A.T @ b, d))
    return np.linalg.lstsq(KKT, KKTb, rcond=None)[0][:-n]

V = np.array([[2.0,1.1,0.1,3.2],
              [1.2,2.2,1.3,0.2],
              [0.5,1.0,3.1,2.7],
              [3.1,0.4,2.4,1.2],
              [1.1,1.1,2.2,2.3]])
t = 600*np.ones(5) #target impressions
B = 375 #Budget

print("Target Impressions in each Demographic Group =\n", t, "\n")

c = np.linalg.lstsq(V,t, rcond=None)[0]
print("No Budget: Cost = $" + str(round(sum(c),2))+"\n")
print("Spending in each Channel = $", [round(cost,2) for cost in c], "\n")
print("Expected Impressions in each Demographic Group =\n", [int(round(impress, 0)) for impress in V@c], "\n")
print("Relative RMS Error = " + str(round(100*(np.linalg.norm(V@c - t)/np.linalg.norm(t)),2)) + "%\n\n")

c = lstsq_constraint(V, t, np.ones(4), B)
print("Fixed Budget: Cost = $" + str(B) +"\n")
print("Spending in each Channel = $", [round(cost,2) for cost in c], "\n")
print("Expected Impressions in each Demographic Group =\n", [int(round(impress, 0)) for impress in V@c], "\n")
print("Relative RMS Error = " + str(round(100*(np.linalg.norm(V@c - t)/np.linalg.norm(t)),2)) + "%")
