
# Heart Shape Plot with Python

This script visualizes a dynamic heart shape using NumPy and Matplotlib.

## Requirements

Before running the code, make sure you have the following Python libraries installed:

- `numpy`
- `matplotlib`

You can install them using:

```bash
pip install numpy matplotlib
```

## Code

```python
import numpy as np
import matplotlib.pyplot as plt

# Heart shape function
def heart(x):
    return np.sqrt(x**2)-np.sqrt(9.3-x**2)*np.sin(15*np.pi*x)

n = 600
da = []
arr = np.linspace(-3, 3, n)

plt.ion()  # Turn on interactive mode

for i in range(len(arr)):
    da.append(arr[i])
    data = np.array(da)
    plt.plot(data, heart(data), color='red')
    plt.ylim(-3.5, 4.5)
    plt.xlim(-3.5, 3.5)
    plt.title("Heart Shape")
    plt.xlabel("X-Axis")
    plt.ylabel("y = sqrt(x^2)-sqrt(9.3-x^2)*sin(15*pi*x)")
    plt.scatter(data, heart(data), cmap='viridis', c=heart(data))
    plt.pause(0.000001)
    plt.draw()
    plt.clf()
    plt.show()

plt.ioff()  # Turn off interactive mode
plt.plot(arr, heart(arr), color='red')
plt.title("Heart Shape")
plt.xlabel("X-Axis")
plt.ylabel("y = sqrt(x^2)-sqrt(9.3-x^2)*sin(15*pi*x)")
plt.ylim(-3.5, 4.5)
plt.xlim(-3.5, 3.5)
plt.scatter(arr, heart(arr), cmap='viridis', c=heart(arr))
plt.show()
```

## Explanation

1. **Heart Function**: This function generates the values for the heart shape curve. It uses trigonometric and square root functions.
   
    ```python
    def heart(x):
        return np.sqrt(x**2) - np.sqrt(9.3 - x**2) * np.sin(15 * np.pi * x)
    ```

2. **Plotting the Dynamic Heart**: We use `plt.ion()` for interactive plotting and a loop to plot the heart shape as it builds incrementally.
   
3. **Final Static Plot**: After finishing the dynamic plotting, `plt.ioff()` turns off interactive mode, and the final heart shape is plotted statically.

## Output

The output is a heart-shaped curve plotted dynamically and then statically displayed at the end.

Happy coding! ❤️
