import numpy as np
import matplotlib.pyplot as plt
import logging
import sys


'''
X = ['ponedjeljak', 'utorak', 'srijeda', 'četvrtak', 'petak']
Y = [10, 15, 6, 7, 22]

plt.pie(Y, labels=X, autopct='%1.2f%%', explode=(0, 0, 0.1, 0, 0))
plt.axis('equal')
plt.savefig('piechart.png')
plt.show()

X1 = ['A', 'B', 'C']
Y1 = [np.random for i in range(50)]
'''

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

k=100
plt.plot([i for i in range(k)], [np.random.randint(0,1000) for i in range(k)], label="šum")
plt.plot([i for i in range(k)], [1000-np.random.randint(0,1000) for i in range(k)], label="šum2")
plt.plot([i for i in range(k)], [np.random.randint(0,1000)/2 for i in range(k)], label="šum3")
plt.plot([i for i in range(k)], [np.random.randint(0,1000)/2+500 for i in range(k)], label="šum4")
plt.plot([i for i in range(k)], [500 for i in range(k)], label="crta")


plt.legend(loc='best')
plt.show()