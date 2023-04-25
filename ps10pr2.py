"""
# ps10pr2.py (Problem Set 10, Problem 2)
#
# A Connect Four Player class 
#@author: airihatori
# A Connect Four Player class  
# Author: Airi Hatori (airi0319@bu.edu), 06/16/2022
"""

from ps10pr1 import Board

# Write your class below.
class Player:
    
    def __init__(self, checker):
        """ constructs a new Player object by initializing an attribute checker 
        and an attribute num_moves. 
        
        an attribute checker - one-character string that represents the 
                               gamepiece for the player, as specified by the 
                               parameter checker 
                               
        an attribute num_moves - an integer that stores how many moves the 
                                 player has made so far. This attribute should 
                                 be initialized to zero to signify that the
                                 Player object has not yet made any Connect Four 
                                 moves. """
        
        assert (checker == 'X' or checker == 'O') 
        
        self.checker = checker    
        self.num_moves = 0                      
        
    def __repr__(self):
        """ returns a string representing a Player object. 
            the string returned should indicate which checker the Player 
            object is using. """
            
        return 'Player' + ' ' + str(self.checker)

    def opponent_checker(self):
        """ returns a one_character string rerpesenting the checker 
        of the player object's opponent. """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
        
    def next_move(self, board):
        """ accepts a Board object b as a parameter and returns the column
            where the player wants to make the next move. """
            
        self.num_moves += 1 
        
        while True:
            #convert the returned string to an integer to get a column number 
            col = int(input('Enter a column: '))
            # if valid column index, return that integer 
            if board.can_add_to(col) == True:
                return col 
            #else, print 'Try again!' and keep looping 
            else:
                print('Try again!')
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
