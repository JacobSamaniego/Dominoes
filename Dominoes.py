import random
#Generates 28 dominoe variations
class CDominoes:
    def __init__(self):
        self.dominoes = []
        self.createDominoes()

    def createDominoes(self):
        for i in range(7):
            for j in range(i, 7):
                self.dominoes.append((i,j))
    
    
    def get_dominoes(self):
        return self.dominoes

#Randomizes the domino list
class CRandom:
    def mix(dominoes):    
        random.shuffle(dominoes)
        return dominoes


# Main function
def main():
    # Initialize the domino set and shuffle it
    domino_set = CDominoes()  # Create a CDominoes object which generates all 28 domino pieces
    CRandom.mix(domino_set.get_dominoes())  # Shuffle the domino pieces using the CRandom class

    # Initialize players with 10 random pieces each
    all_pieces = domino_set.get_dominoes()  # Get the shuffled domino pieces
    player1 = CPlayer(all_pieces[:10])  # Assign the first 10 pieces to player 1
    player2 = CPlayer(all_pieces[10:20])  # Assign the next 10 pieces to player 2
    remaining_pieces = all_pieces[20:]  # The last 8 pieces are left as the remaining pool for drawing

    # Initialize the table where domino pieces will be placed
    table = CTable()  # Create a CTable object to manage the dominoes played on the table

    # Randomly decide who starts the game
    current_player = random.choice([0, 1])  # Randomly select either player 1 or player 2 to start

    # The selected player places the first piece
    first_player = player1 if current_player == 0 else player2  # Determine which player starts
    first_piece = first_player.place_first_piece()  # The starting player places the first piece from their hand
    table.place_piece(first_piece)  # Place the first piece on the table
    print(f"First piece placed by Player {current_player + 1}: [{first_piece[0]}|{first_piece[1]}]")

    game_ended = False  # Variable to track if the game has ended
    both_players_passed = False  # Variable to track if both players have passed consecutively

    # Game loop
    while not game_ended:
        # Determine the current player (player1 if current_player is 0, otherwise player2)
        player = player1 if current_player == 0 else player2

        # Display the current player's turn and their hand
        print(f"\nPlayer {current_player + 1}'s turn")
        print(f"Player {current_player + 1}'s hand: {player.display_hand()}")

        player_passed = False  # Flag to indicate if the current player passed their turn

        # Try to place a piece on the table by matching it with the head or tail
        try:
            piece = player.play_piece(table.get_head(), table.get_tail())  # Find a piece that matches either the head or tail
            table.place_piece(piece)  # Place the matching piece on the table
            print(f"Placed piece: [{piece[0]}|{piece[1]}]")
            print(f"Table: {table.display_table()}")
            both_players_passed = False  # Reset since a valid move was made

            # Check if the current player has won (has no more pieces)
            if not player.has_pieces():
                print(f"Player {current_player + 1} wins!")  # Announce the winner
                game_ended = True  # End the game
                break  # Exit the game loop
        except ValueError:
            # If no matching piece can be found, the player needs to draw a piece
            print("No match found, drawing a piece...")
            if remaining_pieces:  # Check if there are still pieces to draw from the pool
                drawn_piece = remaining_pieces.pop()  # Draw one piece from the remaining pieces
                print(f"Drawn piece: [{drawn_piece[0]}|{drawn_piece[1]}]")
                player.draw_piece(drawn_piece)  # Add the drawn piece to the player's hand
            else:
                # If there are no more pieces to draw, the player passes their turn
                print("No more pieces to draw, passing turn.")
                player_passed = True

        # Check if both players have passed their turn consecutively
        if player_passed:
            if both_players_passed:  # If both players have passed consecutively, the game ends in a draw
                print("Both players passed. The game ends in a draw!")
                game_ended = True  # End the game
            else:
                both_players_passed = True  # Mark the current player as having passed
        else:
            both_players_passed = False  # Reset the pass flag if a piece was successfully placed

        # Switch to the next player (0 -> 1, or 1 -> 0)
        current_player = (current_player + 1) % 2  # Alternates between player 0 and player 1

if __name__ == "__main__":
    main()
