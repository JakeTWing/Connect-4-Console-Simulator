import os
class board:
    
    def clear_console():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
            
          
            
    def __init__(self, grid = None):
        if grid == None:
            self.grid = [[" " for j in range(7)] for i in range(6)]
        else:
            self.grid = grid
        
        
    def ret_grid(self):
        return self.grid
    
    
    def ret_grid_copy(self):
        ret_grid = [row[:] for row in self.grid]

            
        return ret_grid
    
    
    def remove_peice(self, col): #removes the top peice from a chosen colum
        
        for i in range(len(self.grid)):
            
            if self.grid[i][col] != " ":
                self.grid[i][col] = " "
                break
            
    
    def print_grid(self):
        for row in self.grid:
            print(row)
            
            
    def clear_board(self):
        
        self.grid = [[" " for j in range(7)] for i in range(6)]
        
        
    def update_grid(self, new_grid):
        self.grid = new_grid
    #places a peice on the board with the selected column
    def place_peice(self, is_player_x, chosen_column, print_error = True):

        error_message = ""
        valid_move = True
        
        if is_player_x:
            player_peice = "x"
        else:
            player_peice = "o"

        if chosen_column < 0 or chosen_column > 6: #checks for a valid column number
            valid_move = False
            if print_error:
                print(f"column must be in the range 0 to 6; you chose {chosen_column}")
            return valid_move #ending
        
        if self.grid[0][chosen_column] != " ": #if column is full send a error message and od nothing
            valid_move = False
            if print_error:
                print(f"chosen column is full, select a column different than {chosen_column}")
            return valid_move #ending
        
        #updating board
        for i in range(len(self.grid) - 1, -1, -1):
            if self.grid[i][chosen_column] == " ":
                self.grid[i][chosen_column] = player_peice
                break
            
        return valid_move

    
        
    
    
        
        #checks for a win for a player
        #inputs: is_player_x - boolean, true for x, false for o
        #outputs: win - is there a win for this player ; location - grid cords to the connection
    def check_for_win(self, is_player_x, connection_length = 4):
        #grid of player peice
        only_peice_grid = []
        win = False
        location = []
        
        if is_player_x:
            player_peice = "x"
        else:
            player_peice = "o"
                
            
        for outer, row in enumerate(self.grid): #outer loop
            only_peice_row = [] #row of only the players peices
            for inner, col in enumerate(self.grid[0]): #inner loop
                if self.grid[outer][inner] == player_peice: #if its the player's peice, add it to the row
                    only_peice_row.append(player_peice)
                else:
                    only_peice_row.append(" ") #add a blank
            only_peice_grid.append(only_peice_row) #append the row
            
        
        
        draw = self.check_for_draw()
        if draw:
            return win, location, draw
        
        #Use methods to check for win
        win, location = self.check_horizontal(only_peice_grid, connection_length)
        if win:
            return win, location, draw
                    
        win, location = self.check_vertical(only_peice_grid, connection_length)
        if win:
            return win, location, draw
        win, location = self.check_diagonal_left(only_peice_grid, connection_length)
        if win:
            return win, location, draw
                
        win, location = self.check_diagonal_right(only_peice_grid, connection_length)
        
        return win, location, draw
            

    
    #checks for horizontal connections, must have a grid with only one peice type
    #inputs: only_peice_grid - a grid only containing the peices of one player
    #outputs: win - is there a win for this player ; location - grid cords to the connection
    def check_horizontal(self, only_peice_grid, connection_length = 4):
        
        for outer, row in enumerate(only_peice_grid): #rows
            peices_in_a_row = 0 #count of peices in a row
            location = [] #cords to the peices
            for inner, col in enumerate(only_peice_grid[outer]): #columns
                
                
                if peices_in_a_row >= connection_length: #finds 4 in a row
                    
                    return True, location
                
                elif peices_in_a_row > 0 and col == " ":    #resets the count
                   
                    peices_in_a_row = 0
                    location = []
                
                elif col != " ": #finds a peice
                    peices_in_a_row += 1
                    location.append((outer, inner))
                    
            if peices_in_a_row >= connection_length: #finds 4 in a row
                
                return True, location
                
        return False, location
                
    
    
    
    #checks for vertical connections, must have a grid with only one peice type
    #inputs: only_peice_grid - a grid only containing the peices of one player
    #outputs: win - is there a win for this player ; location - grid cords to the connection
    def check_vertical(self, only_peice_grid, connection_length = 4):
        
        
        for outer in range(len(only_peice_grid[0])): #columns
            peices_in_a_row = 0 #count of peices in a row
            location = []                
            for inner in range(len(only_peice_grid) - 1, -1, -1): #rows
            
                current_peice = only_peice_grid[inner][outer] #current peice

                if peices_in_a_row >= connection_length: #finds 4 in a row

                    return True, location
                
                elif peices_in_a_row > 0 and current_peice  == " ": #resets count

                    peices_in_a_row = 0
                    location = []
                
                elif current_peice != " ": #finds a peice
                    peices_in_a_row += 1
                    location.append((inner, outer))
                    

                
                
            if peices_in_a_row >= connection_length: #finds 4 in a row
                return True, location
                
                
            
        return False, location   
    
    
    
    #checks for diagonal left connections, must have a grid with only one peice type 
    #inputs: only_peice_grid - a grid only containing the peices of one player
    #outputs: win - is there a win for this player ; location - grid cords to the connection
    def check_diagonal_left(self, only_peice_grid, connection_length = 4):
        
        for outer, row in enumerate(only_peice_grid): #rows
            peices_in_a_row = 0 #count of peices in a row
            location = [] #cords to the peices
            for inner, col in enumerate(only_peice_grid[outer]): #columns
                
                if col != " ": #if current cords have a peice
                    
                    
                    peices_in_a_row += 1 #increase peices in a row
                    location.append((outer, inner)) #add cords
                    
                    while peices_in_a_row < connection_length: #loops until there are 4 peices in a row
                        
                        try:  
                            #checks for a peice down a row and down a column. row and column must not be a negitive value
                            if only_peice_grid[outer - peices_in_a_row][inner - peices_in_a_row] != " " and not(outer - peices_in_a_row < 0) and not(inner - peices_in_a_row < 0) :
                                
                                
                                location.append((outer - peices_in_a_row, inner - peices_in_a_row)) #adds the cords to location
                                
                                peices_in_a_row += 1 #increases 
                                
                            else: #else
                                
                                
                                peices_in_a_row = 0 #reset to 0
                                location = [] #reset to blank
                                break #break the loop
                            

                        except IndexError: #index error
                            
                            peices_in_a_row = 0 #reset to 0
                            location = [] #reset to blank
                            break #break the loop
                        
                if peices_in_a_row >= connection_length: #finds 4 in a row
                    
                    return True, location
          

        return False, location  
        
    
    
    
    
    
    #checks for diagonal right connections, must have a grid with only one peice type
    #inputs: only_peice_grid - a grid only containing the peices of one player
    #outputs: win - is there a win for this player ; location - grid cords to the connection
    def check_diagonal_right(self, only_peice_grid, connection_length = 4):
        
        for outer, row in enumerate(only_peice_grid): #rows
            peices_in_a_row = 0 #count of peices in a row
            location = [] #cords to the peices
            for inner, col in enumerate(only_peice_grid[outer]): #columns
                
                if col != " ":
                    
                    
                    peices_in_a_row += 1
                    location.append((outer, inner))
                    
                    while peices_in_a_row < connection_length:
                        
                        try: 
                            
                            if only_peice_grid[outer - peices_in_a_row][inner + peices_in_a_row] != " " and not(outer - peices_in_a_row < 0) and not(inner + peices_in_a_row >= len(only_peice_grid[outer])) :
                                
                                
                                location.append((outer - peices_in_a_row, inner + peices_in_a_row))
                                
                                peices_in_a_row += 1
                            else:
                                
                                
                                peices_in_a_row = 0
                                location = []
                                break
                            

                        except IndexError:
                            
                            peices_in_a_row = 0
                            location = []
                            break
                        
                if peices_in_a_row >= connection_length: #finds 4 in a row
                    
                    return True, location
            
            
    
        return False, location  
    
    
    #returns a boolean, if the game is in a draw
    def check_for_draw(self):
        #loops the top row
        for peice in self.grid[0]:
            if peice == " ":
                return False
        return True
    
    
    
    def __str__(self):
        retStr = "  " + "-----" * 6 + "-  Row\n" #adds the top line to the board
        
        for index, row in enumerate(self.grid):
            
            rowStr = "| " + " | ".join(row) + " |" #temp string, joined each together with | on each side
            retStr += " | " + rowStr + f" | [{index}]\n" #combine to finish the row and add to ret_string; adds the row number in brackets at the end

                
            #len(self.grid) - 1 - index down to up
            #prints the inbetween spaces. Does not print on the final iteration
            if index < len(self.grid) - 1:
                retStr += " |-" + "-----" * 6 + "|\n"
            
            
        retStr += "  " + "-----" * 6 + "-\n" #adds the bottom line to the board
        
        retStr += "Col " 
        for i in range(len(self.grid[0])):
            #adds the bottom numbers for each column
            retStr += f"[{i}] "
        
        
        
        
        return retStr
        
    def __repr__(self):
        return self.__str__()
