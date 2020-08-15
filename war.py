import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Deck:
    def __init__(self):
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
        
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        if len(self.all_cards) > 0:
            return self.all_cards.pop()
        
        
class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + ' of ' + self.suit
    
class Player:
    def __init__(self,name):
        self.name = name
        self.all_cards = []
    
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
        
    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards"
         
    def print_player_cards(self):
        print(f'Player {self.name} cards:')
        for cardsPlayer in self.all_cards:
            print(cardsPlayer)
        print('')
    
def split_cards():
    for i in range(int(len(new_deck.all_cards)/2)):     #half of the deck
        player1.add_cards(new_deck.deal_one())
        player2.add_cards(new_deck.deal_one())
        
if __name__ == "__main__":
    
    new_deck = Deck()
    new_deck.shuffle()
    player1 = Player("1")
    player2 = Player("2")
    split_cards()
    
    round = 0
    game_on=True
    
    while game_on:
        round +=1
        
        if len(player1.all_cards) == 0:
            print(f"Player {player2.name} wins!")
            break
        if len(player2.all_cards) == 0:
            print(f"Player {player1.name} wins!")
            break
        
        print(f"Round {round}:")
        
        player1_cards = []
        player1_cards.append(player1.remove_one())
        player2_cards = []
        player2_cards.append(player2.remove_one())
        
        print(f"Player {player1.name} card is: {player1_cards[0]}")
        print(f"Player {player2.name} card is: {player2_cards[0]}")
        
        if player1_cards[0].value > player2_cards[0].value:
            print(f"Player {player1.name} won round {round}")
            player1.add_cards(player1_cards)
            player1.add_cards(player2_cards)
            
        elif player1_cards[0].value < player2_cards[0].value:
            print(f"Player {player2.name} won round {round}")
            player2.add_cards(player1_cards)
            player2.add_cards(player2_cards)
            
        else:
            print("_"*15 + "WAR" + "_"*15)
            if len(player1.all_cards)<5:
                print(f"Player {player1.name} unable to declare war")
                print(f"Player {player2.name} wins!")
                game_on = False
            elif len(player2.all_cards)<5:
                print(f"Player {player2.name} unable to declare war")
                print(f"Player {player1.name} wins!")
                game_on = False
            else:
                for i in range (5):
                    player1_cards.append(player1.remove_one())
                    player2_cards.append(player2.remove_one())

                print(f"Player {player1.name} card is: {player1_cards[-1]}")
                print(f"Player {player2.name} card is: {player2_cards[-1]}")
                
                if player1_cards[-1].value > player2_cards[-1].value:
                    print(f"Player {player1.name} won round {round}")
                    player1.add_cards(player1_cards)
                    if len(player2_cards)>0:
                        player1.add_cards(player2_cards)
                    war=False
                
                elif player1_cards[-1].value < player2_cards[-1].value:
                    print(f"Player {player2.name} won round {round}")
                    player2.add_cards(player2_cards)
                    if len(player1_cards)>0:
                        player2.add_cards(player2_cards)
                    war=False
        
        if round == 10000:       #avoid infinite loops
            print("Tie")
            game_on=False        
   
    #player1.print_player_cards()
    #player2.print_player_cards()