import random
import math

# Initialize counters for points inside and outside the circle
inside_circle = 0
outside_circle = 0

# Generate 10,000 random points and determine if they're inside or outside the circle
for i in range(10000):
    # Generate random x and y values between 0 and 1 (with slight offset to avoid exactly 0 or 1)
    x = random.uniform(0.000001, 0.999999)
    y = random.uniform(0.000001, 0.999999)
    
    # Check if the point is inside the circle using the equation x^2 + y^2 < 1
    if (x*x + y*y) < 1:
        inside_circle += 1
    else:
        outside_circle += 1

# Calculate the ratio of points inside the circle to total points,
# and multiply by 4 to approximate the value of π
ratio = (inside_circle / 10000) * 4

# Get the actual value of π from the math library
pi_from_library = math.pi

# Calculate the difference between the calculated value and the actual value of π
difference = pi_from_library - ratio

# Print the results
print(f"Calculated value of π: {ratio}")
print(f"Value of π from math library: {pi_from_library}")
print(f"Difference: {difference}")