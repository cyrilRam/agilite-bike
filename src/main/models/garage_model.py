from typing import List, Optional

from src.main.models.velo_model import Velo


class Garage:
    def __init__(self, velos: Optional[List[Velo]] = None):
        self.velos: List[Velo] = velos if velos is not None else []
        self.total_kilometres: int = 0

    def ajouter_un_velo(self, velo: Velo):
        self.velos.append(velo)

    def calculer_total_kilometres(self) -> int:
        return sum(velo.nombre_kilometres for velo in self.velos)

