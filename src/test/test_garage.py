import pytest

from src.main.exceptions.exceptions import VeloReferenceExistanteException
from src.main.models.garage_model import Garage
from src.main.models.velo_model import Velo


@pytest.fixture
def garage_avec_velos():
    """Fixture pour créer un garage avec deux vélos ayant des kilomètres attribués."""
    Garage.reset()
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
    Garage.reset()
    garage = Garage()
    assert garage.calculer_total_kilometres() == 0


def test_ajouter_velo_existant(garage_avec_velos):
    with pytest.raises(VeloReferenceExistanteException):
        garage_avec_velos.ajouter_un_velo(garage_avec_velos.velos[0])


def test_trouver_velo_par_reference_existante(garage_avec_velos):
    velo_trouve = garage_avec_velos.trouver_velo_par_reference("REF123")
    assert velo_trouve is not None
    assert velo_trouve.reference == "REF123"
    assert velo_trouve.nombre_kilometres == 10


def test_trouver_velo_par_reference_inexistante(garage_avec_velos):
    velo_trouve = garage_avec_velos.trouver_velo_par_reference("NONEXISTANT")
    assert velo_trouve is None


def test_garage_singleton(garage_avec_velos):
    """
    si je cree un nouveau garage je dois enfait renvoyer le garage déclaré dans la fixture
    """
    garage_bis = Garage()
    assert len(garage_bis.velos) == 2
    assert garage_bis.calculer_total_kilometres() == 30
