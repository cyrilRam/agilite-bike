from typing import List, Optional

from src.main.models.bike_model import Velo


class Garage:
    def __init__(self, velos: Optional[List[Velo]] = None):
        self.velos: List[Velo] = velos if velos is not None else []
        self.nombreKm: int = 0

    def ajouterVelo(self, velo: Velo):
        self.velos.append(velo)

    def getTotalNombreKm(self) -> int:
        totalKm = 0
        for velo in self.velos:
            totalKm += velo.nombreKm
        return totalKm
