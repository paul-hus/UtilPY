from termcolor import colored


def appuyer_touche_continuer() -> None:
    ...

def vider_console():
    ...

def afficher_erreur(message: str) -> None:
    print(colored(message, "red"))


