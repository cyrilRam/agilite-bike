from abc import ABC, abstractmethod

from src.main.models.velo_model import Velo
from src.main.models.vtt_model import VTT


class VeloFactory(ABC):
    @abstractmethod
    def creer_velo_classique(self, reference: str) -> Velo:
        pass

    @abstractmethod
    def creer_vtt(self, reference: str) -> VTT:
        pass


class ClassiqueVeloFactory(VeloFactory):
    def creer_velo_classique(self, reference: str) -> Velo:
        return Velo(reference)

    def creer_vtt(self, reference: str) -> VTT:
        return VTT(reference)
