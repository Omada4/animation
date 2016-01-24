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


for i in range(130):
    x += np.pi / 15.
    y += np.pi /20.
    im = plt.imshow(z(x, y), cmap= 'bwr', animated=True)
    im2 = plt.imshow(z(x, y), cmap= 'gray', animated=True)
    im3 = plt.imshow(z(x,y), cmap= 'bone', animated=False)
    ims.append([im])
    ims.append([im2])
    ims.append([im3])


ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,repeat_delay=5000)

# plt.imsave(ph + "/Animation_Omada_4.mp4", ims)
plt.show()
ani.save(ph + '/Animation_Omada_4.mp4')
# mywriter = animation.FFMpegWriter()
# ani.save(ph + "Animation_Omada_4a.mp4", writer=mywriter)
# plt.show()
