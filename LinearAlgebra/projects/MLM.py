import numpy as np

ranking = lambda names, scores : np.array(names)[np.argsort(-scores)] #A function to sort the names of mathletes by their scores.
        
names = ["Pete Weyl", "Karla Gauss", "Hermie Wielandt", "Artie Cayley", "Emmy Noether", 
"Evie Galois", "Rowan \"Quaternion\" Hamilton", "Dave Hilbert", "Sophie Lie", "Jorge Frobenius", 
"Izzy Schur", "Stevie Humphries", "Mikey Muzychuk", "Manny Leung", "Ollie Tamaschke"]

X = np.array([[11,  9, 10, 13, 30], #Pete Weyl
               [ 7, 17, 10,  1, 11],#Karla Gauss
               [26, 22, 11, 22, 10],#Hermie Wielandt
               [13, 25,  7,  1, 13],#Artie Cayley
               [13, 9, 18, 14, 5],  #Emmy Noether
               [ 4, 14, 10, 25,  0],#Evie Galois
               [ 9, 21, 8, 22, 19], #Rowan "Quaternion" Hamilton
               [30, 14,  7, 24, 16],#Dave Hilbert
               [ 3,  7, 18,  5, 11],#Sophie Lie
               [28, 11, 25,  9, 20],#Jorge Frobenius
               [27, 11, 29,  2, 13],#Izzy Schur
               [ 7, 4, 10, 12, 10], #Stevie Humphries
               [14,  2,  5,  4, 2], #Mikey Muzychuk
               [ 5,  2, 11, 10, 10],#Manny Leung
               [ 3, 19, 14, 19, 9]])#Ollie Tamaschke

### TASK 1 #####################
p = (5,4,3,2,1)
scores = #write your code here to compute scores.
winners = ranking(names, scores)
for i in range(len(names)):
    print(scores[names.index(winners[i])], winners[i])
print("\n")

### TASK 2 #####################
p = (7,4,3,1,1)
scores = #write your code here to compute scores.
winners = ranking(names, scores)
for i in range(len(names)):
    print(scores[names.index(winners[i])], winners[i])
print("\n")

#Compare this ranking to the official ranking you computed above. 
#What significant differences do you observe? 
#Why did they change?  
print()

### TASK 3 #####################
p = #Create two other point vectors to result in two other 
#different MVP winners (not including the two winners from the 
#two previous vectors).
scores = #write your code here to compute scores.
winners = ranking(names, scores)
for i in range(len(names)):
    print(scores[names.index(winners[i])], winners[i])
print("\n")

p = #Create two other point vectors to result in two other 
#different MVP winners (not including the two winners from the 
#two previous vectors).
scores = #write your code here to compute scores.
winners = ranking(names, scores)
for i in range(len(names)):
    print(scores[names.index(winners[i])], winners[i])
print("\n")

#Is there a point vector for which Manny Leung does not get last place?
print()
