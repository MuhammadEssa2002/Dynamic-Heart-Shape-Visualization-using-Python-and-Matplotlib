import numpy as np
import matplotlib.pyplot as plt

# Heart shape function
def heart(x):
    return np.sqrt(x**2)-np.sqrt(9.3-x**2)*np.sin(15*np.pi*x)


n=600
da = []
arr = np.linspace(-3,3,n)
plt.ion()
for i in range(len(arr)):
    da.append(arr[i])
    data = np.array(da)
    plt.plot(data,heart(data),color='red')
    plt.ylim(-3.5,4.5)
    plt.xlim(-3.5,3.5)
    plt.title("Heart Shape")
    plt.xlabel("X-Axis")
    plt.ylabel("y = sqrt(x^2)-sqrt(9.3-x^2)*sin(15*pi*x)")
    plt.scatter(data,heart(data), cmap='viridis',c = heart(data))
    plt.pause(0.000001)
    plt.draw()
    plt.clf()
    plt.show()
    
plt.ioff()
plt.plot(arr,heart(arr),color='red')
plt.title("Heart Shape")
plt.xlabel("X-Axis")
plt.ylabel("y = sqrt(x^2)-sqrt(9.3-x^2)*sin(15*pi*x)")
plt.ylim(-3.5,4.5)
plt.xlim(-3.5,3.5)
plt.scatter(arr,heart(arr), cmap='viridis',c = heart(arr))
plt.show()