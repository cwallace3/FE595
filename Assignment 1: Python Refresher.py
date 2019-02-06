# Claude Wallace 
#FE 595 - Financial Systems Technology
# Assignment 1: Python Refresher 


import matplotlib.pyplot as plt
import numpy as np


# x-axis values from 0 to 2π (one period)
x = np.linspace(0 ,2*np.pi) #np.linspace(start, stop, number within the range)

# Calculate sine and cosine values
y = np.sin(x)
z = np.cos(x)

# Plot sine and cosine graphs on same set of axes
plt.plot(x,y, color="red", label= "sine")

plt.plot(x,z, color="blue", label= "cosine")

# Graph title and legend
plt.title('Sine and Cosine Graph')
plt.legend()


# x- and y- axis labels
plt.xlabel('Phase (radians)')
plt.ylabel('Amplitude')

# Add a horizontal line across the x-axis
plt.axhline(y = 0, color='k')

# Add grid lines
plt.grid(color='black', linestyle='-', linewidth=0.2)

# Label the x-axis tick locations 
plt.xticks((0,np.pi/2,np.pi,np.pi*3/2,np.pi*2),('0','π/2','π','3π/2','2π'))

