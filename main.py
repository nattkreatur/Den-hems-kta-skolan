import sys
import os


def clear():
    os.system('cls' if os.name == 'nt' else "clear")


def quit():
    #Håller exitfunktionen i en egen loop
    while True:
        print("Är du säker på att du vill avsluta spelet? (j/n)")
        answer = input(">")
        if answer.lower().strip() == "j":
            print("Vi ses på andra sidan...")
            sys.exit()
        elif answer.lower().strip() == "n":
            input("Tyckte väl inte att du såg så rädd ut... ännu...")
            clear()
            break

while True:
    print("")
    print("\t\t       Den hemsökta skolan    ")
    print("\t\t      _____________________    ")
    print("\t\t     /                     \   ")
    print("\t\t    /_______________________\  ")
    print("\t\t     |   _      _      _   |  ")
    print("\t\t     |  |_|    |_|    |_|  |  ")
    print("\t\t     |   _    _____    _   |  ")
    print("\t\t     |  |_|   | | |   |_|  |  ")
    print("\t\t     |________|_|_|________|  ")
    print("\t\t     -----------------------  ")


    print("\nVälkommen till 'Den hemsökta skolan'! Ett textbaserat äventyrsspel.\n")
    print("\nVill du spela? (j/n)")
    answer = input(">")

    if answer.lower().strip() == "j":
        input("Bra då börjar vi\n>")
        while True:
            clear()
            print("Du har vandrat långt och länge genom den mörka skogen i fullmånens sken.")
            print("Klockan är efter midnatt och du står nu utanför den hemsökta skolan.")
            print("Du ska livesända en TikTok-livestream när du undersöker skolan,")
            print("målet är att visa alla hur modig du är och få en massa följare.")
            print("Men när skuggorna dansar i månljuset börjar du ångra dig.")
            print("Det prasslar i en närliggande buske och du får en klump i magen.\n")
            print("Vad gör du?\n")
            print("1. Jag går in")
            print("2. Jag går hem")
            answer = input(">")
            if answer.strip() == "1":
                while True:
                    print("Buske hit och buske dit, du sätter Laxtonkepsen på huvudet och tänker att")
                    print("det är nu det gäller. Du går in genom huvudéntren och möts av en stor hall.")
                    print("Månen lyser in genom fönstren och kastar långa skuggor men lyser samtidigt upp")
                    print("lokalerna i ett blått sken. Framför dig har du en stor stentrappa till övre plan")
                    print("och till höger om dig har du en lång korridor.\n")
                    print("Vart vill du gå?\n")
                    print("1. Jag går upp för trappan")
                    print("2. Jag tar den högra korridoren")
                    answer = input(">")
                    if answer.strip() == "1":
                        while True:
                            print("")
                            answer = input(">")
                            if answer.strip() == "1":
                                while True:
                                    print("")
                            elif answer.strip() == "2":
                                pass
                            elif answer.lower().strip() == "q":
                                quit()
                    elif answer.strip() == "2":
                        pass
                    elif answer.lower().strip() == "q":
                        quit()

            elif answer.strip() == "2":
                print("Du vänder tvärt på klacken och tänker 'F dis shiiet'...")
                print("Men du hinner knappt gå mer än två meter innan det hoppar fram en")
                print("stor varulv och äter upp dig.")
                print("Du hann inte ens trycka på record...")
                input(">")
                clear()
                break
            elif answer.lower().strip() == "q":
                quit()

    elif answer.lower().strip() == "n":
        quit()