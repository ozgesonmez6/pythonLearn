import matplotlib.pyplot as plt
import numpy as np
import os

# Tcl/Tk dizinini ayarlayın
os.environ['TCL_LIBRARY'] = r'C:\Users\Kamil\AppData\Local\Programs\Python\Python313\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Kamil\AppData\Local\Programs\Python\Python313\tcl\tk8.6'


x = np.array([0,12])
y = np.array([0,350])

plt.plot(x,y)
plt.show()