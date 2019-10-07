import random


class Game(object):
    
    def __init__(self):
        self.deck = Deck()
        self.player = Player(self.deck)
        self.dealer = Player(self.deck, True)
        self.display_menu()
    
    def start_game(self):
        print("\n\n\n****************************")
        print("      Starting Game!       ")
        print("****************************")
        print(" Dealing your cards...\n")
        
        # Deal player's cards
        self.deal_cards(self.player, 2)
        
        # Deal dealer's cards
        self.deal_cards(self.dealer, 2)
        
        # Check scores
        self.check_scores()
        playerDidHit = self.hit_or_stand()
        
        while self.player.score < 21 and playerDidHit:
            print("\n You hit!")
            self.check_scores()
            playerDidHit = self.hit_or_stand()
        
        self.check_scores()
        
        while self.dealer.score <= 17:
            print("\n Dealer hit!")
            self.dealer.hit()
            self.check_scores()
        
        self.game_over()

    def display_menu(self):
        print("\n")
        print("****************************")
        print("  Welcome to 21 Blackjack! ")
        print("****************************")
        print("        Game Menu \n")
        print(" Play Game............(P) ")
        print(" Instructions.........(I) ")
        print(" Quit.................(Q)\n")
        print("****************************")
        self.prompt_input()
    
    def prompt_input(self):
        print("\nENTER OPTION: ", end = "")
        self.validate_menu_input(input())

    def validate_menu_input(self, option):
        option = option.upper()
        
        if option == "P":
            self.start_game()
        elif option == "I":
            self.display_instructions()
        elif option == "Q":
            exit()
        else:
            print("Invalid input. Must enter 'P', 'I', or 'Q'. Try again.")
            self.prompt_input()

    def display_instructions(self):
        print("\n")
        print("***********************************************************************************")
        print("                                   Instructions")
        print("***********************************************************************************\n")
        print(" - The goal of blackjack is to beat the dealer's hand without going over 21.")
        print(" - Face cards are worth 10. Aces are worth 1 or 11, whichever makes a better hand.")
        print(" - Each player starts with two cards, one of the dealer's cards is hidden until the end.")
        print(" - To 'Hit' is to ask for another card. To 'Stand' is to hold your total and end your turn.")
        print(" - If you go over 21 you bust, and the dealer wins regardless of the dealer's hand.")
        print(" - If you are dealt 21 from the start (Ace & 10), you got a blackjack and win the game.")
        print("\n   PRESS ANY KEY TO RETURN TO THE MAIN MENU")
        input()
        self.display_menu()
    
    
    def game_over(self):
        print("\n")
        print("**********************************")
        print("            Game Over            ")
        print("**********************************\n")
        
        self.display_cards(self.player)
        self.display_cards(self.dealer, True)
        
        print("")
        
        playerScore = self.player.score
        dealerScore = self.dealer.score
        
        print("**********************************")
        print(' Your Score: {0}'.format(playerScore))
        print(' Dealer\'s Score: {0}'.format(dealerScore))
        print("**********************************")
        
        if playerScore == 21:
            print(" You hit Blackjack! YOU WON!")
        elif dealerScore == 21:
            print(" Dealer hit Blackjack! YOU LOST!")
        elif playerScore > 21:
            print(" Bust, you went over 21! YOU LOST!")
        elif dealerScore > 21:
            print(" The dealer bust! YOU WON!")
        elif playerScore > dealerScore:
            print("            YOU WON!")
        elif playerScore < dealerScore:
            print("            YOU LOST!")
        else:
            print("              DRAW!")
        print("**********************************\n\n")
        exit()
    
    
    def check_scores(self):
        self.display_cards(self.player)
        self.display_cards(self.dealer)
        
        if self.player.score >= 21 or self.dealer.score >= 21:
            self.game_over()
    
    def deal_cards(self, player, amount):
        for i in range(amount):
            player.hit()


    def display_cards(self, player, gameOver=False):
        if player.isDealer:
            if len(player.hand) == 2 and not gameOver:
                print(' Dealer\'s Hand: [?, {0}]'.format(player.hand[1]))
            else:
                print(" Dealer's Hand: [", end = "")
                for i in range(len(player.hand)):
                    if i == len(player.hand) - 1:
                        print('{0}]'.format(player.hand[i]))
                    else:
                        print(player.hand[i], end = ", ")
        else:
            print(" Your Hand: [", end = "")
            for i in range(len(player.hand)):
                if i == len(player.hand) - 1:
                    print('{0}]'.format(player.hand[i]))
                else:
                    print(player.hand[i], end = ", ")

    def hit_or_stand(self):
        print("\n")
        print(" Do you wish to hit or stand? (h/s): ", end = "")
        return self.validate_hit_stand_input(input())

    def validate_hit_stand_input(self, option):
        option = option.lower()
        
        if option == "h":
            self.player.hit()
            return True
        elif option == "s":
            return False
        else:
            print(" Invalid input. Must enter 'h' or 's'. Try again.")
            return self.hit_or_stand()


class Deck(object):
    """A Deck contains all traditional 52 cards."""
    
    def __init__(self):
        self.get_new_deck()
    
    def draw_card(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)

    def get_new_deck(self):
        self.cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"] * 4
        self.shuffle()


class Player(object):
    
    def __init__(self, deck, isDealer=False):
        self.deck = deck
        self.isDealer = isDealer
        self.hand = []
        self.score = 0

    def hit(self):
        self.hand.append(self.deck.draw_card())
        self.score = self.getScore()

    def getScore(self):
        score, ace_counter = 0, 0
        
        for card in self.hand:
            if card == "J" or card == "Q" or card == "K":
                score += 10
            elif card != "A":
                score += card
            else:
                ace_counter += 1
    
        if ace_counter > 0:
            return optimal_score(score, ace_counter)
        return score


""" Utils """
aceValues = {1: [1, 11],
             2: [2, 12],
             3: [3, 13],
             4: [4, 14]}

def optimal_score(score, numberOfAces):
    
    potential_scores = []
    for pts in aceValues[numberOfAces]:
         potential_scores.append(score + pts)
    valid_scores = [val for val in potential_scores if val <= 21]
    if valid_scores:
        return max(valid_scores)
    return min(potential_scores)



# START GAME
game = Game()
