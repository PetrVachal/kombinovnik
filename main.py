import os

from kombinovnik import Kombinovnik
from os import path as ospath
from sys import argv

def prepis_radek_programu(adr, text, vlajecka):
    """
    vstup: str, str, str
    vystup: None
    --
    Procedura prepis_radek_programu prepisuje radek v kodu programu        ..
    ulozenem na adrese >adr< na >text< podle vlajecky >vlajecka< .
    """
    nase_fce = "prepis_radek_programu"
    vst_podminky = [
        (type(adr) == str, "argument >adr< musi byt datoveho typu str "),
        (type(text) == str, "argument >text< musi byt datoveho typu str "),
        (type(vlajecka) == str, "argument >vlajecka< musi byt datoveho typu str "),
        ]
    for podm in vst_podminky:
        assert podm[0], f"{nase_fce}: {podm[1]}"

    text = text.replace("\\\\", "\\")
    kod = []
    with open(adr, encoding = "utf-8", mode = "r") as py:
        for radek in py:
            kod.append(radek)
    i = 0
    while i < len(kod):
        radek = kod[i]
        if radek.startswith(vlajecka):
            index = i + 1
            break
        i += 1
    kod[index] = text
    with open(adr, encoding = "utf-8", mode = "w") as py:
        for radek in kod:
            py.write(radek)

# adr
adr = ".\ceska_podstatna_jmena.txt"

ne = "nn"
prompt = ": "
navod = "navod"
navod_obsah = f"""
Program Kombinovník vyhledává všechny řetězce, které se vyskytují ve vámi zadaném řetězci.
U vyhovujících řetězců jde jen o to, aby všechny jejich znaky byly zároveň i ve vašem vstupu.
Zhlediska znakové shody je tedy každý nalezený řetězec podmnožinou řetězce vašeho.
Př.: V řetězci "strom" se vyskytuje řetězec "most".
     V řetězci "chobotnice" se vyskytuje řetězec "beton".
     Pokud chcete vyhledat řetězce na aspoň 5 znaků, zadejte za >mini< hodnotu 5.
     Pokud chcete vyhledat řetězce na maximálně 8 znaků, zadejte za >maxi< hodnotu 8.
     >mini< a >maxi< lze kombinovat. Tyto parametry fungují zároveň.
     V případě zadání Enteru u mini nebo maxi se nastaví parametry takto:
        mini = 3
        maxi = 10
     Pro ukončení programu zadejte "{ne}"."""

# reseni problemu s adresou txt slovniku
prepis = False
while not ospath.isfile(adr):
    # neplatna adresa
    print(
f"""Slovník na adrese {adr} neexistuje.
Zadejte prosím novou adresu slovníku.
Pokud chcete program ukončit, zadejte "{ne}".""")
    adr = input(prompt)
    prepis = True
    if adr == ne:
        # uzivatel nechce zadavat novou adresu
        exit(0)
if prepis:
    # neplatna adresa prepsana na platnou
    atp = adresa_tohoto_programu = argv[0]
    # prepis adresu v tomto kodu
    prepis_radek_programu(atp, f"adr = \"{adr}\"\n", "# adr")
    # ukonci se
    exit(0)

radikal = lambda vst: exit(0) if vst == ne else vst

# vytvoreni instance s danym slovnikem z adresy >adr<
kombi = Kombinovnik(adr)

print(f"\nVítá vás program Kombinovník. Pokud program neznáte, zadejte \"{navod}\".")
print("\nZadejte...")
while True:
    retezec = radikal(input(f"\nřetězec{prompt}"))
    if retezec == navod:
        print(navod_obsah)
        continue
    mini = radikal(input(f"mini [Enter]{prompt}"))
    try:
        mini = int(mini)
    except ValueError as err:
        if mini:
            print(err)
            continue
    maxi = radikal(input(f"maxi [Enter]{prompt}"))
    try:
        maxi = int(maxi)
    except ValueError as err:
        if maxi:
            print(err)
            continue
    if mini and maxi:
        nalezy = kombi.najdi(retezec, mini, maxi)
    elif mini:
        nalezy = kombi.najdi(retezec, mini = mini)
    elif maxi:
        nalezy = kombi.najdi(retezec, maxi = maxi)
    else:
        nalezy = kombi.najdi(retezec)
    if len(nalezy) == 0:
        print("Nebylo nic nalezeno.")
    for nalez in nalezy:
        print(nalez)
    if len(nalezy) > 5:
        print(f"Nalezeno {len(nalezy)} řetězců.")