import numpy as np
import matplotlib.pyplot as plt

#cross validate the linear system Xc = y
def cross_validate(X,y,folds=5,display=False,label="Data",lower_x=0,upper_x=10,lower_y=0,upper_y=10):
    m,n = X.shape
    partition = np.array_split(np.random.permutation(m),folds)
    c = np.zeros((folds,n))
    training_error = np.zeros(folds)
    test_error = np.zeros(folds)
    for k in range(folds):
        test_index = partition[k]
        training_index = np.concatenate(partition[:k]+partition[k+1:])
        a = np.linalg.lstsq(X[training_index],y[training_index],rcond=None)[0]
        c[k,:] = a
        training_error[k] = np.linalg.norm(X[training_index] @ a - y[training_index])/np.linalg.norm(y[training_index])
        test_error[k] = np.linalg.norm(X[test_index] @ a - y[test_index])/np.linalg.norm(y[test_index])
        if display:
            plt.scatter(y[training_index], X[training_index] @ a, color='b', marker='o')
            plt.scatter(y[test_index], X[test_index] @ a, color='r', marker='x')
            plt.plot((lower_x,upper_x),(lower_y,upper_y) ,ls='--', c = 'r')
            plt.ylim(lower_y,upper_y)
            plt.xlim(lower_x,upper_x)
            plt.xlabel(f"Actual {label} (k= {str(k+1)})")
            plt.ylabel(f"Predicted {label}")
            plt.show()
    return c,training_error,test_error

#[class level (e.g. 1=freshmen, 2=sophmore, 3=junior, 4=senior), GPA, # of students, course evalulations]
data = np. array([[1,	2.54,	42, 	3.5],
        [1,	2.85,	33, 	4.4],
        [1,	2.92,	45, 	4.7],
        [1,	2.98,	36,	4.3],
        [1,	3.22,	6,	4.2],
        [1,	2.38,	33,	4.4],
        [1,	2.41,	26, 	4.6],
        [1,	2.57,	42,	4.4],
        [1,	2.89,	10, 	4.4],
        [1,	2.55,	42,	4.7],
        [1,	2.47,	42,	4.3],
        [1,	3.14,	50,	4.4],
        [1,	2.73,	39,	4.3],
        [1,	2.84,	46,	3.8],
        [1,	2.99,	14,	4.4],
        [2,	2.75,	33,	4.2],
        [1,	3.11,	15,	4.6],
        [1,	3.19,	12,	4.2],
        [1,	2.62,	43,	4.1],
        [1,	3.25,	42,	4.4],
        [2,	2.9,	25,	4.1],
        [4,	2.3,	9,	4.5],
        [1,	2.26,	46,	4.4],
        [2,	2.78,	30,	4.3],
        [3,	3.04,	12,	4.6],
        [1,	2.34,	19,	4.5],
        [1,	3.38,	30,	4.3],
        [1,	1.93,	42,	4.5],
        [1,	2.82,	37,	4.4],
        [4,	2.95,	14,	4.5],
        [1,	2.77,	41,	4.4],
        [1,	3.4,	45,	4.4],
        [3,	3.38,	8,	4.6],
        [4,	2.24,	7,	5],
        [1,	2.64,	22,	4.6],
        [1,	2.78,	5,	4.6],
        [1,	2.58,	44,	4],
        [1,	2.56,	42,	4.3],
        [2,	2.97,	30,	4.4],
        [2,	3.63,	20,	4.5],
        [1,	2.63,	37,	4.3],
        [1,	2.94,	45,	4.4],
        [3,	2.96,	9,	4.9],
        [4,	3.83,	6,	4.8]])

x = data[:,:3]
y = data[:,3]
N = len(x)

### TASK 1 #########
print("Task 1")
X = #create the matrix here to be solved in the least squares problem in line 83

coeff = np.linalg.lstsq(X,y,rcond=None)[0]
print(f"Coefficients = {coeff}\n")

Predict = lambda class_ : #write your predictor here

HypotheticalClass = np.array([2,3.00,8])
print(Predict(HypotheticalClass))

r = #Pearson Coefficient between y and y_hat
print(f"Pearson Coefficient = {r}\n")

### TASK 2 #########
print("Task 2")
coeffs,train,test = cross_validate(X,y)
coeff = np.mean(coeffs,axis=0)
print(f"Coefficients = {coeff}\n")

print("Thoughts? Analysis? How did it do?\n")

### TASK 3 #########
print("Task 3")

Xtreme = #feature engineer to improve the previous regression model X (line 81)

coeffs_Xtreme,train_Xtreme,test_Xtreme = cross_validate(Xtreme,y)
coeff_Xtreme = np.mean(coeffs_Xtreme,axis=0)
print(f"Coefficients = {coeff_Xtreme}\n")

print("Thoughts? Analysis? How did it compare? Improvements?\n")
