import numpy as np
from sklearn.metrics import confusion_matrix as errors #true neg, false pos, false neg, true pos

boolean = lambda b : 2*int(b)-1
def cross_validate_boolean(X,y,folds=5):
    m,n = X.shape
    Y = np.array([boolean(b) for b in y])
    partition = np.array_split(np.random.permutation(m),folds)
    c = np.zeros((folds,n))
    training_matrix = np.zeros((folds,2,2)) 
    test_matrix = np.zeros((folds,2,2)) 
    for k in range(folds):
        test_index = partition[k]
        training_index = np.concatenate(partition[:k]+partition[k+1:])
        a = np.linalg.lstsq(X[training_index],Y[training_index],rcond=None)[0]
        c[k,:] = a
        training_matrix[k] = errors(Y[training_index],[boolean(a @ x > 0) for x in X[training_index]])
        test_matrix[k] = errors(Y[test_index], [boolean(a @ x > 0) for x in X[test_index]])  
    return c,training_matrix,test_matrix

from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
# # uncomment lines 25-28 to see the data set
# # or view the whole data set at https://github.com/emisseldine/OpenLinear/blob/main/data/WI_breast_cancer
# print(cancer.feature_names) # 30 attributes
# print(cancer.data)          #569 x 30 attribute matrix
# print(cancer.target_names)  # 2 targets
# print(cancer.target)        # 569-vector Boolean vector: 0 for malignant, 1 for benign

N  = len(cancer.data)

X = # write your matrix/model here
  # you might need to experiment with different models to get your prediction error down
  # make sure to include a constant coefficient on your model, which will be the last column of X
coeffs,train_mtxs,test_mtxs = cross_validate_boolean(X, cancer.target)

### VERIFICATION #####
coeff = np.mean(coeffs.T,axis=1)
train_mtx = np.mean(train_mtxs,axis=0)
test_mtx = np.mean(test_mtxs,axis=0)
print(f"Training Error: {round(100*(1-np.trace(train_mtx)/sum(sum(train_mtx))),2)}%")
print(f"Test Error: {round(100*(1-np.trace(test_mtx)/sum(sum(test_mtx))),2)}%")

# The Classifer
IsBenign = lambda patient : cancer.target_names[int(np.concatenate((patient,[1])) @ coeff>0)]

patient = np.array([ 17.99, 10.38, 122.8, 1001.0, 0.1184, 0.2776, 0.3001, 0.1471, 0.2419, 0.07871, 1.095, 0.9053, 8.589, 153.4, 0.006399, 0.04904, 0.05373, 0.01587, 0.03003, 0.006193, 25.38, 17.33, 184.6, 2019.0, 0.1622, 0.6656, 0.7119, 0.2654, 0.4601, 0.1189])
print(IsBenign(patient))

patient = np.array([ 8.618, 11.79, 54.34, 224.5, 0.09752, 0.05272, 0.02061, 0.007799, 0.1683, 0.07187, 0.1559, 0.5796, 1.046, 8.322, 0.01011, 0.01055, 0.01981, 0.005742, 0.0209, 0.002788, 9.507, 15.4, 59.9, 274.9, 0.1733, 0.1239, 0.1168, 0.04419, 0.322, 0.09026])
print(IsBenign(patient))
