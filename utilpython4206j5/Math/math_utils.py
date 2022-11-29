from math import sqrt, floor, sin, cos, log, e

from utilpython4206j5.Console.console_os import afficher_erreur


def est_carre(n: int) -> bool:
    racine_carree = sqrt(n)
    return racine_carree == floor(racine_carree)


def ln(n: float) -> float:
    return log(n, e)


def bertha(a: float, b: float, c: float) -> (float, float):
    det = (b * b) - 4 * (a * c)
    if det < 0:
        afficher_erreur("Pas de solutions")
        return 0, 0

    haut_div_pos = -1 * b + sqrt(det)
    haut_div_neg = -1 * b - sqrt(det)
    bas_div = 2 * a

    return haut_div_pos / bas_div, haut_div_neg / bas_div


def est_premier(n: int) -> bool:
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0 or n % 11 == 0:
        if n == 2 or n == 3 or n == 5 or n == 7 or n == 11:
            return True
        return False
    return True


def csc(angle: float) -> float:
    return 1 / sin(angle)


def sec(angle: float) -> float:
    return 1 / cos(angle)


if __name__ == "__main__":
    assert (est_carre(1))
    assert (est_carre(4))
    assert (not est_carre(3))
    assert (est_carre(64))
    nb = 758259836596
    assert (est_carre(nb * nb))

    print(est_premier(2))
    print(est_premier(13))
    print(est_premier(45))

    print(bertha(4, 8, -2))

    print(ln(20))
