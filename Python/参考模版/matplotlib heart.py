import matplotlib
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib.path as mpath

fig, ax = plt.subplots()

Path = mpath.Path
path_data = [
    (Path.MOVETO, (1.00, -0.57)),
    (Path.CURVE4, (0.35, 0.0)),
    (Path.CURVE4, (-1.75, 2.0)),
    (Path.CURVE4, (0.375, 2.0)),
    (Path.LINETO, (1.00, 1.35)),
    (Path.CURVE4, (1.625, 2.0)),
    (Path.CURVE4, (3.75, 2.0)),
    (Path.CURVE4, (1.65, 0.0)),
    (Path.CLOSEPOLY, (1.00, -0.57)),
    ]
codes, verts = zip(*path_data)
path = mpath.Path(verts, codes)
patch = mpatches.PathPatch(path, facecolor='r', alpha=0.5)
ax.add_patch(patch)

# plot control points and connecting lines
x, y = zip(*path.vertices)
line, = ax.plot(x, y, 'go-')

ax.grid()
fig.suptitle("Love you till forever!")
ax.axis('equal')
fig.savefig("love520.png")
plt.show()