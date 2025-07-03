import sys
import os
import time


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

def epilog():
    x = "Grattis du överlevde den hemsökta skolan!"
    y = "Slut!"
    print()
    for i in x:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.2)
    print()
    time.sleep(0.75)
    print("\nTyvärr var det dåligt ljus och du skakade av rädsla när du filmade spöket så filmen blev")
    time.sleep(0.75)
    print("av rätt låg kvalitet. Du fick tre nya följare och toppkommentaren under videon blev")
    time.sleep(0.75)
    print("'Why do these idiots Always film shit like this with a f-in toaster?'. Du känner dig")
    time.sleep(0.75)
    print("aningen misslyckad. En kommentar längre ner är mer positiv och tycker att du har gjort")
    time.sleep(0.75)
    print("ett bra jobb. Personen vill gärna att ni träffas imorgon igen vid den hemsökta skolan för")
    time.sleep(0.75)
    print("att utforska den tillsammans. Du tycker att personen verkar trevlig och seriös då personen har")
    time.sleep(0.75)
    print("en mycket verklighetstrogen varulv som profilbild.\n")
    time.sleep(0.75)
    print()
    for i in y:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.5)
    time.sleep(0.2)
    input("\n\nTryck <Enter> för att komma tillbaka starten.")

def death():
    print("")
    x = "\t DU ÄR DÖD!"
    for i in x:
        sys.stdout.write(i) #skriver ut till terminalen utan att göra det på en ny rad(till skillnad från print())
        sys.stdout.flush() #tömmer buffert/cache för att output inte ska bli "ryckig", har förmodligen ingen effekt 
                            #på de flesta moderna terminalfönster då de "flushar" problemfritt på egen hand
        time.sleep(0.3) #pausar programmet i 0.4sec efter varje loop
    print(r"")
    print(r"        ____________   " )      
    print(r"       /            \  " )
    print(r"      /              \ " )
    print(r"     |                | " )
    print(r"     |      R.I.P     | " )
    print(r"     |                | " )
    print(r"     |                | " )
    print(r"     |                | " )
    print(r"     |                | " )
    print(r"    *|   *   *  *     | *     ")
    print(r" ____)/\/(\/(/\)/\//\/|_)____ ")
    input("Tryck <Enter> för att fortsätta...")


