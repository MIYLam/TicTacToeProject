#constructing the game board
gameState = [["_","_","_","_","_"],["|"," "," "," ","|"],["|"," "," "," ","|"],["|"," "," "," ","|"],["-","-","-","-","-"]]
winner = False
#printing the game board
for i in gameState:
    print(' '.join(i))


# a turn 
def game_process(turn):
    
    #crosses always goes first, which happens to have it end up on even numbered turns
    if turn % 2 == 0:
        prompt = "Where should x be played? Input format: (row,column)"
    
    
    #naughts go second, which means it gets odd numbered turns
    elif turn % 2 == 1: 
        prompt = "Where should o be played? Input format: (row,column)"
   
   
    #integration of a validation method
    validation = False 
    while not validation:   
        print("\n")
        position = input(prompt + "\n")
        
        try:
            answer = position.split(",")  #Splitting the user input into the relevant information 
            true_row = int(answer[0]) 
            true_column = int(answer[1])
            if gameState[true_row][true_column] != " ":
                print("There is already a symbol there")
                continue
            if len(answer) != 2:
                print("Please enter valid coordinates")
                continue
            if (true_column or true_row) > 3:
                print("Please enter valid coordinates")
                continue
            validation = True   
        except:
            print("Please enter valid input")
            continue
        
        
        return true_row, true_column


#function to place a piece on the board
def placing_piece(turn,row,column):  
    if turn % 2 == 0: 
        
        gameState[row][column] = "x"
      
    elif turn % 2 == 1: 
       
        gameState[row][column] = "o"    

    print("\n" * 10)        
    for i in gameState:
        print(' '.join(i)) 

    
#function to check for a winner
def winning_check(): 
    diagonal_winner = []
    other_diagonal = [] #these lists are outside of the for loops as they only need to be refered once
    counter = 3

    #checking the up --> down diagonal
    for i in range(3):
        
        diagonal_winner.append(gameState[i+1][i+1])
        
    if diagonal_winner.count(diagonal_winner[1]) == len(diagonal_winner):
        return diagonal_winner[1]
    else:
        pass
    
    #checking the down --> up diagonal
    for i in range(3):    
        
        other_diagonal.append(gameState[i+1][counter])
        counter -= 1
    if other_diagonal.count(other_diagonal[1]) == len(other_diagonal):
        return other_diagonal[1]
    else:
        pass
    
    #checking columns    
    for i in range(3):    
        row_winner = []
        for row in range(3):
            row_winner.append(gameState[row+1][i+1])
                
        if row_winner.count(row_winner[0]) == len(row_winner) and row_winner[0] == ("x" or "o"):
            return row_winner[0]
        else:
            pass   
        
    #checking rows
          
    for i in range(3):
        column_winner = []
        for column in range(3):
            column_winner.append(gameState[i+1][column+1])
        
        if column_winner.count(column_winner[0]) == len(column_winner) and column_winner[0] == ("x" or "o"): #makes sure that its not just the spaces that are there
            return column_winner[1]
        else:
            pass 
            
    return "" #if there is no winner yet
     
    
#main line 
#no one can possibly win within this time, so only the turn sequence is being run 
for i in range(4):
    user_input = list(game_process(i))        
    placing_piece(i, user_input[0], user_input[1])    
#incorporating the mechanisms checking for a winner
for i in range(5):
    user_input = list(game_process(i))        
    placing_piece(i, user_input[0], user_input[1])

    win_state = winning_check()   
    if len(win_state) == 1:
        winner = True
    else:
        continue
    if winner == True: 
        print(win_state + " player has won")
        input()

#ending if there is no winner 
if winner == False: 
    print("This game is a tie")
    input()

    


    
