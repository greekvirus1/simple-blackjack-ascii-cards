import random, time

SPADES = chr(9824)
CLUBS = chr(9827)
HEARTS = chr(9829)
DIAMONDS = chr(9830)

def main():
    print("""Welcome to Blackjack. The goal of the card
game is for the player to go as close to, but not over,
'21' than the dealer.

JACK, QUEEN and KING are all value '10'.
ACE is '1' or '11'.
At the start of the game, the player is given 2 cards and the dealer 2 cards.
The dealer keeps one card turned over until the player is done with their turn.
In two hands of equal value, the hand with the least cards is stronger.
In case of a draw, bet is returned.
Blackjack (hand value of '21' with just two cards) has 3-2 increased payout.
The dealer will hit until soft 17.
The dealer will stand on hand values of 17 and over.
The dealer's strategy doesn't depend on the player's hand.

Available actions:

(H)it: Draw one more card
(S)tand: End your turn
(D)ouble-down: On your first draw you can double your bet
and draw exactly one more card, then stand.""")

    input("Press 'Enter' to continue:")
    money = 500
    while True:
        #Game Start
        deck = getDeck()
        print("")
        print("The Dealer shuffles the deck.")
        time.sleep(1)
        print("You are dealt 2 cards...")
        playerHand = [deck.pop(), deck.pop()]
        dealerHand = [deck.pop(), deck.pop()]
        bet = getBet(money)
        money -= bet
        showHiddenCard = False
        while True:
            #Player Actions
            time.sleep(1)
            displayHands(money, bet, playerHand, dealerHand, showHiddenCard)
            action = getAction(playerHand)
            if action == "s":
                showHiddenCard = True
                print("'Stand.'")
                break
            elif action == "h":
                print("'Hit.'")
                playerHand.append(deck.pop())
                if getHandValue(playerHand) >= 21:
                    showHiddenCard = True
                    break
            else:
                print("'Double Down.'")
                money -= bet
                bet *= 2
                playerHand.append(deck.pop())
                showHiddenCard = True
                break
        while True:
            #Dealer Actions
            if getHandValue(playerHand) > 21:
                time.sleep(1)
                displayHands(money, bet, playerHand, dealerHand, showHiddenCard)
                print("You have bust and lose your bet.")
                time.sleep(1)
                print("'Bad luck, Chum.")
                time.sleep(1)
                print("Type 'q' to Quit. Press 'Enter' to continue. ")
                if input("> ").lower().startswith("q"):
                    print("You walk away with {} money.".format(money))
                    exit()
                else:
                    break
            while True:
                time.sleep(2)
                displayHands(money, bet, playerHand, dealerHand, showHiddenCard)
                if getHandValue(dealerHand) <17:
                    print("The dealer draws a card...")
                    dealerHand.append(deck.pop())
                elif getHandValue(dealerHand) <= 21:
                    print("The dealer stands...")
                    break
                else:
                    break
            time.sleep(6)
            displayHands(money, bet, playerHand, dealerHand, showHiddenCard)
            dealerValue = getHandValue(dealerHand)
            playerValue = getHandValue(playerHand)
            if dealerValue > 21:
                time.sleep(1)
                print("The dealer has bust! You win.")
                print("'The house always wins in the end, Chum.'")
                if playerValue == 21 and len(playerHand) == 2:
                    time.sleep(0.5)
                    print("As you have blackjack your payout increases")
                    time.sleep(0.5)
                    print("You win {}!".format(round(bet*1.5)+ bet))
                    print("'Hmm.'")
                    money += (round(bet*1.5) + bet)
                else:
                    print("You win {}!".format(bet))
                    print("The House always wins in the end, Chum.")
                    time.sleep(0.5)
                    money += 2*bet
            elif playerValue > dealerValue:
                if playerValue == 21 and len(playerHand) == 2:
                    time.sleep(0.5)
                    print("As you have blackjack your payout increases")
                    time.sleep(0.5)
                    print("You win {}!".format(round(bet*1.5)))
                    print("'Dang.'")
                    money += (round(bet*1.5) + bet)
                else:
                    print("You win {}!".format(bet))
                    print("The House always wins in the end, Chum.")
                    time.sleep(0.5)
                    money += 2*bet
            elif dealerValue > playerValue:
                time.sleep(0.5)
                print("The dealer wins, you lose your bet.")
                print("'Bad luck, Chum.'")
            else:
                if len(playerHand) < len(dealerHand):
                    if playerValue == 21 and len(playerHand) == 2:
                        time.sleep(0.5)
                        print("As you have blackjack your payout increases")
                        time.sleep(0.5)
                        print("You win {}!".format(round(bet*1.5)))
                        print("'Ugh.'")
                        money += (round(bet*1.5) + bet)
                    else:
                        print("You win {}!".format(bet))
                        print("The House always wins in the end, Chum.")
                        time.sleep(0.5)
                        money += 2*bet
                elif len(playerHand) < len(dealerHand):
                    time.sleep(0.5)
                    print("The dealer wins, you lose your bet.")
                    print("'Bad luck, Chum.'")
                elif len(dealerHand) > len(playerHand):
                    time.sleep(0.5)
                    print("The dealer wins, you lose your bet.")
                    print("'Bad luck, Chum.'")
                else:
                    print("It's a draw, you get your bet back.")
                    money += bet
                    print("'Close, but no cigar, Chum.")
            time.sleep(1)
            print("Type 'q' to Quit. Press 'Enter' to continue. ")
            if input("> ").lower().startswith("q"):
                print("You walk away with {} money.".format(money))
                exit()
            else:
                break




