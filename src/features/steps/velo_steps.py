from behave import given, when, then
from pytest import raises

from src.main.exceptions.exceptions import ValeurKilometriqueInvalideException
from src.main.models.velo_model import Velo
from src.main.models.vtt_model import VTT


@given('un vélo avec la référence "{reference}"')
def step_given_velo(context, reference):
    context.velo = Velo(reference)


@given('un VTT avec la référence "{reference}"')
def step_given_velo(context, reference):
    context.velo = VTT(reference)


@when('j\'ajoute {kilometres} kilomètres')
def step_when_ajoute_kilometres(context, kilometres):
    context.velo.ajouter_kilometres(int(kilometres))


@when('j\'ajoute {kilometres} kilomètres (erreur)')
def step_when_ajoute_kilometres(context, kilometres):
    context.kilometres = int(kilometres)


@when('je conduis en mode tout-terrain pour {kilometres} kilomètres')
def step_when_ajoute_kilometres_vtt_mode(context, kilometres):
    context.kilometres = context.velo.conduite_tout_terrain(int(kilometres))


@then('le vélo doit avoir {kilometrage} kilomètres')
def step_then_velo_kilometrage(context, kilometrage):
    assert context.velo.nombre_kilometres == int(kilometrage)


@then('une exception doit être levée avec le message "{message}"')
def step_then_exception(context, message):
    with raises(ValeurKilometriqueInvalideException) as excinfo:
        context.velo.ajouter_kilometres(context.kilometres)

    assert message == str(excinfo.value)
