import numpy as np
from sklearn.metrics import confusion_matrix as errors 

boolean = lambda b : 2*int(b)-1

def cross_validate_boolean(X,y,folds=5):
    m,n = X.shape
    partition = np.array_split(np.random.permutation(m),folds)
    c = np.zeros((folds,n))
    training_matrix = np.zeros((folds,2,2)) 
    test_matrix = np.zeros((folds,2,2)) 
    for k in range(folds):
        test_index = partition[k]
        training_index = np.concatenate(partition[:k]+partition[k+1:])
        a = np.linalg.lstsq(X[training_index],y[training_index],rcond=None)[0]
        c[k,:] = a
        training_matrix[k] = errors(y[training_index],[boolean(a @ x > 0) for x in X[training_index]])
        test_matrix[k] = errors(y[test_index], [boolean(a @ x > 0) for x in X[test_index]])  
    return c,training_matrix,test_matrix

###################### IRIS EXAMPLE ##################################################
from sklearn.datasets import load_iris
iris_types = load_iris()['target']
iris_data = np.array(load_iris()['data'])

n = len(iris_types)
X = np.column_stack([iris_data, np.ones(n)])

IsVirginica = np.array([boolean(iris == 2) for iris in iris_types])

coeff, training_matrix, test_matrix = cross_validate_boolean(X,IsVirginica)

model = "+".join([str(round(np.mean(coeff[:,i]),4)) + "x_" + str(i+1) for i in range(5)])
print("y = " + model[:-3] + "\n")

print("Training Confusion Matrix\n", training_matrix)
print("\nTest Confusion Matrix\n", test_matrix)

accuracy =  np.array([[(training_matrix[j,0,0]+training_matrix[j,1,1])/sum(sum(training_matrix[j])),(test_matrix[j,0,0]+test_matrix[j,1,1])/sum(sum(test_matrix[j]))] for j in range(5)])
print("\nAccuracy = ( ( true pos + true neg ) / total )  [training, test]\n", 
      accuracy, "\n\n", sum(accuracy)/5, "\n\n")

specificity = np.array([[training_matrix[j,0,0]/(training_matrix[j,0,0]+training_matrix[j,0,1]),test_matrix[j,0,0]/(test_matrix[j,0,0]+test_matrix[j,0,1])] for j in range(5)])    
print("\nSpecificity = ( true neg / actual neg )  [training, test]\n", 
      specificity, "\n\n", sum(specificity)/5, "\n\n")

recall = np.array([[training_matrix[j,1,1]/(training_matrix[j,1,0]+training_matrix[j,1,1]),test_matrix[j,1,1]/(test_matrix[j,1,0]+test_matrix[j,1,1])] for j in range(5)])
print("\nSensitivity/Recall = ( true pos / actual pos )  [training, test]\n", 
      recall, "\n\n", sum(recall)/5, "\n\n")

precision = np.array([[training_matrix[j,1,1]/(training_matrix[j,0,1]+training_matrix[j,1,1]),test_matrix[j,1,1]/(test_matrix[j,0,1]+test_matrix[j,1,1])] for j in range(5)])
print("\nPrecision = ( true pos / predict pos )  [training, test]\n", 
      precision, "\n\n", sum(precision)/5, "\n\n")
