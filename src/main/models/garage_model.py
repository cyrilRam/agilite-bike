from typing import List, Optional

from src.main.exceptions.exceptions import VeloReferenceExistanteException
from src.main.models.velo_model import Velo


class Garage:
    def __init__(self, velos: Optional[List[Velo]] = None):
        self.velos: List[Velo] = velos if velos is not None else []
        self.total_kilometres: int = 0

    def ajouter_un_velo(self, velo: Velo):
        if self.trouver_velo_par_reference(velo.reference):
            raise VeloReferenceExistanteException(velo.reference)
        self.velos.append(velo)

    def calculer_total_kilometres(self) -> int:
        return sum(velo.nombre_kilometres for velo in self.velos)

    def trouver_velo_par_reference(self, reference: str) -> Optional[Velo]:
        for velo in self.velos:
            if velo.reference == reference:
                return velo
        return None
