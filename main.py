from letItRide import *
from card import initDeckCardList

deck = initDeckCardList()
game = LetItRideGame(deck)

initMoney = 500
initBet = 50
print("Start money = {}".format(initMoney))
print("Start bet = {}".format(initBet))
player = Player(initMoney)

while True:
    game.startGame(initBet, player)
    print("\nYour cards: {}\nYour bets: {}".format(player.getCards(), player.getBets()))

    if int(input('1 - let it ride; 0 - pull bet: ')) == 0:
        player.pullBet()
    print("Your bets: {}".format(player.getBets()))
    game.nextStage()
    print("\nYour cards: {}\nYour bets: {}".format(player.getCards(), player.getBets()))

    if int(input('1 - let it ride; 0 - pull bet: ')) == 0:
        player.pullBet()
    print("Your bets: {}".format(player.getBets()))
    game.nextStage()

    print("\nYour money: {}".format(player.getMoney()))
    if int(input("Continue? 1/0: ")) == 0:
        break
