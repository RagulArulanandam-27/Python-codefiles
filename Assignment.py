import numpy as np
import matplotlib.pyplot as plt

# Mandelbrot Set

def mandelbrot(c, max_iter, k):
    z = 0
    for i in range(max_iter):
        z = z**k + c
        if abs(z) > 2:
            return i
    return max_iter

def plot_mandelbrot(k, max_iter=100, resolution=500):
    x_min, x_max, y_min, y_max = -2, 2, -2, 2
    x_vals = np.linspace(x_min, x_max, resolution)
    y_vals = np.linspace(y_min, y_max, resolution)
    
    mandelbrot_set = np.zeros((resolution, resolution))
    for i, x in enumerate(x_vals):
        for j, y in enumerate(y_vals):
            c = complex(x, y)
            mandelbrot_set[j, i] = mandelbrot(c, max_iter, k)
    
    plt.figure(figsize=(8, 8))
    plt.imshow(mandelbrot_set, extent=(x_min, x_max, y_min, y_max), cmap='hot')
    plt.colorbar()
    plt.title(f'Mandelbrot Set for k={k}')
    plt.show()

plot_mandelbrot(2)
plot_mandelbrot(4)

# Julia Set

def julia(z, c, max_iter):
    for i in range(max_iter):
        z = z**2 + c
        if abs(z) > 2:
            return i
    return max_iter

def plot_julia(c, max_iter=100, resolution=500):
    x_min, x_max, y_min, y_max = -2, 2, -2, 2
    x_vals = np.linspace(x_min, x_max, resolution)
    y_vals = np.linspace(y_min, y_max, resolution)
    
    julia_set = np.zeros((resolution, resolution))
    for i, x in enumerate(x_vals):
        for j, y in enumerate(y_vals):
            z = complex(x, y)
            julia_set[j, i] = julia(z, c, max_iter)
    
    plt.figure(figsize=(8, 8))
    plt.imshow(julia_set, extent=(x_min, x_max, y_min, y_max), cmap='hot')
    plt.colorbar()
    plt.title(f'Julia Set for c={c}')
    plt.show()

plot_julia(complex(-0.5, -0.66))
plot_julia(complex(-0.70576, -0.3842))

# Infection Model

def infection_model(p0, k, steps=20):
    p_values = [p0]
    for t in range(steps):
        pt = p_values[-1]
        new_p = pt + k * pt * (1 - pt)
        p_values.append(new_p)
    return p_values

def plot_infection():
    p_values = [0.1, 0.2, 0.3]
    k_values = np.arange(1, 4.25, 0.25)
    
    plt.figure(figsize=(10, 6))
    for p in p_values:
        for k in k_values:
            infection_curve = infection_model(p, k)
            plt.plot(infection_curve, label=f'p0={p}, k={k}')
    
    plt.xlabel('Time steps')
    plt.ylabel('Proportion Infected')
    plt.title('Infection Spread Model')
    plt.legend()
    plt.show()
    plt.close()

plot_infection()

