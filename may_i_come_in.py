while True:
    print("wat is jou leeftijd?")
    choice = input()
    if choice >= '18':
        print("kom binnen")
        break
    elif choice < '18':
        print("weg")
        break
    else:
        print(choice, " dat was geen leeftijd")
        continue