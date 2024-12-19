import pytest

from src.main.exceptions.exceptions import ValeurKilometriqueInvalideException
from src.main.models.velo_model import Velo


@pytest.fixture
def velo():
    """Fixture pour créer un nouvel objet Velo avant chaque test."""
    return Velo("REF123")


def test_ajouter_kilometres_valide(velo):
    """Test pour vérifier l'ajout de kilomètres valides."""
    velo.ajouter_kilometres(10)
    assert velo.nombre_kilometres == 10


def test_ajouter_kilometres_cumule(velo):
    """Test pour vérifier l'ajout cumulé de kilomètres."""
    velo.ajouter_kilometres(5)
    velo.ajouter_kilometres(15)
    assert velo.nombre_kilometres == 20


def test_ajouter_kilometres_zero(velo):
    """Test pour vérifier que l'ajout de 0 kilomètre lève une exception."""
    with pytest.raises(ValeurKilometriqueInvalideException) as exc_info:
        velo.ajouter_kilometres(0)


def test_ajouter_kilometres_negatif(velo):
    """Test pour vérifier que l'ajout d'une valeur négative lève une exception."""
    with pytest.raises(ValeurKilometriqueInvalideException) as exc_info:
        velo.ajouter_kilometres(-5)
