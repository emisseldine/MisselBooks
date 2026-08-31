import numpy as np
from sklearn.metrics import confusion_matrix as errors

boolean = lambda b : 2*int(b)-1
def cross_validate_multiclass(X,y,p=2,folds=5):
    m,n = X.shape
    partition = np.array_split(np.random.permutation(m),folds)
    c = np.zeros((p,folds,n))
    training_matrix = np.zeros((folds,p,p)) 
    test_matrix = np.zeros((folds,p,p))
    IsType = np.array([np.array([boolean(yi == j) for yi in y]) for j in range(p)])
    for k in range(folds):
        test_index = partition[k]
        training_index = np.concatenate(partition[:k]+partition[k+1:])
        for j in range(p):
            a = np.linalg.lstsq(X[training_index],IsType[j,training_index],rcond=None)[0]
            c[j,k,:] = a 
        training_matrix[k] = errors(y[training_index], [np.argmax([c[j,k] @ x for j in range(p)]) for x in X[training_index]])
        test_matrix[k] = errors(y[test_index], [np.argmax([c[j,k] @ x for j in range(p)]) for x in X[test_index]])
    return c,training_matrix,test_matrix

from sklearn.datasets import load_wine
wine = load_wine()
# # uncomment lines 26-29 to see the data set
# # or view the whole data set at https://github.com/emisseldine/OpenLinear/blob/main/data/wine
# print(wine.feature_names) # 13 attributes
# print(wine.data)          #178 x 13 attribute matrix
# print(wine.target_names)  # 3 targets
# print(wine.target)        # 178-vector vector with entries 0, 1, 2

N = len(wine.data)
M = len(wine.target_names) 

### VERIFICATION #####
X = np.array([np.append(wine.data[i],[1]) for i in range(N)])
coeffs,train_mtxs,test_mtxs = cross_validate_multiclass(X,wine.target,M)
coeff = np.array([np.mean(coeffs[i].T,axis=1) for i in range(M)])
train_mtx = np.mean(train_mtxs,axis=0)
test_mtx = np.mean(test_mtxs,axis=0)
print(f"Training Error: {round(100*(1-np.trace(train_mtx)/sum(sum(train_mtx))),2)}%")
print(f"Test Error: {round(100*(1-np.trace(test_mtx)/sum(sum(test_mtx))),2)}%\n")

#%% Task 1 ##################
_,sigma,VT = #compute the PCA of the fine wine data wine = U @ Sigma @ V.T. Note that U will not be used in the PCA
print(sigma,"\n")

#%% Task 2 ##################
k = # which rank will make the PCA affine model (see X below) reliable below 10% error?
print(f"k = {k}")
PCA = #compute the rank-k PCA dimension reduction of the fine wine data
# print(PCA)

### VERIFICATION #####
X = np.array([np.append(PCA[i],[1]) for i in range(N)])
coeffs,train_mtxs,test_mtxs = cross_validate_multiclass(X,wine.target,M)
coeff = np.array([np.mean(coeffs[i].T,axis=1) for i in range(M)])
train_mtx = np.mean(train_mtxs,axis=0)
test_mtx = np.mean(test_mtxs,axis=0)
print(f"Training Error: {round(100*(1-np.trace(train_mtx)/sum(sum(train_mtx))),2)}%")
print(f"Test Error: {round(100*(1-np.trace(test_mtx)/sum(sum(test_mtx))),2)}%")
