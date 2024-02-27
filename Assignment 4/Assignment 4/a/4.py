def getFluctuation(F1: float, F2: float) -> float:
    return round((F1 + F2 + F1 * F2) / 100, 6)


print(getFluctuation(10.42, 20.64))
