def createScreen(name: str, num: int, word: str):
    print("-" * 39)
    for index, i in enumerate([name, num, word]):
        print("|" + " " * 10 + str(i) + " " * (27 - len(str(i))) + "|")
        if index != 2:
            print("|" + " " * 37 + "|")
    print("-" * 39)


name, int, word = input().split()
createScreen(name, int, word)
