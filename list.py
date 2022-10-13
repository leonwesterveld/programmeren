boodschapList = []
import os

def add():
    print("wat wil je toevoegen")
    boodschapList.append(input())
    os.system('cls')
    print(boodschapList)
    lijst1()

def weg():
    print("wat wil je verwijderen")
    boodschapList.remove(input())
    os.system('cls')
    print(boodschapList)
    lijst1()


def lijst1():
    q1 = input("Wat wil je doen? toevoegen (t) of verwijderen (v)?")
    if q1 == 't':
        add()
    elif q1 == 'v':
        weg()

def lijst():
    q1 = input("Jouw lijst is nog leeg!\nWat wil je doen? toevoegen (t) of verwijderen (v)?")
    if q1 == 't':
        add()
    elif q1 == 'v':
        weg()

lijst()
