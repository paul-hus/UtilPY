from termcolor import colored
import sys


def lire_caractere(question: str) -> str:
    while True:
        caractere = input(question)

        if len(caractere) == 1: break

        print("Veuillez saisir un seul caractère.")

    return caractere


def lire_chaine():
    ...


def lire_chaine_taille_intervalle():
    ...


def lire_entier(question: str) -> int:
    while True:
        try:
            entier = int(input(question))
            return entier
        except ValueError:
            print("Veuillez saisir un simple entier.")


def lire_entier_positif():
    ...


def lire_entier_minimum():
    ...


def lire_entier_intervalle():
    ...


def lire_reel():
    ...


def lire_reel_positif():
    ...


def lire_reel_minimum():
    ...


def lire_reel_intervalle():
    ...


def lire_entier_minimum_ou_sentinelle(question: str, minimum: int, sentinelle: int) -> int:
    ...


def lire_caractere_ensemble(question: str, ensemble: str) -> str:
    """
    Demande la saisie d'un caractère valide selon l'ensemble spécifié
    :param question: un caractère valide
    :param ensemble: une chaine de tous les caractères valides
    :return: le caractère choisi
    """

    if question in ensemble:
        return question


def confirmer(question: str) -> bool:
    """
    Demande une confirmation O/N à l'utilisateur
    :param question: la question doit aussi afficher les choix valides (O ou N) pour indiquer à l'utilisateur
    :return: vrai si l'utilisateur a confirmé (O ou o)
    """

    print(question + " (O/N)")

    while True:
        reponse = input(": ")

        if reponse in "Oo":
            return True
        elif reponse in "Nn":
            return False
        print(colored(text="Choix invalide, veuiller réessayer", color="red"))


if __name__ == '__main__':
    if confirmer("Êtes-vous en vie?"):
        print("Bravo")
    else:
        print("Dommage")
