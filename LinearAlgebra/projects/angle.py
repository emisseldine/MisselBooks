import numpy as np

### TASK 1 ###################
angle = lambda u, v : #write your formula here

u = np.array([6,-1])
v = np.array([1,4])
print(angle(u,v), angle(u,v)*180/np.pi)

### TASK 2 ###################
CC= np.array([37.6775, -113.0619]) #Cedar City
Pusan = np.array([35.2100, 129.0689]) #Pusan, South Korea

r = 6367.5 #Radius of Earth in km

#converts latitude/longitude coordinates into a vector in R^3
convert_coord = lambda coords, radius : np.array([radius*np.sin(coords[1]*np.pi/180)*np.cos(coords[0]*np.pi/180), 
              radius*np.cos(coords[1]*np.pi/180)*np.cos(coords[0]*np.pi/180), 
              radius*np.sin(coords[0]*np.pi/180)])

CC_vec = #write the convert coordinates of Cedar City here
Pusan_vec = #write the convert coordinates of Pusan here
angle_CP = #compute the angle between the cities here
print(r*angle_CP) 