while True:
    clear()
    print("")
    print(r"           Den hemsökta skolan      ")
    print(r"      *****************************   ")
    print(r"          _____________________    ")
    print(r"         /                     \   ")
    print(r"        /_______________________\  ")
    print(r"         |   _      _      _   |  ")
    print(r"         |  |_|    |_|    |_|  |  ")
    print(r"         |   _    _____    _   |  ")
    print(r"         |  |_|   | | |   |_|  |  ")
    print(r"         |________|_|_|________|  ")
    print(r"         -----------------------  ")
    print(r"           ©Oskar Boberg 2025    ")

    
    print("\nVill du spela? (j/n)")
    answer = input(">")

    if answer.lower().strip() == "j":
        while True:
            clear()
            print("\nVälkommen till 'Den hemsökta skolan! Ett textbaserat äventyrsspel.")
            answer = input("Du kan när som helst avsluta spelet genom att skriva 'q' för quit.\n>")
            if answer.lower().strip() == "q":
                quit()
                continue
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
                        clear()
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
                                clear()
                                print("Du går långsamt upp för den dammiga gamla trappan, brädorna knarrar under dina fötter.")
                                print("När du når toppen av trappan möts du av en lång hall med klassrum på båda sidor.")
                                print("Du går in i det första klassrummet till vänster och möts av rader med tomma bänkar.")
                                print("Du ser också att det finns en dörr som leder till nästa klassrum, och en annan dörr")
                                print("som leder tillbaka ut till hallen. Plötsligt hör du steg i trappan utanför.\n")
                                print("Vad gör du?\n")
                                print("1. Jag gömmer mig i ett skåp")
                                print("2. Jag flyr in i nästa klassrum")
                                answer = input(">")
                                if answer.strip() == "1":
                                    clear()
                                    print("Det är kvavt och instängt i skåpet. Fotstegen kommer in i rummet. Du håller andan medan")
                                    print("du hör stegen gå ett varv runt hela rummet och sedan fortsätta in i nästa klassrum.")
                                    print("Samtidigt som du öppnar luckan för att krypa ut känner du en smärta i vaden. Du har")
                                    print("blivit biten av en råtta i skåpet. Beklämd över att det nu har blivit hål i dina nya")
                                    print("byxor går du hem och skiter i den här hemsökta jädra skolan.\n")
                                    input()
                                    print("Några veckor senare dör du i sviterna av en långdragen infektion som hade sitt ursprung")
                                    print("i ett råttbett.")
                                    input(">")
                                    death()
                                elif answer.strip() == "2":
                                    while True:
                                        clear()
                                        print("Du flyr in i nästa klassrum. Rakt fram har du en dörr in till ytterligare ett klassrum")
                                        print("och till höger har du en dörr som leder ut mot hallen igen. Bakom dig kan du höra hur ")
                                        print("fotstegen kommer in i rummet och går ett varv och fortsätter sedan rakt mot dig.\n")
                                        print("Vad gör du?\n")
                                        print("1. Jag flyr vidare in i nästa klassrum")
                                        print("2. Jag flyr ut i hallen")
                                        answer = input(">")
                                        if answer.strip() == "1":
                                            clear()
                                            print("Du springer in i nästa klassrum. Stegen bakom dig tystnar och du börjar nu känna dig säker.")
                                            print("På tavlan står det 'Datorteknik'. En kyla sänker sig snabbt över rummet och en skepnad")
                                            print("uppenbarar sig bakom lärarens skrivbord. Det är vålnaden av läraren i Datorteknik. Hon")
                                            print("spänner ögonen djupt i dig och säger 'Det blir F'.\n")
                                            input()
                                            print("Du avlider av skam.")
                                            input(">")
                                            death()
                                        elif answer.strip() == "2":
                                            while True:
                                                clear()
                                                print("Du springer ut i hallen och in i klassrummet tvärsöver. Du hör inte längre fotstegen")
                                                print("och du verkar vara utom fara. I det här klassrummet är det ett stort hål i golvet")
                                                print("och ett öppet fönster. Du hör prassel i buskarna utanför.\n")
                                                print("Vad gör du?\n")
                                                print("1. Jag hoppar ner i hålet")
                                                print("2. Jag tittar ut genom fönstret")
                                                answer = input(">")
                                                if answer.strip() == "1":
                                                    while True:
                                                        clear()
                                                        print("Du landar i köket med en hög duns. Vad det än var som följde efter dig på övervåningen")
                                                        print("hör din landning och fotstegen smattrar ner för trappen. Paniken sprider sig i din kropp")
                                                        print("och du måste tänka fort.\n")
                                                        print("Vad gör du?\n")
                                                        print("1. Jag kryper in i ugnen och gömmer mig")
                                                        print("2. Jag har fått nog, jag konfronterar monstret")
                                                        answer = input(">")
                                                        if answer.strip() == "1":
                                                            clear()
                                                            print("Detta visar sig snabbt vara en dålig idé då det väsen som har jagat dig går raka vägen")
                                                            print("in i köket och startar ugnen. Medan du grillas till döds hinner du reflektera över hur")
                                                            print("dumt det var att du inte visste att elen var påslagen i byggnaden. Isåfall hade du ju")
                                                            print("bara kunnat tända taklamporna istället för att fjanta runt i mörkret.")
                                                            input()
                                                            print("Dina sista tankar blir på MAX-hamburgare av någon anledning.")
                                                            input(">")
                                                            death()
                                                        elif answer.strip() == "2":
                                                            clear()
                                                            print("Du beväpnar dig med en stekspade och inväntar sammandrabbningen. Dörren flängs upp och")
                                                            print("in springer ett spöke som ser ut som en gammal mattant, hon springer raka vägen till")
                                                            print("ugnen och sätter på den och fortsätter sedan genom dig bort mot skafferiet. Det visar")
                                                            print("sig vara en vålnad som rör sig i ett mönster och hon verkar inte alls kunna se dig.")
                                                            print("Ett minne från någons liv som spelas upp om och om igen som en gammal trasig skiva.")
                                                            print("Lättad men fascinerad dokumenterar du händelsen på TikTok och det enda du kan tänka på")
                                                            print("är hur många likes du kommer att få.")
                                                            input(">")
                                                            epilog()
                                                        elif answer.lower().strip() == "q":
                                                            quit()
                                                            continue
                                                        else:
                                                            continue
                                                        break
                                                elif answer.strip() == "2":
                                                    clear()
                                                    print("Du tittar ut genom fönstret och nedanför dig är buskarna och huvudentrén till skolan där")
                                                    print("du nyss gick in. Det är samma buskar som prasslade innan, och eftersom du känner dig ")
                                                    print("trygg på andra våningen fortsätter du titta ner för att försöka se vad det är.\n")
                                                    print("Plötsligt hoppar en stor varulv upp och biter av dig huvudet.\n")
                                                    input()
                                                    print("Det sista du hinner tänka innan du dör är 'röva'.")
                                                    input(">")
                                                    death()
                                                elif answer.lower().strip() == "q":
                                                    quit()
                                                    continue
                                                else:
                                                    continue
                                                break
                                        elif answer.lower().strip() == "q":
                                            quit()
                                            continue
                                        else:
                                            continue
                                        break
                                elif answer.lower().strip() == "q":
                                    quit()
                                    continue
                                else:
                                    continue
                                break
                        elif answer.strip() == "2":
                            while True:
                                clear()
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
                                            input()
                                            print("Du kämpar för ditt liv men syret tar snart slut precis som ditt liv. Och fastän ditt")
                                            print("liv är slut kommer du snart att bli känd! För när du blir hittad går du viral på TikTok ")
                                            print("som 'Stupid kid crawled in boiler and died a horrible death'. En liten tröst iaf!")
                                            input(">")
                                            death()
                                        elif answer.strip() == "2":
                                            clear()
                                            print("Du gömmer dig bakom en hylla i förrådet och du hör hur fotstegen går in i pannrummet.")
                                            print("Sedan går de ut och fortsätter bort, djupare in i källaren. Du drar en lättnadens suck")
                                            print("och tar ett kliv mot dörren men i mörkret råkar du välta hyllan så att du får den över")
                                            print("dig. Olyckligtvis faller du med huvudet först ner i skurhinken.\n")
                                            input()
                                            print("Fastklämd drunknar du sakta i det sura vattnet, dina sista tankar blir på dina tre")
                                            print("TikTok-följare.")
                                            input(">")
                                            death()
                                        elif answer.lower().strip() == "q":
                                            quit()
                                            continue
                                        else:
                                            continue
                                        break
                                        
                                elif answer.strip() == "2":
                                    clear()
                                    print("Du kliver in i salen men möts av en kväljande amfibiestank. När du tittar närmare")
                                    print("på akvariet i hörnet ser du att klassens experiment på de lokala paddorna har blivit")
                                    print("kvarglömda då skolan lades ner. När du ser det krossade glaset och de gigantiska")
                                    print("paddformade fotspåren på golvet inser du att något har muterat utom kontroll i den")
                                    print("isolerade miljön.\n")
                                    input()
                                    print("När du känner en slemmig hand med simhud läggas på din axel förstår du att din tid är kommen.")
                                    input(">")
                                    death()
                                elif answer.lower().strip() == "q":
                                    quit()
                                    continue
                                else:
                                    continue
                                break
                        elif answer.lower().strip() == "q":
                            quit()
                            continue
                        else:
                            continue
                        break

                elif answer.strip() == "2":
                    clear()
                    print("Du vänder tvärt på klacken och tänker 'F dis shiiet'...")
                    print("Men du hinner knappt gå mer än två meter innan det hoppar fram en")
                    print("stor varulv och äter upp dig.\n")
                    input()
                    print("Du hann inte ens trycka på record...")
                    input(">")
                    death()
                elif answer.lower().strip() == "q":
                    quit()
                    continue
                else:
                    continue
                break
            break
    elif answer.lower().strip() == "n":
        quit()
    #inge else / break behöver förekomma efter denna elif ditt trötthuvve
