from math import sqrt, floor, sin, cos, log, e, pi


def est_carre(n: int) -> bool:
    """
    Vérifie si un nombre est un carré parfait.
    :param n: nombre à vérifier
    :return:
    """

    racine_carree = sqrt(n)
    return racine_carree == floor(racine_carree)


def ln(n: float) -> float:
    """
    Retourne le logarithme népérien d'un nombre.
    :param n: nombre à prendre le logarithme népérien
    :return:
    """

    return log(n, e)


def bertha(a: float, b: float, c: float) -> (float, float):
    """
    Retourne les solutions d'une équation quadratique, ou une erreur s'il n'y a pas de solutions réelles.
    :param a: coefficient de x²
    :param b: coefficient de x
    :param c: constante
    :return: un tuple contenant les deux solutions
    """

    det = (b * b) - 4 * (a * c)
    if det < 0:
        raise ArithmeticError("Pas de solutions réelles.")

    haut_div_pos = -1 * b + sqrt(det)
    haut_div_neg = -1 * b - sqrt(det)
    bas_div = 2 * a

    return haut_div_pos / bas_div, haut_div_neg / bas_div


def est_premier(n: int) -> bool:
    """
    Vérifie si un nombre est premier. (limité aux multiple de 2, 3, 5, 7 et 11
    :param n: nombre à vérifier
    :return:
    """

    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0 or n % 11 == 0:
        if n == 2 or n == 3 or n == 5 or n == 7 or n == 11:
            return True
        return False
    return True


def csc(angle: float, convert: bool = False) -> float:
    """
    Retourne la cosecante d'un angle.
    :param angle: angle en radians
    :param convert: True si l'angle est en degrés
    :return:
    """

    if convert:
        angle = angle * (pi / 180)

    return 1 / sin(angle)


def sec(angle: float, convert: bool = False) -> float:
    """
    Retourne la secante d'un angle.
    :param angle: angle en radians
    :param convert: True si l'angle est en degrés
    :return:
    """

    if convert:
        angle = angle * (pi / 180)

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
