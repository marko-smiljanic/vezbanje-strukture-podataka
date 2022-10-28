from Tacka2D import Tacka2D

class Tacka3D(Tacka2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def ispisi_koordinate(self):
        super().ispisi_koordinate()     #poziva se super ispis koji nema prelazak u novi red
        print(", z: {z}".format(z = self.z))

    