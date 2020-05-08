for i in range(int(input())):
    word = input()
    letters = set(word)
    print(word)
    print(f" is{' not ' if 'a' in letters or 'u' in letters else ' '}a lipogram")