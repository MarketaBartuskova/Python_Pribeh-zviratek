# 🐄 FarmStory – Příběh zvířátek na farmě

Projekt je interaktivní program v Pythonu vytvořený pomocí knihovny **turtle**.  
Uživatel klikáním na zvířátka postupně odhaluje příběh o tom, jak se farma připravovala na ples.  

---

***Součástí repozitáře je:***
- `README.md` – popis projektu, dokumentace  
- `main.py` – hlavní program s příběhem  
- `*.gif` – obrázky zvířátek použitá v programu (kráva, pes, kočka, kohout, slepice, králík, prase)  
- `images/` – složka se screenshoty ukazující průběh programu  

---

***Funkce:***
- Kliknutím na správné zvíře se zobrazí další část příběhu  
- Při kliknutí na špatné zvíře program vypíše upozornění (např. *„Toto není Kočka Mína, ale Prase Líza. Zkus to znovu!“*)  
- Po kliknutí na poslední zvíře se zobrazí závěr a možnost ukončit program  
- Grafické zobrazení farmy (louka, domek, psí bouda) vytvořené pomocí knihovny `turtle`  
- Interaktivní ovládání pouze pomocí klikání myší  

---

***Použité technologie a metody:***
- **Python 3** – programovací jazyk  
- **turtle** – kreslení grafiky, registrace GIF obrázků a obsluha kliknutí myší  
- Ošetření chybného postupu uživatele (kliknutí na nesprávné zvíře)  
- Práce s globálním stavem programu (sledování, které zvíře je na řadě)  

---

***Ukázka aplikace:***

[Úvodní obrazovka](images/start_screen.png)  

[Kliknutí na správné zvíře](images/correct_click.png)  

[Kliknutí na špatné zvíře](images/wrong_click.png)  

[Závěr příběhu](images/end_story.png)  
