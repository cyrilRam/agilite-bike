Feature: Gestion des kilomètres pour un vélo
  En tant que propriétaire de vélo,
  Je veux pouvoir gérer les kilomètres parcourus,
  Afin de suivre l'utilisation de mon vélo.

  Scenario: Ajouter des kilomètres valides
    Given un vélo avec la référence "VttGiant"
    When j'ajoute 50 kilomètres
    Then le vélo doit avoir 50 kilomètres

  Scenario: Ajouter des kilomètres invalides
    Given un vélo avec la référence "VttGiant"
    When j'ajoute -10 kilomètres
    Then une exception doit être levée avec le message "Le nombre de kilomètres (-10) doit être un entier positif."

  Scenario Outline: Ajouter plusieurs kilomètres à un vélo
    Given un vélo avec la référence "<reference>"
    When j'ajoute <kilometres1> kilomètres
    And j'ajoute <kilometres2> kilomètres
    Then le vélo doit avoir <total_kilometres> kilomètres

    Examples:
      | reference | kilometres1 | kilometres2 | total_kilometres |
      | V123      | 30          | 20          | 50               |
      | V124      | 10          | 40          | 50               |
