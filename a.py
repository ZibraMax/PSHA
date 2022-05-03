from PSHA.SSM import SeismicSourceModel, Point, Line, Rectangle, Area
from PSHA.GMM import AkkarEtAl_2014
import numpy as np
import matplotlib.pyplot as plt


gmm = AkkarEtAl_2014(760)


ip = np.array([0.0, 0.0])

coords = np.array([[0.0, 60.0]])
punto = Point(coords, 4.0, 5.0, 2.7, 1.2)
punto.setGMM(gmm)

coords = np.array([[-15.0, -30.0], [-50.0, 75.0]])
linea = Line(coords, 7.3, 4.0, 4.4, 1.0, nr=10, ns=1000, nm=10)
linea.setGMM(gmm)


coords = np.array([[60.0, -50.0], [90.0, -50.0], [90.0, 0.0], [60.0, 0.0]])
rectangulo = Rectangle(coords, 7.7, 4.0, 3.5, 0.8, nr=10, nm=10)
rectangulo.setGMM(gmm)
rectangulo.mesh(300, 500)
rectangulo.plotMesh()
plt.show()

O = SeismicSourceModel(ip, [punto, linea, rectangulo])


# O.sources[0].plotDMDistribution()
# O.sources[1].plotDMDistribution()
# O.sources[2].plot5DMDistribution()

O.solve()

a = 0