def getDeck():
    cardValues = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    cardColours =[SPADES, CLUBS, HEARTS, DIAMONDS]
    deck = []
    for value in cardValues:
        for colour in cardColours:
            deck.append((value, colour))
    random.shuffle(deck)
    return deck


def getHandValue(hand, showHiddenCard = True):
    value = 0
    aces = 0
    if showHiddenCard:
        for card in hand:
            if (card[0] == "J") or (card[0] == "Q") or (card[0] == "K"):
                value += 10
            elif card[0] == "A":
                aces += 1
            else:
                value += card[0]
    else:
        for card in hand[1::]:
            if (card[0] == "J") or (card[0] == "Q") or (card[0] == "K"):
                value += 10
            elif card[0] == "A":
                aces += 1
            else:
                value += card[0]
    if aces > 0:
        if 11 + value + aces - 1 > 21:
            value += aces
        else:
            value += 11 + aces - 1
    return value


def displayCards(hand, showHiddenCard = True):
    if showHiddenCard:
        rows = ["    ","    ","    ","    "]
        rows[0] += " ___  " * len(hand)
        for card in hand:
            cardTop = "{}  ".format(card[0])
            cardBtm = "__{}".format(card[0])
            rows[1] += "|" + cardTop[0:3] + "| "
            rows[2] += "| {} | ".format(card[1])
            rows[3] += "|" + cardBtm[-3:] + "| "
    else:
        rows = ["     ___  ", "    |## | ", "    | # | ", "    |_##| "]
        rows[0] += " ___  " *(len(hand) - 1)
        for card in hand[1:]:
            cardTop = "{}  ".format(card[0])
            cardBtm = "__{}".format(card[0])
            rows[1] += "|" + cardTop[0:3] + "| "
            rows[2] += "| {} | ".format(card[1])
            rows[3] += "|" + cardBtm[-3:] + "| "
    displayThis = ""
    for row in rows:
        displayThis += row + "\n"
    return displayThis


def getBet(money):
    while True:
        try:
            print("Please input bet: (Money = {})".format(money))
            bet = int(input("> "))
            if bet <= money:
                break
            else:
                print("Not enough money!")
        except:
            print("Invalid bet. Try again.")
    return bet


def displayHands(money, bet, playerHand, dealerHand, showHiddenCard=False):
    
    print("""
Money: {}
Bet: {}
Dealer: {}
{}
Player: {}
{}""".format(money, bet, getHandValue(dealerHand, showHiddenCard), displayCards(dealerHand, showHiddenCard), getHandValue(playerHand), displayCards(playerHand)))
    if (len(playerHand) == 2) and (showHiddenCard == False) and (bet*2 <= money):
        print("""
Actions:
    (H)it
    (S)tand
    (D)ouble-down""")
    elif showHiddenCard == False:
        print("""
Actions:
    (H)it
    (S)tand""")


def getAction(playerHand):
    while True:
        if len(playerHand) == 2:
            print("Input action:")
            action = input("> ")
            if action.lower().startswith("h") or action.lower().startswith("s") or action.lower().startswith("d"):
                return action
            else:
                print("Invalid input. Please try again")
        else:
            print("Input action:")
            action = input("> ")
            if action.lower().startswith("h") or action.lower().startswith("s"):
                    return action
            else:
                    print("Invalid input. Please try again")



#############################
#############################
if __name__ == "__main__":
    main()
#############################
#############################
