from typing import Optional, List

from src.main.exceptions.exceptions import VeloReferenceExistanteException
from src.main.models.velo_model import Velo


class Garage:
    _instance = None

    def __new__(cls, velos: Optional[List[Velo]] = None):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.velos = velos if velos is not None else []
            cls._instance.total_kilometres = 0
        return cls._instance

    @classmethod
    def reset(cls):
        """Réinitialiser l'instance du Singleton pour chaque test."""
        cls._instance = None

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
