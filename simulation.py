# Importing libraries
import numpy as np
import drawSvg as draw

# Calculating Pi using 100,000 draws from uniform random variables
pi_value = 0
for i in range(100000):
    rvs = np.random.uniform(-1, 1, size=2)
    if (rvs[0]**2 + rvs[1]**2 <= 1):
        pi_value += 1
pi_value = 4 * pi_value / 100000
print(pi_value)

# Graphically visualizing Pi
s = 500 # scaling the figure [-1,1] to 1000 pixels
canvas = draw.Drawing(2*s, 2*s, origin='center')
canvas.append(draw.Rectangle(-s,-s,2*s,2*s, fill='white', stroke='black', stroke_width=4))
canvas.append(draw.Circle(0,0,s,fill='white', stroke='black', stroke_width=2))

color = 'black' # default color
for i in range(10000):
    rvs = np.random.uniform(-1, 1, size=2)
    color = 'red' if (rvs[0]**2 + rvs[1]**2 <= 1) else 'blue'
    canvas.append(draw.Circle(rvs[0]*s,rvs[1]*s,3,fill=color))
canvas.rasterize()



