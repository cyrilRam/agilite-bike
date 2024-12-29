import pytest

from src.main.exceptions.exceptions import ValeurKilometriqueInvalideException
from src.main.factories.velo_factory import VeloFactory
from src.main.models.velo_model import Velo
from src.main.models.vtt_model import VTT


@pytest.fixture
def velo():
    """Fixture pour créer un nouvel objet Velo avant chaque test."""
    return Velo("REF123")


@pytest.fixture
def vtt():
    """Fixture pour créer un nouvel objet VTT avant chaque test."""
    return VTT("REF456")


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


def test_conduite_tout_terrain_valide(vtt):
    """Test pour vérifier l'ajout de kilomètres en conduite tout-terrain."""
    vtt.conduite_tout_terrain(10)
    assert vtt.nombre_kilometres == 20  # Les kilomètres sont doublés


def test_creer_velo_factory():
    """Test pour vérifier la création d'un VTT via la factory."""
    reference_vtt = "VTT1"
    reference_velo = "Velo1"
    vtt = VeloFactory.creer_vtt(reference_vtt)
    velo = VeloFactory.creer_velo_classique(reference_velo)

    assert isinstance(vtt, VTT)
    assert isinstance(velo, Velo)
    assert vtt.reference == reference_vtt
    assert vtt.nombre_kilometres == 0
    assert velo.reference == reference_velo
    assert velo.nombre_kilometres == 0
