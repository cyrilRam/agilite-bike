from src.main.models.velo_model import Velo


class VTT(Velo):
    def __init__(self, reference: str):
        super().__init__(reference)

    def conduite_tout_terrain(self, kilometres: int):
        self.ajouter_kilometres(kilometres * 2)
