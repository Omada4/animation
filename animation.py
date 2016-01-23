
#!/usr/bin/env python
"""
An animated image
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
ph = os.path.expanduser('~/public_html')

fig = plt.figure()


def f(x, y):
    return np.sin(x) + np.cos(y)
    
def z(x, y):
    return np.sin(2*x) + np.cos(2*y)


x = np.linspace(0, 3 * np.pi, 100)
y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)
# ims is a list of lists, each row is a list of artists to draw in the
# current frame; here we are just animating one artist, the image, in
# each frame
ims = []
ims2 = []

ims3 = []

for i in range(100):
    x += np.pi / 15.
    y += np.pi /20.
    im = plt.imshow(f(x, y), cmap='Blues', animated=True)
    im2 = plt.imshow(z(x, y), cmap='RdPu', animated=False)
#    im3 = plt.imshow(z(x,y), cmap='bone', animated=True)
 
ims.append([im])
ims.append([im2])
#ims.append([im3])
ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,
                                repeat_delay=1000)

ani.save(ph+"/dynamic_images.mp4")


plt.show()