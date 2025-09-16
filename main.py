import turtle

# gif, umístění obrázků v okně, text příběhu
zvirata = [
    {"name": "Kráva Běla", "shape": "krava.gif",
     "pozice": (0, 0), "pribeh": "Na farmě se chystal velký ples a kráva Běla měla být hostitelkou.\n"
     "Jenže stála uprostřed dvora a přemýšlela: „Co když nestihneme\n" 
     "připravit výzdobu?“ Rozhodla se požádat o pomoc psa Maxe,\n" 
     "protože ten vždy ví, kde co leží. Pro pokračování klikni na psa Maxe."},

    {"name": "Pes Max", "shape": "pes.gif",
     "pozice": (200, -120), "pribeh": "Max našel ve stodole staré lampiony a barevné stuhy.\n"
     "Přitáhl je na dvůr, ale zjistil, že sám je nepověsí.\n"
     "„To zvládne jedině Mína, ta je mrštná jako kočka,“ pomyslel si.\n"
     "Pro pokračování klikni na kočku Mínu."},

    {"name": "Kočka Mína", "shape": "kocka.gif",
     "pozice": (240, 35), "pribeh": "Mína vyskočila na plot a rychle pověsila lampiony i stuhy.\n"
     "Pak zamňoukala: „Ale hudbu ještě nemáme! Bez hudby ples nebude.“\n"
     "Vtom spatřila kohouta Rudlu, který vždycky zpívá nejhlasitěji.\n"
     "Pro pokračování klikni na kohouta Rudlu."},

    {"name": "Kohout Rudla", "shape": "kohout.gif",
     "pozice": (-220, -270), "pribeh": "Rudla zakokrhal: „Hudbu? To je moje! Ale potřebujeme i rytmus.“\n"
     "Začal volat na slepici Bělušku, protože ta vždycky klove do všeho\n" 
     "jako do bubínku. Pro pokračování klikni na slepici Bělušku."},

    {"name": "Slepice Běluška", "shape": "slepice.gif", 
     "pozice": (50, -250), "pribeh": "Běluška ťukala zobákem do kbelíku a vznikl krásný rytmus.\n"
     "Ale ples bez občerstvení by nebyl úplný. Naštěstí poblíž chroupal mrkev\n"
     "králík Hugo. Ten se určitě podělí. Pro pokračování klikni na králíka Huga."},

    {"name": "Králík Hugo", "shape": "kralik.gif",
     "pozice": (260, -230), "pribeh": "Hugo přinesl celou hromadu čerstvých mrkví a řekl:\n"
     "„Hosté musí mít co jíst. Ale pořád něco chybí... koláče!“\n"
     "A kdo jiný by upekl nejlepší koláče než prasátko Líza?\n"
     "Pro pokračování klikni na prase Lízu."},

    {"name": "Prase Líza", "shape": "prase.gif", 
     "pozice": (-80, -130), "pribeh": "Líza zapnula troubu, zamíchala těsto a brzy vůně koláčů\n"
     "provoněla celý dvůr. Všechno bylo připraveno: výzdoba, hudba, jídlo i dort.\n"
     "Zvířata se sešla uprostřed dvora a začal velký farmářský ples.\n"
     "Tancovali, zpívali a věděli, že když každý přidá svou ruku k dílu,\n"
     "dokáží společně cokoliv."},
]

aktualni_index = 0

# Nastavení okna
okno = turtle.Screen()
okno.title("Zvířátka na farmě")
okno.bgcolor("lightblue")
okno.setup(width=800, height=700) 

# rozdělení hrací plochy čárou
rozdeleni = turtle.Turtle()
rozdeleni.hideturtle()
rozdeleni.penup()
rozdeleni.goto(-400, -50)  
rozdeleni.pendown()
rozdeleni.forward(800)

# louka (zelený pruh dole)
louka = turtle.Turtle()
louka.hideturtle()
louka.penup()
louka.speed(0)
louka.goto(-400, -50)
louka.pendown()
louka.fillcolor("lightgreen")
louka.begin_fill()
for _ in range(2):
    louka.forward(800)
    louka.right(90)
    louka.forward(400)
    louka.right(90)
louka.end_fill()

# vykreslení - psí bouda se vstupem
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)
pen.penup()
pen.goto(200, -120)  
pen.pendown()
pen.fillcolor("#D9A273")
pen.begin_fill()
for _ in range(2):
    pen.forward(150)  
    pen.left(90)
    pen.forward(110)    
    pen.left(90)
pen.end_fill()
# vstup, psí bouda
pen.penup()
pen.goto(220, -110)
pen.pendown()
pen.fillcolor("#F2D1B3")
pen.begin_fill()
for _ in range(4):
    pen.forward(60)
    pen.left(90)  
