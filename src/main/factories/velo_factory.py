from src.main.models.velo_model import Velo
from src.main.models.vtt_model import VTT


class VeloFactory:

    @staticmethod
    def creer_velo_classique(reference: str) -> Velo:
        """
        Factory Method pour créer un vélo.
        """
        return Velo(reference)

    @staticmethod
    def creer_vtt(reference: str) -> VTT:
        """
        Factory Method pour créer un vtt.
        """
        return VTT(reference)
