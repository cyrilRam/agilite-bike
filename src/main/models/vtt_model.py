from src.main.models.velo_model import Velo


class VTT(Velo):
    def __init__(self, reference: str):
        super().__init__(reference)

    def conduite_tout_terrain(self, kilometres: int):
        """
        Les kilomètres parcourus en mode tout-terrain comptent double en raison
        des efforts supplémentaires nécessaires pour ce type de conduite. Le velo est soumis à plus de contraintes
        """
        self.ajouter_kilometres(kilometres * 2)
