import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread as img
import urllib.request

#import image
url = r'https://raw.githubusercontent.com/emisseldine/OpenLinear/main/Chapter6/images/Bell_Tower.jpg'
bell = np.asarray(img(urllib.request.urlopen(url),'jpg'))[:,:,0] #change 'jpg' based upon the file type of image
color = 'gist_heat'                                              #select a color map

# processing image
plt.figure(figsize=(9,6))
plt.imshow(bell,cmap=color)
plt.axis('off')
plt.show()
print(bell.shape,np.linalg.matrix_rank(bell))
#%%
U,sigma,VT = np.linalg.svd(bell)

reduced_svd = lambda U,sigma,VT,k : U[:,:k] @ np.diag(sigma[:k]) @ VT[:k,:]
#%%
num_vals = np.concatenate((np.arange(1,5),
                           np.arange(5,50,5),
                           np.arange(50,525,25),
                           np.arange(1000,3000,500),
                           [len(sigma)]))
for k in num_vals:
    bell_blur = reduced_svd(U,sigma,VT,k)
    plt.figure(figsize=(9,6))
    plt.imshow(bell_blur,cmap=color)
    plt.title(f"k = {k}")
    plt.axis('off')
    plt.show()
