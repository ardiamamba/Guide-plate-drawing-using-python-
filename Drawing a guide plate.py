#  Write a computer program to design and draw a guide plate of dimensions 120 × 240mm with circles of diameters from 4 to 12 mm, in steps of 2 mm, and from 15 to 50mm, in steps of 5 mm.
import math
import matplotlib.pyplot as plt


width = 120
height = 240

small_diameters = [4, 6, 8, 10, 12]
large_diameters = [15, 20, 25, 30, 35, 40, 45, 50]

fig, ax = plt.subplots(figsize=(12, 6))
ax.set_xlim(0, width)
ax.set_ylim(0, height)
ax.set_aspect('equal')

for d in small_diameters:
    x = d / 2
    y = d / 2
    ax.add_artist(plt.Circle((x, y), d / 2, fill=False))
    ax.add_artist(plt.Circle((width - x, y), d / 2, fill=False))
    ax.add_artist(plt.Circle((x, height - y), d / 2, fill=False))
    ax.add_artist(plt.Circle((width - x, height - y), d / 2, fill=False))
    
for d in large_diameters:
    x = d / 2
    y = d / 2
    ax.add_artist(plt.Circle((x, y), d / 2, fill=False))
    ax.add_artist(plt.Circle((width - x, y), d / 2, fill=False))
    ax.add_artist(plt.Circle((x, height - y), d / 2, fill=False))
    ax.add_artist(plt.Circle((width - x, height - y), d / 2, fill=False))

# Save the figure
plt.savefig('guide_plate_circles.png')
