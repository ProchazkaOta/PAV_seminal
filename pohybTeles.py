# IMPORT
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML

# POCATECNI PODMINKY
hmotnost_slunce = 333000 # Me (v jednotkach hmotnosti zeme)
polomer_slunce = 0.0004*150000000 # AU (astronomicka jednotka) na km
hmotnost_asteroidu = 2e-25 # Me
prumer_asteroidu = 1 # km

print(hmotnost_slunce)

fig, ax = plt.subplots()



ax.scatter(0, 0, marker="*", c="orange", s=1000)
ax.scatter(0, 1, marker="o", c="black", s=100)
#plt.show()



#ax.set_xlim(( 0, 2))
#ax.set_ylim((-2, 2))
#ax.grid()

print("only a test")

plt.show()
