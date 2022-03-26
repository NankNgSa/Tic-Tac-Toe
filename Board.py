
class Board:
    
    def __init__(self):
        self.player = "x"
        self.round = 0

# -----------------------------------------------------------------------------------

    # print the board on screen
    def print_board(self, b):
        print(" " +b[0] +" | " +" " +b[1] +" | " +b[2] +" ")
        print("---+----+---")
        print(" " +b[3] +" | " +" " +b[4] +" | " +b[5] +" ")
        print("---+----+---")
        print(" " +b[6] +" | " +" " +b[7] +" | " +b[8] +" ")

# -----------------------------------------------------------------------------------

    # launch play
    def play(self, b):
        
        while self.round < 9:         
            print("> round of player : " +self.player)

            try:
            # we do -1 because the index starts from 0 to 9
                move = int(input("enter a number between 1 & 9 : ")) - 1
                    
            # if the box is empty, we write in the box chosen by the player
            # and we continue with the next round with the next player
                if b[move] == " ":
                    b[move] = self.player
                    self.round += 1
                    print()
                    self.print_board(b)              
                else:
                    print("/!\ Choose another case...")
                    print()
                    continue          

                # after each move, we check if the player has won
                if self.check_win(b) == True:
                    print()
                    print("the player " +self.player +" won the game !")
                    break
                
                # after each move, we change the player
                self.player = "o" if self.player == "x" else "x"

                # after 9 round, we end the game because the board has 9 cases
                if self.round == 9:
                    print("end game !")

            # when the player doesn't enter a number, recall the function
            except:
                self.play(b)
                break


# ----------------------------------------------------------------------------------- 
          
    # check that we have won in row
    def check_win_row(self, b):
        if (b[0] == b[1] == b[2] != " " or 
            b[3] == b[4] == b[5] != " " or 
            b[6] == b[7] == b[8] != " "): 
            return True
        else:
            return False

# ---------------------------------------------

    # check that we have won in column
    def check_win_colomn(self, b):
        if (b[0] == b[3] == b[6] != " " or 
            b[1] == b[4] == b[7] != " " or 
            b[2] == b[7] == b[8] != " "): 
            return True
        else:
            return False

# ---------------------------------------------

    # check that we have won in diagonal
    def check_win_diagonal(self, b):
        if (b[0] == b[4] == b[8] != " " or 
            b[2] == b[4] == b[6] != " "):
            return True
        else:
            return False

# ---------------------------------------------

    # check that we have won whatever the case : row / column / diagonal
    def check_win(self, b):
        if (self.check_win_colomn(b) == True or 
            self.check_win_diagonal(b) == True or 
            self.check_win_row(b) == True):
            return True
        else:
            return False


    














