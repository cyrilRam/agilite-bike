class ValeurKilometriqueInvalideException(Exception):
    """Exception levée lorsque le nombre de kilomètres ajouté est invalide."""

    def __init__(self, message="Le nombre de kilomètres doit être un entier positif."):
        super().__init__(message)
