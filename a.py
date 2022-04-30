from PSHA import PSHA
import numpy as np
import matplotlib.pyplot as plt

ip = np.array([0.0, 0.0])
mmin = 4.0
mmax = 5.0
a = 2.7
b = 1.2

coords = np.array([[0.0, 60.0]])
sources = [PSHA.Point(coords, 4.0, 5.0, 2.7, 1.2)]

coords = np.array([[-15.0, -30.0], [-50.0, 75.0]])
sources += [PSHA.Line(coords, 7.3, 4.0, 4.4, 1.0, nr=10, ns=1000, nm=10)]

coords = np.array([[-15.0, -30.0], [-50.0, 75.0], [-15.0, 30.0], [0.0, -20.0]])
sources += [PSHA.Area(coords, 7.3, 4.0, 4.4, 1.0, nm=10)]
sources[-1].mesh(fmt='qa10')
# sources[-1].plotMesh()
plt.show()

coords = np.array([[20, 18.0], [100.0, 18.0], [100.0, 78.0], [20.0, 78.0]])
sources += [PSHA.Rectangle(coords, 7.7, 4.0, 3.5, 0.8, nr=10, nm=10)]
sources[-1].mesh(80, 60)
# sources[-1].plotMesh()
plt.show()

O = PSHA.SeismicSourceModel(ip, sources)
# O.sources[0].plotDistanceDistribution()
# O.sources[1].plotDistanceDistribution()
# O.sources[2].plotDistanceDistribution()
# O.sources[3].plotDistanceDistribution()
a = 0
