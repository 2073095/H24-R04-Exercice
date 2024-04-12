class Reservoir:
    def __init__(self, pVolume) -> None:
        self.volume = pVolume

    def remplir(self, nombre):
        self.volume += nombre #basically bullshit

    def __str__(self):
        return f"Le réservoir est de : {self.volume}"
        