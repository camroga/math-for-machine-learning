import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D

# Define parameters
p = math.pi  # You can change the value of p to see different results

# Define x and y ranges
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

# Create a meshgrid for x and y
x, y = np.meshgrid(x, y)


# Define the parameters for the two mountains
# First Mountain (Peak at (-2, -2))
h1, k1 = -2, -2
a1, b1, c1 = 0.1, 0.1, 10  # Increase the height

# Second Mountain (Peak at (2, 2))
h2, k2 = 2, 2
a2, b2, c2 = 0.1, 0.1, 10  # Increase the height

# Define the equation for the two mountains
z1 = -(a1 * (x - h1)**2 + b1 * (y - k1)**2 + c1)
z2 = -(a2 * (x - h2)**2 + b2 * (y - k2)**2 + c2)
# Define the equation z = p * x^3 + x * y^2 + 2 * y^4
#z = p * x**3 + x * y**2 + 2 * y**4
# Combine the two mountains
#z = -(x**2 + y**2) + z1 + z2
z = z1 + z2

# Compute the partial derivatives (Jacobian components)
dz_dx = -2 * a1 * (x - h1) - 2 * a2 * (x - h2)  # ∂z/∂x
dz_dy = -2 * b1 * (y - k1) - 2 * b2 * (y - k2)  # ∂z/∂y

# Create a 3D plot
fig = plt.figure(figsize=(16, 7))

# 3D Surface Plot (left side)
ax = fig.add_subplot(131, projection='3d')

# Plot the surface
ax.plot_surface(x, y, z, cmap='viridis')

# Set labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D Surface Plot')

# Now, to show the 2D projection (you can change this to other projections like top view or side view):

# 2D contour plot
ax2 = fig.add_subplot(132)  # Add subplot for 2D plot (right side)
contour = ax2.contourf(x, y, z, 20, cmap='viridis')


# Set labels for the 2D projection
plt.xlabel('X axis')
plt.ylabel('Y axis')
fig.colorbar(contour, ax=ax2, label='Z value')
ax2.set_title('2D Contour Projection')


# Jacobian Vector Field Plot (right side)
ax3 = fig.add_subplot(133)
# Plot the Jacobian (Vector field) on the 2D contour plot
# Use quiver to plot the Jacobian vectors
skip = 5  # Control how many grid points to skip for arrow density
quiver = ax3.quiver(x[::skip, ::skip], y[::skip, ::skip], dz_dx[::skip, ::skip], dz_dy[::skip, ::skip], 
                    angles='xy', scale=80, color='g', width=0.004, headwidth=4, headlength=6)

# Add a marker for the origin (optimal point)
ax3.plot(0, 0, 'bo', color='r')  # Blue dot at the optimal point (0,0)

# Set labels and title for the Jacobian plot
ax3.set_xlabel('X axis')
ax3.set_ylabel('Y axis')
ax3.set_title('Jacobian Vector Field')

# Show both plots together
plt.tight_layout()
plt.show()