pen.end_fill()
# popisek na boudě - MAX
pen.penup()
pen.goto(230, -50)   
pen.pendown()
pen.write("MAX", font=("Arial", 16, "bold"))

# domek
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)
pen.penup()
pen.goto(-380, -200)  
pen.pendown()
pen.fillcolor("#33FF7C")
pen.begin_fill()
for _ in range(4):
    pen.forward(200)
    pen.left(90)
pen.end_fill()
# dveře domu + klika
pen.penup()
pen.goto(-270, -200)
pen.pendown()
pen.fillcolor("#D9B23D")
pen.begin_fill()
for _ in range(2):
    pen.forward(60)
    pen.left(90)
    pen.forward(80)
    pen.left(90)
pen.end_fill()
pen.penup()
pen.goto(-215, -160)   
pen.pendown()
pen.dot(10, "black") 
# okna domu
pen.penup()
pen.goto(-270, -70)
pen.pendown()
pen.fillcolor("#F2EDE4")
pen.begin_fill()
for _ in range(4):
    pen.forward(50)
    pen.left(90)
pen.penup()
pen.goto(-350, -70)
pen.pendown()
for _ in range(4):
    pen.forward(50)
    pen.left(90)
pen.end_fill()
# vodorovná a svislá okenní mřížka, první okno
pen.penup()
pen.pensize(1)
pen.goto(-270, -50)     
pen.pendown()
pen.forward(50)
pen.penup()
pen.pensize(1)
pen.goto(-250, -70)     
pen.pendown()
pen.left(90)
pen.forward(50)
pen.right(90)   
# vodorovná a svislá okenní mřížka, druhý okno
pen.penup()
pen.pensize(1)
pen.goto(-350, -50)     
pen.pendown()
pen.forward(50)
pen.penup()
pen.pensize(1)
pen.goto(-330, -70)     
pen.pendown()
pen.left(90)
pen.forward(50)
pen.right(90)   
# střecha domu
pen.penup()
pen.pensize(3)
pen.goto(-380, 0)
pen.pendown()
pen.fillcolor("#D93814")
pen.begin_fill()
for _ in range(3):
    pen.forward(200)
    pen.left(120)
pen.end_fill()

# registrakce gif obrázků j
for z in zvirata:
    okno.addshape(z["shape"])

# nastavení umístění textu příběhu
pribeh_text = turtle.Turtle()
pribeh_text.hideturtle()
pribeh_text.penup()
pribeh_text.goto(90, 200) 

# uvodní text
uvod_text = turtle.Turtle()
uvod_text.hideturtle()
uvod_text.color("#155902")
uvod_text.penup()
uvod_text.goto(385, 250)
uvod_text.write("Příběh o tom, jak se zvířátka z farmy připravovala na ples.",align="right", font=("Comic Sans MS", 19, "bold"))
uvod_text.color("black")
uvod_text.penup()
uvod_text.goto(260, 200)
uvod_text.write("Pro pokračování příběhu klikni na kravičku Bělu.",align="right", font=("Arial", 17))

def konec(x, y):
    okno.bye()
# funkce po kliknutí na zvíře, vypíše text příběhu
def klik(index):
    def proved_akci(x, y):
        global aktualni_index
        pribeh_text.clear()
        uvod_text.clear()

        if index == aktualni_index:
            vypis_text(zvirata[index]["pribeh"])
            if aktualni_index == len(zvirata) - 1:
                pribeh_text.goto(-100, 150)
                pribeh_text.write("Klikni kamkoli pro ukončení.", font=("Arial", 17, "bold"))
                
                for turt in okno.turtles():
                    turt.onclick(None)
                okno.ontimer(lambda: okno.onscreenclick(konec))

            else:
                aktualni_index += 1
        else:
            spravne = zvirata[aktualni_index]["name"]
            spatne = zvirata[index]["name"]
            vypis_text(f"Toto není {spravne}, ale {spatne}. Zkus to znovu!")
            
    return proved_akci

# funkce pro zarovnání textu
def vypis_text(text, start_x=-260, start_y=320, line_height=30):
    pribeh_text.clear()
    lines = text.split("\n")
    y = start_y
    for line in lines:
        pribeh_text.goto(start_x, y)
        pribeh_text.write(line, align="left", font=("Arial", 14, "normal"))
        y -= line_height

# cyklus vezme informace o každém zvířeti a nastaví mu co se má stát, když na obrázek(zvířátko) někdo klikne.
for i in range(len(zvirata)):
    info = zvirata[i]
    t = turtle.Turtle()
    t.shape(info["shape"])
    t.penup()
    t.goto(info["pozice"])
    t.onclick(klik(i))


# hlavní cyklus
turtle.done()

