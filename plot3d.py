from matplotlib import pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
from numpy import array

def plot3d(my_matrix):
    # cast to array
    my_array = array(my_matrix.T)
    class Arrow3D(FancyArrowPatch):
        def __init__(self, xs, ys, zs, *args, **kwargs):
            FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
            self._verts3d = xs, ys, zs

        def draw(self, renderer):
            xs3d, ys3d, zs3d = self._verts3d
            xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
            self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
            FancyArrowPatch.draw(self, renderer)


    fig = plt.figure(figsize=(5,5))
    ax = fig.add_subplot(111, projection='3d')

    for v in my_array:
        a = Arrow3D([0, v[0]], [0, v[1]], [0, v[2]], mutation_scale=10, lw=3, arrowstyle="-|>", color="r")    
        ax.add_artist(a)
        
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    plt.title('Vectors')
    return plt

    plt.draw()
    plt.show()
