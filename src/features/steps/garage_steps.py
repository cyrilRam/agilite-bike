from _pytest.python_api import raises
from behave import given, when, then

from src.main.exceptions.exceptions import VeloReferenceExistanteException
from src.main.models.garage_model import Garage
from src.main.models.velo_model import Velo


@given('un garage vide')
def step_given_garage_vide(context):
    Garage.reset()
    context.garage = Garage()


@when('j\'ajoute un vélo avec la référence "{reference}"')
def step_when_ajoute_velo(context, reference):
    velo = Velo(reference)
    context.garage.ajouter_un_velo(velo)


@when('j\'ajoute un vélo qui existe déjà avec la référence "{reference}"')
def step_when_ajoute_velo(context, reference):
    context.reference = reference


@when('j\'ajoute {nombreKm} kilomètres au vélo "{reference}"')
def step_when_ajoute_kilometres(context, nombreKm, reference):
    velo = context.garage.trouver_velo_par_reference(reference)
    velo.ajouter_kilometres(int(nombreKm))


@then('le kilométrage total doit être {kilometrage}')
def step_then_kilometrage_total(context, kilometrage):
    assert context.garage.calculer_total_kilometres() == int(kilometrage)


@then('le garage contient un vélo avec la référence "{reference}"')
def step_then_velo_dans_garage(context, reference):
    velo = context.garage.trouver_velo_par_reference(reference)
    assert velo is not None
    assert velo.reference == reference


@then('l\'exception doit être levée avec le message "{message}"')
def step_then_exception_levee(context, message):
    with raises(VeloReferenceExistanteException) as excinfo:
        velo = Velo(context.reference)
        context.garage.ajouter_un_velo(velo)

    assert message in str(excinfo.value)
