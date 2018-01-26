from marching_cubes import march
from numpy import load
import numpy
from operator import mul
from functools import reduce

try:
    volume = load("test/sample.npy")
except IOError:
    volume = load("sample.npy")


numpy.random.seed(5)

for i in range(1000):
    print('set seed to',i)
    numpy.random.seed(i)
    shape = [20]*3
    volume  = numpy.random.randint(2, size=reduce(mul,shape)).reshape(shape)

    while(volume.sum() == 0):
        volume  = numpy.random.randint(2, size=reduce(mul,shape)).reshape(shape)



    print(i)
    vertices, normals, faces = march(volume, 0)  # zero smoothing rounds
    smooth_vertices, smooth_normals, faces = march(volume, 4)  # 4 smoothing rounds


from pyqtgraph.opengl import GLViewWidget, MeshData
from pyqtgraph.opengl.items.GLMeshItem import GLMeshItem

from PyQt5.QtGui import QApplication

app = QApplication([])
view = GLViewWidget()

mesh = MeshData(vertices/100.0, faces)  # scale down - otherwise camera is misplaced
# or mesh = MeshData(smooth_vertices / 100, faces)
mesh._vertexNormals = normals
# or mesh._vertexNormals = smooth_normals

item = GLMeshItem(meshdata=mesh, color=[1, 0, 0, 1], shader="normalColor")

view.addItem(item)
view.show()
app.exec_()