![Blackjack](blackjack.jpg "Blackjack")
# Welcome to Blackjack!
The best single-player game in the world!

# Get Started 
1. Download the ```blackjack.py``` file. 
2. On your terminal, run either ```python blackjack.py``` or ```python3 blackjack.py```. 
3. You're ready to go!

 # Rules 
- The goal of blackjack is to beat the dealer's hand without going over 21.
- Face cards are worth 10. Aces are worth 1 or 11, whichever makes a better hand.
- Each player starts with two cards, one of the dealer's cards is hidden until the end.
- To 'Hit' is to ask for another card. To 'Stand' is to hold your total and end your turn.
- If you go over 21 you bust, and the dealer wins regardless of the dealer's hand.
- If you are dealt 21 from the start (Ace & 10), you got a blackjack.
- Blackjack usually means you win 1.5 the amount of your bet. Depends on the casino.
- Dealer will hit until his/her cards total 17 or higher.

# Design Choices
I created 3 classes for this game: **Game**, **Player**, and **Deck**.

- **Game**: The Game class controls the entire flow of the game. It is responsible for creating the 2 players, 
one being the Dealer, and the other being the user, as well as holding the game deck, and displaying the text-based UI for the game. 

- **Player**: The Player class holds the player's current hand and calculates its value. To calculate a player's score, I had to keep
a special case in mind which is the Ace card being able to take on the value of either a 1 or 11. For this, I created a function named
```optimal_score``` which takes in the score of a hand (without including any Aces) along with the number of Aces in the hand. 
Based on that information, the function calculates the highest score you can get without busting (going over 21). To help with that,
I created a dictionary with the key being the number of Ace cards (1-4) in a player's hand and the value being a list of the 
possible points the Ace cards would add to the hand. For example, if you have a score of 6 (before counting Aces) and you have 2 
Aces, then that means you could add either 2 or 12 to your current score. Since 12 is bigger and adding it to 6 won't put you over 21, then
it will assign that score to the player. 

- **Deck**: The Deck class creates a deck of 52 cards, shuffles them, and allows you to draw a card from it. 
The Deck uses an array to store the cards. I chose an array for its simplicity, and for the ability to use the ```random``` 
library in order to be able to shuffle the array as you would for a real deck. 




