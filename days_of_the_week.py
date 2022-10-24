from calendar import weekday


print("moet je vandaag naar school?")
choice = input().upper()
if choice == 'ja':
    print("saai")
elif choice == 'nee':
    print("lekker")
else:
    print(choice, " dat was geen keuze JA OF NEE")
    