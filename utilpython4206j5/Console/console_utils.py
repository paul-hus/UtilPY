from termcolor import colored


def lire_caractere(question: str) -> str:
    """
    Prend une question nécessitant une réponse à un seul caractère et retourne le caractère entré par l'utilisateur, et affiche une erreur si autre chose est entrée.
    :param question: Question posé à l'utilisateur
    :return: La lettre choisie par l'utilisateur
    """

    print(question)
    while True:
        caractere = input(": ")

        if len(caractere) == 1: break
        print("Veuillez saisir un seul caractère.\n")

    return caractere


def lire_chaine():
    ...


def lire_chaine_taille_intervalle():
    ...


def lire_entier(question: str) -> int:
    """
    Prend une question nécessitant un entier comme réponse et retourne l'entier entré par l'utilisateur, et affiche une erreur si autre chose est entrée.
    :param question: Question posé à l'utilisateur
    :return: L'entier choisi par l'utilisateur
    """

    print(question)
    while True:
        try:
            entier = int(input(": "))
            return entier
        except ValueError:
            print("Veuillez saisir un simple entier.\n")


def lire_entier_positif(question: str) -> int:
    """
    Prend une question nécessitant un entier positif comme réponse et retourne l'entier entré par l'utilisateur, et affiche une erreur si autre chose est entrée.
    :param question: Question posé à l'utilisateur
    :return: L'entier positif choisi par l'utilisateur
    """

    print(question)
    while True:
        try:
            entier = int(input(": "))

            if 0 > entier:
                raise AttributeError

            return entier
        except ValueError:
            print("Veuillez saisir un simple entier.\n")
        except AttributeError:
            print("Veuillez saisir un entier positif.\n")


def lire_entier_minimum(question: str, limite_min: int) -> int:
    """
    Prend une question nécessitant un entier au dessus d'une certaine limite comme réponse et retourne l'entier entré par l'utilisateur, et affiche une erreur si autre chose est entrée.
    :param question: Question posé à l'utilisateur
    :param limite_min: La limite minimum de l'intervalle
    :return: L'entier valide choisi par l'utilisateur
    """

    print(question)
    while True:
        try:
            entier = int(input(": "))

            if limite_min > entier:
                raise AttributeError

            return entier
        except ValueError:
            print("Veuillez saisir un simple entier.\n")
        except AttributeError:
            print("Veuillez saisir un entier valide.\n")


def lire_entier_intervalle(question: str, intervalle_min: int, intervalle_max: int) -> int:
    """
    Prend une question nécessitant un entier situé dans un intervalle donné comme réponse et retourne l'entier entré par l'utilisateur si valide dans l'intervalle, et affiche une erreur si une valeur non-élement de l'intervalle est entrée ou si autre chose est entrée.
    :param question: Question posé à l'utilisateur
    :param intervalle_min: Limite minimale de l'intervalle
    :param intervalle_max: Limite maximale de l'intervalle
    :return: L'entier valide choisi par l'utilisateur
    """

    print(question)
    while True:
        try:
            entier = int(input(": "))

            if intervalle_min > entier > intervalle_max:
                raise AttributeError

            return entier
        except ValueError:
            print("Veuillez saisir un simple entier.\n")
        except AttributeError:
            print("Veuillez saisir un entier valide.\n")


def lire_reel(question: str) -> float:
    """
    Prend une question nécessitant un réel comme réponse et retourne le réel entré par l'utilisateur, et affiche une erreur si autre chose est entrée.
    :param question: Question posé à l'utilisateur
    :return: Le réel choisi par l'utilisateur
    """

    print(question)
    while True:
        try:
            reel = float(input(": "))
            return reel
        except ValueError:
            print("Veuillez saisir un simple nombre.\n")


