from random import choice as rand
import colorama as c
c.init(autoreset=True)

from time import sleep

class Player:
    def __init__(self, ism, play, magazine) -> None:
        self.name = ism
        self.ball = 0
        self.play = play
        self.__magazine = magazine

    def getName(self):
        return self.name

    def getBall(self):
        return self.ball

    def baraban_aylantir(self):
        ball = [1000, 500, 200, 100, 50, 0, 'X']

        while True:
            aylantir = input(f"{self.name} barabanni aylantirishga tayyormisiz (ha/yo'q): ")
            if aylantir.lower() == 'ha':
                break
            else:
                sleep(2)
        b = rand(ball)
        print(f"Barabanni aylantirganda tushdi: {b}")
        return b

    def sayLatter(self, savolJ, javob, savol):
        while True:
            if savolJ == javob:
                break
            ball = self.baraban_aylantir()

            if ball == "X":
                print(f"{c.Back.RED + c.Fore.BLACK + c.Style.BRIGHT} {self.name} siz bir bor gal o'tkazasiz!")
                self.ball = 0
                return javob
            
            print(self.play.savolBer(savol))
            belgi = input("Biron bir harf ayting: ")
            belgi = belgi.upper()
            count, javob = self.play.yangilash(savolJ, belgi, javob)
            if count != 0:
                self.ball += (int(ball) * count)
            else: break

        return javob
    
    def sovgaOlish(self):
        print(self.__magazine.sovgaOlish(self))