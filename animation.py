#!/usr/bin/env python
"""
An animated image
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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

for i in range(100):
    x += np.pi / 15.
    y += np.pi / 15.
    im = plt.imshow(f(x, y), cmap='Blues', animated=True)
    im2 = plt.imshow(z(x, y), cmap='RdPu', animated=False)

    ims.append([im])
    ims.append([im2])

ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,
                                repeat_delay=1000)

ani.save('dynamic_images.mp4')


plt.show()