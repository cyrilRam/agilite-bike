from src.main.exceptions.exceptions import ValeurKilometriqueInvalideException


class Velo:
    def __init__(self, reference: str):
        self.reference: str = reference
        self.nombre_kilometres: int = 0

    def ajouter_kilometres(self, kilometres: int):
        if kilometres <= 0:
            raise ValeurKilometriqueInvalideException(
                f"Valeur invalide : {kilometres}. Le nombre de kilomètres doit être positif."
            )
        self.nombre_kilometres += kilometres