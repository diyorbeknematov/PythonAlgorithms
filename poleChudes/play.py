from random import choice
import colorama as c
c.init(autoreset=True)

def savollar():
    savol = {
                "Yer yuzidagi eng katta materik" : 'YEVROOSIYO',
                "O'zbekiston davlatining poytaxti qaysi shahar" : "TOSHKENT",
                "Suvning kimyoviy belgisi" : "H2O"
            }
    return savol

class Play:
    def __init__(self, nomi) -> None:
        self.nomi = nomi


    def __drawCell(self, space):
        uzn = len(space)
        print(f"{c.Fore.GREEN + c.Style.BRIGHT}{'______'*uzn}")
        print(f"{c.Fore.GREEN + c.Style.BRIGHT}{'|     '*uzn}|")
        for i in space:
            print(f"{c.Fore.GREEN + c.Style.BRIGHT}|{c.Fore.RED}  {i}  ", end="")
        print(f"{c.Fore.GREEN + c.Style.BRIGHT}|")
        print(f"{c.Fore.GREEN + c.Style.BRIGHT}{'|_____'*uzn}|", end="\n\n")


    def SavolTanlash(self, savolLugat):
        self.s = choice(list(savolLugat.keys()))
        return self.s

    def savolBer(self, savol):
        return f"\n{c.Back.WHITE + c.Fore.RED + c.Style.BRIGHT} !!!SAVOL        {savol}        SAVOL!!! {c.Style.RESET_ALL}\n"

    def yangilash(self, savolj, harf, javob : str):
        count = 0
        if harf == savolj:
            for i in javob:
                if i == "*":
                    count += 1
            javob = harf
            self.__drawCell(javob)
            return count, javob
        
        for i, bel in enumerate(savolj):
            if bel == harf:
                count += 1
                javob = list(javob)
                javob[i] = harf
                javob = ''.join(javob)

        self.__drawCell(javob)
        return count, javob


    def checkWinner(self, savolj, javob):
        if savolj == javob:
            return True
        else: False
