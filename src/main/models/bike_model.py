from src.main.exceptions.exceptions import ValeurKilometriqueInvalideException


class Velo:
    def __init__(self, reference: str):
        self.reference: str = reference
        self.nombreKm: int = 0

    def ajouterKilometres(self, kilometres: int):
        if kilometres <= 0:
            raise ValeurKilometriqueInvalideException(
                f"Valeur invalide : {kilometres}. Le nombre de kilomètres doit être positif."
            )
        self.nombreKm += kilometres
