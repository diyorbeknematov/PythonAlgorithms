from poleChudes.player import Player
from poleChudes.magazine import Magazine
from poleChudes.play import Play, savollar
from time import sleep
from os import system
import colorama as c
c.init(autoreset=True)

play = Play('Poli')
m = Magazine()
p1 = Player("Anvar", play, m)
p2 = Player("Akobir", play, m)
p3 = Player("Sherzod", play, m)

print(f"{c.Back.LIGHTBLUE_EX + c.Fore.BLACK + c.Style.BRIGHT} Assalomu alaukum {c.Style.RESET_ALL} 👋")
print(f"{c.Back.WHITE + c.Fore.BLUE + c.Style.BRIGHT} POLE CHUDES {c.Style.RESET_ALL} {c.Fore.GREEN + c.Style.DIM}o'yiniga xush kelibsiz {c.Style.RESET_ALL}")
print(f"Bugungi ishtirokchilarimiz\n    {p1.getName()}\n    {p2.getName()}\n    {p3.getName()}\n")
print(f"🤗🤩😁 {c.Back.WHITE + c.Fore.RED + c.Style.BRIGHT} Bugungi o'yinni boshladik {c.Style.RESET_ALL}\n")
savol = savollar()
s1 = play.SavolTanlash(savol)
javob = "*"*len(savol[s1])

while True:
    javob = p1.sayLatter(savol[s1], javob, s1)
    if play.checkWinner(savol[s1], javob):
        sleep(2)
        system("cls")
        print(f"{p1.getName().upper()} 😍😍😍Siz g'alaba qozondingiz👌👌👌")
        p1.sovgaOlish()
        break

    javob = p2.sayLatter(savol[s1], javob, s1)
    if play.checkWinner(savol[s1], javob):
        sleep(2)
        system("cls")
        print(f"{p2.getName().upper()} 😍😍😍Siz g'alaba qozondingiz👌👌👌")
        p2.sovgaOlish()
        break

    javob = p3.sayLatter(savol[s1], javob, s1)
    if play.checkWinner(savol[s1], javob):
        sleep(2)
        system("cls")
        print(f"{p3.getName().upper()} 😍😍😍Siz g'alaba qozondingiz👌👌👌")
        p3.sovgaOlish()
        break
