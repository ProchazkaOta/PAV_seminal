# IMPORT
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML

# POCATECNI PODMINKY
mS = 333000 # Me (v jednotkach hmotnosti zeme)
dS = 0.0004*150000000 # AU (astronomicka jednotka) na km
m1 = 2e-25 # Me
d1 = 1 # km
G = 6.674e-11 # m3.kg-1.s-2

xS = 0
yS = 0
vxS = 0
vyS = 0
x1 = 2e8
y1 = 0
vx1 = 0
vy1 = -2e5

A = np.array([[xS, yS, vxS, vyS], [x1, y1, vx1, vy1]])
M = np.array([mS, m1])

def dist( D ):
    ((D[0,0]-D[1,0])**2 + (D[0,1]-D[1,1])**2)
    
    return;

print(A[0,0]-A[1,0])

print(A)
print(A[:,0])
#F = G*(M[0]*M[1])/(A[0,0]-A[0,1])
print(F)

print(mS)

fig, ax = plt.subplots()



ax.scatter(0, 0, marker="*", c="orange", s=1000)
ax.scatter(0, 1, marker="o", c="black", s=100)
#plt.show()



#ax.set_xlim(( 0, 2))
#ax.set_ylim((-2, 2))
#ax.grid()

plt.show()
