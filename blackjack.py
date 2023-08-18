import random

def show_card(cards):
    if cards == None:
        print(cards)
    else:
        print(f"Your cards are {cards}")
deck = list()
for i in range(1,10):
    for j in range(4):
        deck.append(i)
for i in range(52-len(deck)):
    deck.append(10)
status = 1
random.shuffle(deck)
1
while(status == 1):
    print("Do you want to play?")
    decision = input("1 = yes or 0 = No :\n")
    if int(decision) == 1:
        random.shuffle(deck)
        your_cards = [deck[0], deck[2]]
        opponent_cards = [deck[1], deck[3]]
        show_card(your_cards)
        choice = input("Do you want new card?:\n")
        if int(choice) == 1:
            while(int(choice) == 1):
                index = 4
                your_cards.append(deck[index])
                opponent_cards.append(deck[index+1])
                index += 1
                show_card(your_cards)
                choice = input("Do you want new card?:\n")
        
        your_sum = sum(your_cards)
        opponent_sum = sum(opponent_cards)
        if abs(your_sum - 21) < abs(opponent_sum - 21):
            print("you have won")
            print(f"yours cards ")
            show_card(your_cards)
            print(f"opponets cards ")
            show_card(opponent_cards)
        else:
            print("you have lost")
            print(f"yours cards ")
            show_card(your_cards)
            print(f"opponets cards ")
            show_card(opponent_cards)

    else:
        print("This is the end")
        status = 0

