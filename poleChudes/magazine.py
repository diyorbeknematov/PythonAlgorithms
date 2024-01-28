import colorama as c
c.init(autoreset=True)

class Magazine:
    def __init__(self) -> None:
        self.olingan_sovgalar = []
        self.sovga = {
                "Kitob"          : 50,
                "Televizor"      : 100,
                "Kompyuter"      : 3000,
                "Printer"        : 200,
                "5 million"      : 1500,
                "Mi 13"          : 1000,
                "Samsum S24"     : 2500,
                "iPhone 15"      : 3000,
                "Mackbook"       : 5000,
                "Malibu"         : 10000
            }

    def sovgalar(self):
        print("*******    SOVG'LAR    *******")
        for key , value in self.sovga.items():
            print(f"{key} : {value}")

    def sovgaOlish(self, player):
        if self.sovga['Kitob'] > player.ball:
                return f"{player.name} sizning to'plagan balingiz: {player.ball}\nSizning yig'gan balingiz sovgalar uchun yetmaydi\n"
                 
         
        while player.ball>=0:
            print(f"{c.Back.WHITE + c.Fore.RED + c.Style.BRIGHT} Sizning balingiz: {player.ball} {c.Style.RESET_ALL}\n")
            if self.sovga['Kitob'] > player.ball:
                return f"{player.name} balingiz boshqa sovg'aga yetmaydi😒😒😒\n\n{c.Back.WHITE + c.Fore.RED + c.Style.BRIGHT} {player.name} siz yutib olgan sovg'alar: {self.olingan_sovgalar} 👍 "
            self.sovgalar()

            s = input("Yig'gan balingizga qanday sovg'alar olasiz: ").capitalize()
            if s not in self.sovga.keys():
                print("Bizda bunday sovg'a yo'q")
                continue

            if self.sovga[s] <= player.ball:
                self.olingan_sovgalar.append(s)
                print(f"\nOlingan sovg'alar: {self.olingan_sovgalar}")
                player.ball -= self.sovga[s]
            else:
                print("Sizning balingiz bunga yetmaydi!") 

        return f"{player.name} siz yutib olgan sovg'alar: {c.Back.WHITE + c.Fore.RED + c.Style.BRIGHT} {self.olingan_sovgalar} "