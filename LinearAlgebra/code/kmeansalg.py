import numpy as np

def clustering_objective(data, clustering, reps):
    J_obj = 0                               #Initialize clustering objective
    for i in range(len(data)):              #for-loop going through all data vectors "data[i]"
        J_obj += np.linalg.norm(data[i] - reps[int(clustering[i])])**2 #Running total calculating the numerator of the clustering objective
    return J_obj/len(data)                  #the running total divided by the number of data gives the clustering objective


#inputs a set of data vectors "data" and a set of cluster representatives "reps"
#outputs a cluster assignment vector by identifying which representative is nearest to each data vector
def update_cluster(data,reps):
    new_clustering = np.zeros(len(data))    #Initialize cluster assignment vector
    for i in range(len(data)):              #for-loop running over the N data vectors: "data[i]"
        distance = np.zeros(len(reps))     #Initialize the vector of distances between the fixed vector "data[i]" with the cluster representatives 
        for j in range(len(reps)):          #for-loop running over the k cluster representatives: "reps[j]"
            distance[j] = np.linalg.norm(data[i] - reps[j])    #computes the distance between data vector "data[i]" and cluster representative "reps[j]"
        new_clustering[i] = np.argmin(distance)   #grabs the nearest neighbor
    return new_clustering
    
#inputs a set of data vectors "data" and a cluster assignment vector "clustering"
#outputs a new set of cluster representatives by replacing the current representatives with the mean of each of the clusters of vectors
def update_reps(data, clustering):
    new_reps = [];                          #Initialize the set of new representatives
    for j in range(int(max(clustering)+1)):   #for-loop running over the k cluster representatives
        sum = np.zeros(len(data[0]))        #Initialize a running sum of the vectors "data[i]" in cluster j
        count = 0                           #Initialize the size of cluster j
        for i in range(len(data)):          #for-loop running over the N data vectors: "data[i]"
            if clustering[i] == j:      #check to see if vector "data[i]" belongs to cluster j by referencing the assignment "clustering[i]"
                sum = sum+data[i]           #adds data from "data[i]" to running sum
                count += 1                  #increases count of cluster j by 1
        if count > 0:
            new_reps.append(sum/count)      #appends mean vector j to list of new representatives
    return np.array(new_reps)

#inputs a set of data vectors "data" and a set of cluster representatives "reps"
#"show_steps" is an optional parameter, which by default is False, which if toggled to True would show the steps of the algorithm
#outputs four quantities as explained below: 
#1st, the final set of representatives: "new_reps"
#2nd, the final partition: "clustering"
#3rd, the sequence of clustering objective for each iteration with the 0th index the initial objective: "J_obj"
#4th, the number of iterations to complete the algorithm
def Kmeans_alg(data, reps, show_steps=False):
    J_obj = []                      #Initialize the cluster objective sequence
    clustering = update_cluster(data, reps) #calculates the initial clustering assignment (to avoid an error when we lose a group 
    J_obj.append(clustering_objective(data, clustering, reps)) #calculates the initial clustering objective
    
    if show_steps:
        print("Iteration", len(J_obj)-1, ":\n (Update Cluster)")
        print("c = ", clustering)
        print(" Z = ", reps)
        print("J^clust = ", J_obj[-1], "\n")
    
    Stop = False        #Initialize the boolean for terminating the while loop
    while not(Stop):
        new_reps = update_reps(data, clustering)
        if show_steps:
            print("Iteration", len(J_obj), ":\n (Update Reps)")
            print(" Z = ", new_reps)
            
        clustering = update_cluster(data, new_reps)
        J_obj.append(clustering_objective(data, clustering, new_reps))
        if show_steps:
            print("(Update Cluster)")
            print("c = ", clustering)
            print("J^clust = ", J_obj[-1], "\n")
        Stop = (len(new_reps) == len(reps)) and (np.linalg.norm(np.array(new_reps) - np.array(reps)) < 1e-6)
           #checks to see if any clusters were lost #checks if change in reps is significant
        reps = new_reps                 #update reps for next iteration
            
    return new_reps, clustering, J_obj, len(J_obj)-1
    
    
X = np.array([ [1,2,3], [4,5,6], [1,2,0], [0,0,3], [ 3, 2, 1], [2,2,0], [0,5,0], [2,3,1], [6,6,4], [9,3,2], [2,3,4], [7,5,0], [ 2,7,8] ])
Z = np.array([ [1,0,0], [0,1,0], [0,0,1] ])

print(X, "\n")

final_Z, final_c, final_obj, final_it = Kmeans_alg(X,Z, show_steps=False)
print("Z = ", final_Z)
print("c = ", final_c)
print("J^clust = ", final_obj)
print("steps = ", final_it)