def lire_reel_positif(question: str) -> float:
    """
    Prend une question nécessitant un réel positif comme réponse et retourne le réel entré par l'utilisateur, et affiche une erreur si autre chose est entrée.
    :param question: Question posé à l'utilisateur
    :return: Le réel positif choisi par l'utilisateur
    """

    print(question)
    while True:
        try:
            reel = int(input(": "))

            if 0 > reel:
                raise AttributeError

            return reel
        except ValueError:
            print("Veuillez saisir un simple nombre.\n")
        except AttributeError:
            print("Veuillez saisir un nombre positif.\n")


def lire_reel_minimum(question: str, limite_min: float) -> float:
    """
    Prend une question nécessitant un réel au dessus d'une certaine limite comme réponse et retourne le réel entré par l'utilisateur, et affiche une erreur si autre chose est entrée.
    :param question: Question posé à l'utilisateur
    :param limite_min: La limite minimum de l'intervalle
    :return: Le réel valide choisi par l'utilisateur
    """

    print(question)
    while True:
        try:
            reel = int(input(": "))

            if limite_min > reel:
                raise AttributeError

            return reel
        except ValueError:
            print("Veuillez saisir un simple nombre.\n")
        except AttributeError:
            print("Veuillez saisir un nombre valide.\n")


def lire_reel_intervalle(question: str, intervalle_min: float, intervalle_max: float) -> float:
    """
    Prend une question nécessitant un réel situé dans un intervalle donné comme réponse et retourne le réel entré par l'utilisateur si valide dans l'intervalle, et affiche une erreur si une valeur non-élement de l'intervalle est entrée ou si autre chose est entrée.
    :param question: Question posé à l'utilisateur
    :param intervalle_min: Limite minimale de l'intervalle
    :param intervalle_max: Limite maximale de l'intervalle
    :return: Le réel valide choisi par l'utilisateur
    """

    print(question)
    while True:
        try:
            reel = int(input(": "))

            if intervalle_min > reel > intervalle_max:
                raise AttributeError

            return reel
        except ValueError:
            print("Veuillez saisir un simple nombre.\n")
        except AttributeError:
            print("Veuillez saisir un nombre valide.\n")


def lire_entier_minimum_ou_sentinelle(question: str, limite_min: int, sentinelle: int) -> int:
    """
    Prend une question nécessitant un entier au dessus d'une certaine limite comme réponse et retourne l'entier entré par l'utilisateur, et affiche une erreur si autre chose est entrée. Si la sentinelle est entrée, le script va arrêter.
    :param question: Question posé à l'utilisateur
    :param limite_min: La limite minimum de l'intervalle
    :param sentinelle: L'entier choisi pour sortir du programme
    :return: L'entier valide choisi par l'utilisateur
    """

    print(question)
    while True:
        try:
            entier = int(input(": "))

            if entier == sentinelle: exit()

            if limite_min > entier:
                raise AttributeError

            return entier
        except ValueError:
            print("Veuillez saisir un simple entier.\n")
        except AttributeError:
            print("Veuillez saisir un entier valide.\n")


def lire_caractere_ensemble(question: str, ensemble: str) -> str:
    """
    Demande la saisie d'un caractère valide selon l'ensemble spécifié
    :param question: Question posé à l'utilisateur
    :param ensemble: Une chaine de tous les caractères valides
    :return: Le caractère choisi
    """

    print(question)
    while True:
        caractere = input(": ")

        if len(caractere) != 1:
            print("Veuillez saisir un seul caractère.\n")
            continue

        if not caractere in ensemble:
            print("Veuillez saisir un caractère valide.\n")
            continue

        return caractere



def confirmer(question: str) -> bool:
    """
    Demande une confirmation O/N à l'utilisateur
    :param question: La question doit aussi afficher les choix valides (O ou N) pour indiquer à l'utilisateur
    :return: Vrai si l'utilisateur a confirmé (O ou o)
    """

    print(question + " (O/N)")

    while True:
        reponse = input(": ")

        if reponse in "Oo":
            return True
        elif reponse in "Nn":
            return False
        print("Veuillez saisir un caractère valide.\n")


if __name__ == '__main__':
    lire_caractere("C ou F")
