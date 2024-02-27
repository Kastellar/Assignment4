def getHint(secret: str, guess: str) -> str:
    b, c = 0, 0
    gc = {i: guess.count(i) for i in guess}
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            b += 1
            gc[secret[i]] -= 1
        elif gc.get(secret[i]):
            c += 1
            gc[secret[i]] -= 1

    return f"{b}A{c}B"


print(getHint("1807", "7810"))
print(getHint("1123", "0111"))
print(getHint("1122", "2211"))
print(getHint("11", "10"))
