import os
from os import system
from sys import platform

from termcolor import colored


def appuyer_touche_continuer() -> None:
    os.system("pause")


def vider_console() -> None:
    os_type: str
    match platform:
        case "linux":
            os_type = "clear"  # linux
        case "linux2":
            os_type = "clear"  # linux
        case "darwin":
            os_type = "clear"  # macOS
        case "win32":
            os_type = "cls"  # windows x86
        case "win64":
            os_type = "cls"  # windows x64
        case _:
            os_type = "clear"

    system(os_type)


def afficher_erreur(message: str) -> str:
    return colored(message, "red")


if __name__ == "__main__":
    print("Hello")
    appuyer_touche_continuer()
    print("World")
