class ValeurKilometriqueInvalideException(Exception):
    """Exception levée lorsque le nombre de kilomètres ajouté est invalide."""

    def __init__(self, kilometres):
        super().__init__(f"Le nombre de kilomètres ({kilometres}) doit être un entier positif.")


class VeloReferenceExistanteException(Exception):
    """Exception levée lorsque le nombre de kilomètres ajouté est invalide."""

    def __init__(self, reference):
        super().__init__(f"Un vélo avec la référence {reference} existe déjà dans le garage.")
