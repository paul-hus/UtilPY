from os import system
from sys import platform


def appuyer_touche_continuer() -> None:
    system("pause")


def vider_console() -> None:
    os_type = "cls" if platform in ("win32", "win64") else "clear"
    system(os_type)


if __name__ == "__main__":
    print("Hello")
    appuyer_touche_continuer()
    vider_console()
    print("World")
    appuyer_touche_continuer()
