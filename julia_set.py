import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Axes limits and plot resolution

x_min, x_max, y_min, y_max, res = -2, 2, -2, 2, 50

# Real and imaginay axes

re = np.linspace(x_min, x_max, int(res*(x_max - x_min)))
im = np.linspace(y_min, y_max, int(res*(y_max - y_min)))
# Number of iterations and frames of animation

max_iter = 20
frames = 100

# Complex Number c:= r*e^(i*theta) = r*cos(theta) + i*r*sin(theta)
#r = 0.7885
r = 0.8
theta = np.linspace(0, np.pi, frames)

# Julia Set function

def julia(cx, cy, zx, zy, max_iter):
    c = complex(cx, cy)
    z = complex(zx, zy)
    for i in range(max_iter):
        z = z**2 + c
        if abs(z) > 2:
            return i
    return max_iter - 1

# Empty Canvas

fig, ax = plt.subplots(figsize=(6, 6))

# Animation Function

def animate(i):
    ax.clear()
    ax.set_xticks([])
    ax.set_yticks([])
    Z = np.empty((len(re), len(im)))
    cx, cy = r * np.cos(theta[i]), r * np.sin(theta[i])

    for i in range(len(re)):
        for j in range(len(im)):
            Z[i, j] = julia(cx, cy, re[i], im[j], max_iter)

    img = ax.imshow(Z.T, interpolation="bicubic", cmap='magma')
    return [img]

# Run the animation

anim = animation.FuncAnimation(
    fig, animate, frames=frames, interval=50, blit=True, repeat=False)

# Save a gif of the animation

#anim.save('julia_set.gif', writer='imagemagick')
writervideo = animation.FFMpegWriter(fps=30, bitrate=-1)
plt.rcParams['animation.ffmpeg_path'] = r'C:\\Users\\unive\\Downloads\\Programs\\ffmpeg-4.3.1-win64-static\\bin\\ffmpeg.exe'
anim.save("julia_set3.gif", writer=writervideo)
