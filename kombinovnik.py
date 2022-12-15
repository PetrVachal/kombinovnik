class Kombinovnik:
    '''
    Obsahuje vse pro vyhledavani podretezcu v zadanem retezci od uzivatele.
    V zadanem retezci se vyhovujici podretezce vyhledavaji z textoveho dokumentu,
    ktery je v zakladmim nastaveni slovnikem ceskych podstatnych jmen.
    '''

    def __init__(self, adr: str):
        '''
        Inicializuje instanci s vytvorenym slovnikem nactenym z adresy >adr<.
        :param adr: adresa slovniku jakozto txt dokumentu
        '''
        self.__adr = adr
        self.__slovnik = self._vrat_slovnik()

    def _vrat_slovnik(self) -> dict:
        '''
        Nacte data z txt slovniku a ulozi je do slovniku v podobe:
        {pocet znaku: slovo z txt dokumentu}
        :return: slovnik: {pocet znaku: slovo z txt dokumentu}
        '''

        slovnik = {}
        with open(self.__adr, encoding = "utf-8", mode = "r") as txt:
            for radek in txt:
                slovo = radek[:-1]
                try:
                    slovnik[len(slovo)].append(slovo)
                except KeyError:
                    slovnik[len(slovo)] = [slovo]
        maximum = max(slovnik.keys())
        for i in range(1, maximum + 1):
            if i not in slovnik:
                slovnik[i] = []
        return slovnik

    def najdi(self, retezec: str, mini: int = 3, maxi: int = 10) -> list:
        '''
        Prohledava ve slovniku vsechny takove retezce, ktere se v ruznych
        permutacich znaku objevuji v zadanem retezci.
        Pr.: V zadanem retezci "strom" se vyskytuje retezec "most"
             V zadanem retezci "kladivoun" se vyskytuje "dvoulinka".
        :param retezec: retezec zadany na vstupu
        :param mini: minimalni pocet znaku vracenych vyhledanych retezcu
        :param maxi: maximalni pocet znaku vracenych vyhledanych retezcu
        :return: seznam vsech nalezenych vyhovujicich retezcu ze slovniku
        '''

        nalezy = []
        maxi = min(maxi, len(retezec), max(self.__slovnik.keys()))
        if mini > maxi:
            return []
        for aktual_pocet_slov in range(mini, maxi + 1):
            for slovo in self.__slovnik[aktual_pocet_slov]:
                list_retezec = list(retezec)
                for znak in slovo:
                    if znak not in list_retezec:
                        break
                    list_retezec.remove(znak)
                else:
                    nalezy.append(slovo)
        return nalezy