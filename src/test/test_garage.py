import pytest

from src.main.models.velo_model import Velo
from src.main.models.garage_model import Garage


@pytest.fixture
def garage_avec_velos():
    """Fixture pour créer un garage avec deux vélos ayant des kilomètres attribués."""
    garage = Garage()

    velo1 = Velo("REF123")
    velo1.ajouter_kilometres(10)
    garage.ajouter_un_velo(velo1)

    velo2 = Velo("REF456")
    velo2.ajouter_kilometres(20)
    garage.ajouter_un_velo(velo2)

    return garage


def test_ajouter_velo(garage_avec_velos):
    """Test pour vérifier que l'on peut ajouter un vélo au garage."""
    nouveau_velo = Velo("REF789")
    nouveau_velo.ajouter_kilometres(15)
    garage_avec_velos.ajouter_un_velo(nouveau_velo)

    assert len(garage_avec_velos.velos) == 3
    assert garage_avec_velos.velos[-1].reference == "REF789"


def test_get_total_nombre_km(garage_avec_velos):
    """Test pour vérifier le total des kilomètres parcourus par les vélos du garage."""
    assert garage_avec_velos.calculer_total_kilometres() == 30


def test_get_total_nombre_km_apres_ajout(garage_avec_velos):
    """Test pour vérifier le total des kilomètres après ajout d'un nouveau vélo."""
    nouveau_velo = Velo("REF999")
    nouveau_velo.ajouter_kilometres(25)
    garage_avec_velos.ajouter_un_velo(nouveau_velo)

    assert garage_avec_velos.calculer_total_kilometres() == 55


def test_calculer_total_kilometres_vide():
    garage = Garage()
    assert garage.calculer_total_kilometres() == 0
