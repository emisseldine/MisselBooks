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

X = # you might need to experiment with different models to get your prediction error down
    # make sure to include a constant coefficient on your model, which will be the last column of X
coeffs,train_mtxs,test_mtxs = cross_validate_multiclass(X,wine.target,M)

### VERIFICATION #####
coeff = np.array([np.mean(coeffs[i].T,axis=1) for i in range(M)])
train_mtx = np.mean(train_mtxs,axis=0)
test_mtx = np.mean(test_mtxs,axis=0)
print(f"Training Error: {round(100*(1-np.trace(train_mtx)/sum(sum(train_mtx))),2)}%")
print(f"Test Error: {round(100*(1-np.trace(test_mtx)/sum(sum(test_mtx))),2)}%")

WhichWine = lambda bottle : np.argmax([np.concatenate((bottle,[1])) @ coeff[i] for i in range(M)])

bottle = np.array([ 12.96, 3.45, 2.35, 18.5, 106.0, 1.39, 0.7, 0.4, 0.94, 5.28, 0.68, 1.75, 675.0])
print(WhichWine(bottle))

bottle = np.array([ 12.04, 4.3, 2.38, 22.0, 80.0, 2.1, 1.75, 0.42, 1.35, 2.6, 0.79, 2.57, 580.0])
print(WhichWine(bottle))
