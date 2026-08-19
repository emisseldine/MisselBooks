#matplotlib, as the name suggests, is a library designed for plotting mathematical 
    #functions. From time to time, we will need to use it to create graphics.
    #Please see the appendix on matplotlib for further details.
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-whitegrid')

import numpy as np
from sklearn.cluster import KMeans

k = 4  	  #the number of clusters to be formed in the partition

plt.ion() #interactive mode will be on
    	    #figures will automatically be shown
#X is a set of 1000 2-vectors randomly generated using methods within 
#the random sublibrary of NumPy.	
X = np.concatenate([[0.3*np.random.randn(2) for i in range(100)], 
                    [[0,1] + 0.5*np.random.randn(2) for i in range(100)], 
                    [[1,1] + 0.4* np.random.randn(2) for i in range(100)],
                    [[1,-1] + 0.3* np.random.randn(2) for i in range(100)],
                    [[-0.5,1] + 0.25* np.random.randn(2) for i in range(100)],
                    [[0.5,-1] + 0.1* np.random.randn(2) for i in range(100)],
                    [[0.5,-0.5] + 0.3* np.random.randn(2) for i in range(100)],
                    [[1,-0.25] + 0.25* np.random.randn(2) for i in range(100)],
                    [[1.75,-0.75] + 0.2* np.random.randn(2) for i in range(100)],
                    [[1,0] + 0.5* np.random.randn(2) for i in range(100)]])

#The following code formats the scatterplot of X w/o clustering.
x = np.linspace(-2, 3, 10)  #Used to create an evenly spaced sequence in the 
                            #interval (-2 to 3). There will be (10) spaces.
plt.xlim(-2,3)              #Sets the x-axis boundaries for the graph
plt.ylim(-2,3)              #Sets the y-axis boundaries for the graph
plt.scatter( X[:,0],X[:,1]) #Plots all the vectors in X
plt.show()                  #Displays all open figures

#The k-means algorithm takes the number of clusters k and a random state,
    #which randomizes the initial representatives
kmeans = KMeans(n_clusters=k, random_state=0).fit(X) 
labels = kmeans.labels_        #the cluster assignment vector
reps = kmeans.cluster_centers_ #the cluster representatives
J_clust = kmeans.inertia_      #the cluster objective
print(J_clust)

#formatting and creation of second scatterplot
#grps is the creation of the actual clustering of vectors for the purposes of coloring 
    #the scatterplot.
grps = [[X[i,:] for i in range(len(X)) if labels[i]==j] for j in range(k)]
for i in range(k):
    plt.scatter([c[0] for c in grps[i]],[c[1] for c in grps[i]])
plt.scatter([z[0] for z in reps],[z[1] for z in reps],c='black',marker='x',s=50)
plt.xlim(-2,3)
plt.ylim(-2,3)
plt.show()
