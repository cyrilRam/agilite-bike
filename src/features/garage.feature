Feature: Gestion des vélos dans le garage
  En tant que propriétaire de garage,
  Je veux gérer les vélos et leur kilométrage,
  Afin de suivre leur état d'utilisation.

  Scenario: Ajouter plusieurs vélos dans le garage
    Given un garage vide
    When j'ajoute un vélo avec la référence "VttGiant"
    And j'ajoute un vélo avec la référence "VttSpe"
    And j'ajoute 50 kilomètres au vélo "VttGiant"
    And j'ajoute 75 kilomètres au vélo "VttSpe"
    Then le kilométrage total doit être 125
#    And le garage contient un vélo avec la référence "<reference>"

  Scenario: Ajouter un velo déjà existant
    Given un garage vide
    When j'ajoute un vélo avec la référence "VttGiant"
    And j'ajoute un vélo avec la référence "VttGiant"
    Then l'exception doit être levée avec le message "Un vélo avec la référence VttGiant existe déjà dans le garage."

  Scenario: Calculer le kilométrage total avec un garage vide
    Given un garage vide
    Then le kilométrage total doit être 0

#  Scenario Outline: Ajouter plusieurs vélos dans le garage
#    Given un garage vide
#    When j'ajoute un vélo avec la référence "<reference>"
#    And j'ajoute <nombreKm> kilomètres au vélo "<reference>"
#    Then le kilométrage total doit être 125
#
#    Examples:
#      | reference | nombreKm |
#      | VttGiant  | 50       |
#      | VttSpe    | 75       |

