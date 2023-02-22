#Marlo Emiliano Muktiono 2006570315 21/02/23
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10,100)

def FungsiY(x,n,a,b) :
    y = a*(x**n) + b
    return y

#Sumbu x dan y di letakan di tengah
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.plot(x, FungsiY(x,1,3,4), label = 'y=3x+4')
plt.plot(x, FungsiY(x,2,2,1), label = 'y=2x^2+1')
plt.plot(x, FungsiY(x,3,1,3), label = 'y=x^3+3')
plt.title('HW01 no6')
plt.ylim(-10,10)
plt.xlim(-5,5)
plt.show()