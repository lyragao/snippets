import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math 

# animate pie chart that has 4 components

labels = ["hello",
         "i",
         "am",
         "piechart"]
colors = ["#3d85c6",
         "#FFA500",
         "#b6d7a8",
         "#6aa84f"]

revshares = [[37, 24, 22, 17], 
             [35, 25, 23, 17],
             [36, 23, 25, 16],
             [37, 23, 25, 16]]
revshares = np.array(revshares)

z = np.array([0,0,0,0]).astype(np.float)
year = 2018

fig, ax = plt.subplots()

def update(num):
    
    global z
    
    ax.clear()
    ax.axis('equal')     
    z += revshares[num]  
    pie = ax.pie(z, labels=labels, colors=colors, 
                 autopct='%1.1f%%', shadow=False, startangle=140)
    ax.set_title(math.floor(2016 + sum(z)/100))   
    
ani = animation.FuncAnimation(fig, update, frames=range(4), repeat=False)
ani.save('revshare.gif', writer='pillow', fps=1)
