def est_carre(n: int) -> bool:
    ...


def ln(nb: float) -> float:
    ...


def bertha(a: float, b: float, c: float) -> (float, float):
    ...


def est_premier(nb: int) -> bool:
    ...


def csc():
    ...


def sec():
    ...


if __name__ == "__main__":
    assert (est_carre(1))
    assert (est_carre(4))
    assert (not est_carre(3))
    assert (est_carre(64))
    nb = 758259836596
    assert (est_carre(nb * nb))
