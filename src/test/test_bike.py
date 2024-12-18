import pytest

from src.main.exceptions.exceptions import ValeurKilometriqueInvalideException
from src.main.models.bike_model import Velo


@pytest.fixture
def velo():
    """Fixture pour créer un nouvel objet Velo avant chaque test."""
    return Velo("REF123")


def test_ajouter_kilometres_valide(velo):
    """Test pour vérifier l'ajout de kilomètres valides."""
    velo.ajouterKilometres(10)
    assert velo.nombreKm == 10


def test_ajouter_kilometres_cumule(velo):
    """Test pour vérifier l'ajout cumulé de kilomètres."""
    velo.ajouterKilometres(5)
    velo.ajouterKilometres(15)
    assert velo.nombreKm == 20


def test_ajouter_kilometres_zero(velo):
    """Test pour vérifier que l'ajout de 0 kilomètre lève une exception."""
    with pytest.raises(ValeurKilometriqueInvalideException) as exc_info:
        velo.ajouterKilometres(0)
    assert "Le nombre de kilomètres doit être positif" in str(exc_info.value)


def test_ajouter_kilometres_negatif(velo):
    """Test pour vérifier que l'ajout d'une valeur négative lève une exception."""
    with pytest.raises(ValeurKilometriqueInvalideException) as exc_info:
        velo.ajouterKilometres(-5)
    assert "Le nombre de kilomètres doit être positif" in str(exc_info.value)
