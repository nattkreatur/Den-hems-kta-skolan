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


def death():
    #infoga snygg forloop? RIP
    pass

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
                            print("Du går långsamt upp för den dammig gamla trappan, brädorna knarrar under dina fötter.")
                            print("När du når toppen av trappan möts du av en lång hall med klassrum på båda sidor.")
                            print("Du går in i det första klassrummet till vänster och möts av rader av tomma bänkar.")
                            print("Du ser också att det finns en dörr som leder till nästa klassrum så du behöver inte gå")
                            print("tillbaka ut i hallen om du inte vill. Plötsligt hör du steg i trappan utanför.\n")
                            print("Vad gör du?\n")
                            print("1. Jag gömmer dig i ett skåp")
                            print("2. Jag flyr in i nästa klassrum")
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
                        while True:
                            print("Du vandrar längs med korridoren och betraktar lektionssalarna som radar upp sig på")
                            print("din vänstra sida. Några dörrar är stängda medan andra står på glänt, genom springan")
                            print("ekar salarna tomma med bord och bänkar som vittnar om en tid då skolan var full av")
                            print("liv och rörelse. Längst bort i korridoren finns en dörr som leder ner till källaren.")
                            print("Plötsligt hör du ett kväkande ljud från Biologi-salen.\n")
                            print("Vad gör du?\n")
                            print("1. Jag flyr ner i källaren.")
                            print("2. Jag går in i Biologisalen för att undersöka.")
                            answer = input(">")
                            if answer.strip() == "1":
                                while True:
                                    clear()
                                    print("I källaren möts du av ett totalt mörker och det är oklart om du känner dig säkrare")
                                    print("här. Snarare känner du dig dum för det var ju läskigare här nere, du lyser dig fram")
                                    print("med mobilens sken och du hittar en dörr märkt 'Pannrum' och en dörr märkt 'Städskrubb'.")
                                    print("Du hör fotsteg på väg nerför trappan. Hjärtat bultar och du måste gömma dig.\n")
                                    print("Vilket rum väljer du?\n")
                                    print("1. Pannrummet")
                                    print("2. Städskrubben")
                                    answer = input(">")
                                    if answer.strip() == "1":
                                        clear()
                                        print("Du forcerar den tunga dörren till pannrummet och springer in medan fotstegen utanför")
                                        print("blir allt högre. I brist på gömställen kryper du in i den gamla pannan för att gömma")
                                        print("dig, du stänger till luckan och kryper ihop i mörkret. Utanför hör du hur fotstegen")
                                        print("kommer in i pannrummet, men också hur de går ut från rummet. Du känner lättnad över")
                                        print("att ha klarat dig och försöker nu att krypa ut ur pannan igen men luckan har fastnat!\n")
                                        print("Du kämpar för ditt liv men syret tar snart slut precis som ditt liv. Och fastän ditt")
                                        print("liv är slut kommer du snart att bli känd! För när du blir hittad går du viral på TikTok ")
                                        print("som 'Stupid kid crawled in boiler and died a horrible death'. En liten tröst iaf!")
                                        input(">")
                                        clear()
                                        break
                                    elif answer.strip() == "2":
                                        clear()
                                        print("Du gömmer dig bakom en hylla i förrådet och du hör hur fotstegen går in i pannrummet.")
                                        print("Sedan går de ut och fortsätter bort, djupare in i källaren. Du drar en lättnadens suck")
                                        print("och tar ett kliv mot dörren men i mörkret råkar du välta hyllan så att du får den över")
                                        print("dig. Olyckligtvis faller du med huvudet först ner i skurhinken.\n")
                                        print("Fastklämd drunknar du sakta i det sura vattnet, dina sista tankar blir på dina tre")
                                        print("TikTok-filföljare.")
                                        input(">")
                                        clear()
                                        break
                                    elif answer.lower().strip() == "q":
                                        quit()
                                    
                            elif answer.strip() == "2":
                                print("Du kliver in i salen men möts av en kväljande amfibiestank. När du tittar närmare")
                                print("på akvariet i hörnet ser du att klassens experiment på de lokala paddorna har blivit")
                                print("kvarglömda då skolan lades ner. När du ser det krossade glaset och de gigantiska")
                                print("paddformade fotspåren på golvet inser du att något har muterat utom kontroll i den")
                                print("isolerade miljön.\n")
                                print("När du känner en slemmig hand med simhud läggas på din axel förstår du att din tid är kommen.")
                                input(">")
                                clear()
                                break
                            elif answer.lower().strip() == "q":
                                quit()
                            break #testar att stoppa loopdöden här
                    elif answer.lower().strip() == "q":
                        quit()
                    break #testar att stoppa även här

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
#Kopierungsunderlag:
'''
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
'''