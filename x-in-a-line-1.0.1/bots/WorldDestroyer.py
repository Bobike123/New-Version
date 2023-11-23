import random
from bots.base_bot import BaseBot
from game.board_cell import BoardCell
from game.colors import Colors
from game.board_cell import BoardCell
from bots.base_bot import BaseBot


class WorldDestroyer(BaseBot):
    truemove=False
    initialLocation=False
    initialLocation_x=0
    initialLocation_y=0
    previous_x=0
    previous_y=0
    direction="n"
    move=0
    def __init__(self, uid):
        self.rand = random.Random(uid)
        self.uid = uid
        self.name = "WorldDestroyer"
        self.color = (0, 0, 0)  # RGB color values, set the values between 0 and 255
        super().__init__(uid, f"{self.__class__.__name__}_{uid}", Colors.get_random_color())
        self.cols = 0
        self.rows = 0
        self.board = [[int]]
    def init_board(self, cols: int, rows: int, win_length: int, obstacles: [(int, int)], time_given: int) -> None:
        self.cols = cols
        self.rows = rows
        self.board = [[BoardCell.CLEAR for _ in range(rows)] for _ in range(cols)]
        for x, y in obstacles:
            self.board[x][y] = BoardCell.BLOCKED
    def check(self,x,y)-> bool:
        if y >= 0 and y < self.cols and x>=0 and y< self.rows:
            return True
        return False
    def check_vertical_up(self,x,y)->bool:      #check up the winning steps(ask for how to get the winning moves)
        if y >= 0 and y < self.cols:      
            for c in range(1, 6):    
                cy = y - c
                if cy < 0 or self.board[x][cy] != BoardCell.CLEAR:
                    return False
            return True
        return False
    def check_vertical_down(self,x,y)->bool:    #check down the winning steps(ask for how to get the winning moves)
        if y >= 0 and y < self.cols:      
            for c in range(1, 6):    
                cy = y + c
                if cy >= self.cols or self.board[x][cy] != BoardCell.CLEAR:
                    return False
            return True
        return False
    def check_orizontal_left(self,x,y)->bool:   #check left the winning steps(ask for how to get the winning moves)
        if x >= 0 and x < self.rows:
            for c in range(1, 6):    
                cx = x - c
                if cx < 0 or self.board[cx][y] != BoardCell.CLEAR:
                    return False
            return True
        return False
    def check_orizontal_right(self,x,y)->bool:  #check right the winning steps(ask for how to get the winning moves)
        if x >= 0 and x < self.rows: 
            for c in range(1, 6):    
                cx = x + c
                if cx >= self.rows or self.board[cx][y] != BoardCell.CLEAR:
                    return False
            return True
        return False
    def check_diagonal_up_r(self,x,y)->bool: #check diagonalupR the winning steps
        c=0
        cx=x
        cy=y
        if y >= 0 and y < self.cols:
            while c!=5:
                cy = y + c
                cx = x - c
                if self.board[cx][cy] !=BoardCell.CLEAR and cx<=0 and cy>self.rows:
                    return False
                c+=1
            return True
        return False
    def check_diagonal_down_r(self,x,y)->bool: #check diagonaldownR the winning steps
        c=0
        cx=x
        cy=y
        if y >= 0 and y < self.cols:
            while c!=5:
                cy = y + c
                cx = x + c
                if self.board[cx][cy] !=BoardCell.CLEAR and cx<=0 and cy>self.rows:
                    return False
                c+=1
            return True
        return False
    def check_diagonal_up_l(self,x,y)->bool: #check diagonaldownL the winning steps
        c=0
        cx=x
        cy=y
        if y >= 0 and y < self.cols:
            while c!=5:
                cy = y - c
                cx = x - c
                if self.board[cx][cy] !=BoardCell.CLEAR and cx<=0 and cy>self.rows:
                    return False
                c+=1
            return True
        return False
    def check_diagonal_down_l(self,x,y)->bool: #check diagonaldownL the winning steps
        c=0
        cx=x
        cy=y
        if y >= 0 and y < self.cols:
            while c!=5:
                cy = y - c
                cx = x + c
                if self.board[cx][cy] !=BoardCell.CLEAR and cx<=0 and cy>self.rows:
                    return False
                c+=1
            return True
        return False
#def if any other bot is

#TODO: CHECK WHICH WAY IS THE WINNING POSITION AND DONT WRITE IN THAT POSITION IF YOU CANNOT WIN
#maybe implement diagonal later but i dont think is necesarry
    def make_a_move(self, time_left: int) -> (int, int):
        self.move=self.move+1
        print(f"Initial X:{self.initialLocation_x}")
        print(f"Initial Y:{self.initialLocation_y}")
        print(f"Previous X:{self.previous_x}")
        print(f"Previous Y:{self.previous_y}")
        print(f"Move number #{self.move}")#number of moves
        while(True):#looking for its next move to conquer the world
            if(self.initialLocation==False):   
                self.direction=""
                x = self.rand.randrange(self.rows)
                y = self.rand.randrange(self.cols)
                if(self.check_diagonal_up_r(x,y)==True):#going up-right
                    self.initialLocation_x=x
                    self.initialLocation_y=y
                    self.previous_x=x
                    self.previous_y=y
                    self.initialLocation=True
                    self.direction="NE"
                    if self.board[x][y]==BoardCell.CLEAR:
                        print(f"This boardcell is clear (x:{x},y:{y})")
                        return x,y
                if(self.check_diagonal_down_r(x,y)==True):#going down-right
                    self.initialLocation_x=x
                    self.initialLocation_y=y
                    self.previous_x=x
                    self.previous_y=y
                    self.initialLocation=True
                    self.direction="SE"
                    if self.board[x][y]==BoardCell.CLEAR:
                        print(f"This boardcell is clear (x:{x},y:{y})")
                        return x,y
                if(self.check_diagonal_up_l(x,y)==True):#going up-left
                    self.initialLocation_x=x
                    self.initialLocation_y=y
                    self.previous_x=x
                    self.previous_y=y
                    self.initialLocation=True
                    self.direction="NW"
                    if self.board[x][y]==BoardCell.CLEAR:
                        print(f"This boardcell is clear (x:{x},y:{y})")
                        return x,y
                if(self.check_diagonal_down_l(x,y)==True):#going down-left
                    self.initialLocation_x=x
                    self.initialLocation_y=y
                    self.previous_x=x
                    self.previous_y=y
                    self.initialLocation=True
                    self.direction="SW"
                    if self.board[x][y]==BoardCell.CLEAR:
                        print(f"This boardcell is clear (x:{x},y:{y})")
                        return x,y
                if(self.check_vertical_up(x,y)==True):#going up
                    self.initialLocation_x=x
                    self.initialLocation_y=y
                    self.previous_x=x
                    self.previous_y=y
                    self.initialLocation=True
                    self.direction="N"
                    if self.board[x][y]==BoardCell.CLEAR:
                        print(f"This boardcell is clear (x:{x},y:{y})")
                        return x,y
                if(self.check_vertical_down(x,y)==True):#going down
                    self.initialLocation_x=x
                    self.initialLocation_y=y
                    self.previous_x=x
                    self.previous_y=y
                    self.initialLocation=True
                    self.direction="S"
                    if self.board[x][y]==BoardCell.CLEAR:
                        print(f"This boardcell is clear (x:{x},y:{y})")
                        return x,y
                if(self.check_orizontal_right(x,y)==True):#going right
                    self.initialLocation_x=x
                    self.initialLocation_y=y
                    self.previous_x=x
                    self.previous_y=y
                    self.initialLocation=True
                    self.direction="E"
                    if self.board[x][y]==BoardCell.CLEAR:
                        print(f"This boardcell is clear (x:{x},y:{y})")
                        return x,y
                if(self.check_orizontal_left(x,y)==True):#going left
                    self.initialLocation_x=x
                    self.initialLocation_y=y
                    self.previous_x=x
                    self.previous_y=y
                    self.initialLocation=True
                    self.direction="W"
                    if self.board[x][y]==BoardCell.CLEAR:
                        print(f"This boardcell is clear (x:{x},y:{y})")
                        return x,y
                else:#if there are no winning moves, only draw so fuck it, go random
                    for _ in range(self.rows * self.cols):
                        x = self.rand.randrange(self.rows)
                        y = self.rand.randrange(self.cols)
                        if self.board[x][y] == BoardCell.CLEAR:
                            self.initialLocation=False
                            self.initialLocation_x=x
                            self.initialLocation_y=y
                            self.direction=""
                            print("Everything is fucked, I go rambo")
                            print(f"This boardcell is clear (x:{x},y:{y})")
                            return x,y
            else:
                x=self.previous_x
                y=self.previous_y
                if(self.direction=="NE"):
                    self.previous_x=x+1
                    self.previous_y=y-1
                    if self.board[x+1][y-1]==BoardCell.CLEAR and self.check(x+1,y-1)==True:
                        print(f"This boardcell is clear (x:{x+1},y:{y-1})")
                        return x+1,y-1
                    else:
                        #print("blocked north")
                        self.direction="SE"
                        x=self.initialLocation_x-1
                        y=self.initialLocation_y+1
                        self.previous_x=x
                        self.previous_y=y
                        if self.board[x][y]==BoardCell.CLEAR and self.check(x,y)==True:
                            print(f"This boardcell is clear (x:{x},y:{y})")
                            return x,y
                        else:
                            for _ in range(self.rows * self.cols):
                                x = self.rand.randrange(self.rows)
                                y = self.rand.randrange(self.cols)
                                if self.board[x][y] == BoardCell.CLEAR:
                                    self.initialLocation=False
                                    self.initialLocation_x=x
                                    self.initialLocation_y=y
                                    self.direction=""
                                    print(f"This boardcell is clear (x:{x},y:{y})")
                                    return x, y
                if(self.direction=="SE"):
                    self.previous_x=x-1
                    self.previous_y=y+1
                    if self.board[x-1][y+1]==BoardCell.CLEAR and self.check(x+1,y-1)==True:
                        print(f"This boardcell is clear (x:{x-1},y:{y+1})")
                        return x-1,y+1
                    else:
                        #print("blocked north")
                        self.direction="NE"
                        x=self.initialLocation_x+1
                        y=self.initialLocation_y-1
                        self.previous_x=x
                        self.previous_y=y
                        if self.board[x][y]==BoardCell.CLEAR and self.check(x,y)==True:
                            print(f"This boardcell is clear (x:{x},y:{y})")
                            return x,y
                        else:
                            for _ in range(self.rows * self.cols):
                                x = self.rand.randrange(self.rows)
                                y = self.rand.randrange(self.cols)
                                if self.board[x][y] == BoardCell.CLEAR:
                                    self.initialLocation=False
                                    self.initialLocation_x=x
                                    self.initialLocation_y=y
                                    self.direction=""
                                    print(f"This boardcell is clear (x:{x},y:{y})")
                                    return x, y
                                
                if(self.direction=="NW"):
                    self.previous_x=x-1
                    self.previous_y=y-1
                    if self.board[x-1][y-1]==BoardCell.CLEAR and self.check(x+1,y-1)==True:
                        print(f"This boardcell is clear (x:{x-1},y:{y-1})")
                        return x-1,y-1
                    else:
                        #print("blocked north")
                        self.direction="SW"
                        x=self.initialLocation_x+1
                        y=self.initialLocation_y+1
                        self.previous_x=x
                        self.previous_y=y
                        if self.board[x][y]==BoardCell.CLEAR and self.check(x,y)==True:
                            print(f"This boardcell is clear (x:{x-1},y:{y-1})")
                            return x,y
                        else:
                            for _ in range(self.rows * self.cols):
                                x = self.rand.randrange(self.rows)
                                y = self.rand.randrange(self.cols)
                                if self.board[x][y] == BoardCell.CLEAR:
                                    self.initialLocation=False
                                    self.initialLocation_x=x
                                    self.initialLocation_y=y
                                    self.direction=""
                                    print(f"This boardcell is clear (x:{x},y:{y})")
                                    return x, y
                

                if(self.direction=="SW"):
                    self.previous_x=x+1
                    self.previous_y=y-1
                    if self.board[x+1][y-1]==BoardCell.CLEAR and self.check(x+1,y-1)==True:
                        print(f"This boardcell is clear (x:{x+1},y:{y-1})")
                        return x+1,y-1
                    else:   
                        #print("blocked north")
                        self.direction="NE"
                        x=self.initialLocation_x-1
                        y=self.initialLocation_y+1
                        self.previous_x=x
                        self.previous_y=y
                        if self.board[x][y]==BoardCell.CLEAR and self.check(x,y)==True:
                            print(f"This boardcell is clear (x:{x},y:{y})")
                            return x,y
                        else:
                            for _ in range(self.rows * self.cols):
                                x = self.rand.randrange(self.rows)
                                y = self.rand.randrange(self.cols)
                                if self.board[x][y] == BoardCell.CLEAR:
                                    self.initialLocation=False
                                    self.initialLocation_x=x
                                    self.initialLocation_y=y
                                    self.direction=""
                                    print(f"This boardcell is clear (x:{x},y:{y})")
                                    return x, y
                if(self.direction=="N"):
                    self.previous_x=x
                    self.previous_y=y-1
                    if self.board[x][y-1]==BoardCell.CLEAR:
                        print(f"This boardcell is clear (x:{x},y:{y-1})")
                        return x,y-1
                    else:
                        #print("blocked north")
                        self.direction="S"
                        x=self.initialLocation_x
                        y=self.initialLocation_y+1
                        self.previous_x=x
                        self.previous_y=y
                        if self.board[x][y]==BoardCell.CLEAR and self.check(x,y)==True:
                            print(f"This boardcell is clear (x:{x},y:{y})")
                            return x,y
                        else:
                            for _ in range(self.rows * self.cols):
                                x = self.rand.randrange(self.rows)
                                y = self.rand.randrange(self.cols)
                                if self.board[x][y] == BoardCell.CLEAR:
                                    self.initialLocation=False
                                    self.initialLocation_x=x
                                    self.initialLocation_y=y
                                    self.direction=""
                                    print(f"This boardcell is clear (x:{x},y:{y})")
                                    return x, y
                if(self.direction=="S"):
                    self.previous_x=x
                    self.previous_y=y+1
                    if self.board[x][y+1]==BoardCell.CLEAR and self.check(x,y)==True:
                        print(f"This boardcell is clear (x:{x},y:{y+1})")
                        return x,y+1
                    else:
                        #print("blocked south")
                        self.direction="N"
                        x=self.initialLocation_x
                        y=self.initialLocation_y+1
                        self.previous_x=x
                        self.previous_y=y
                        if self.board[x][y]==BoardCell.CLEAR and self.check(x,y)==True:
                            print(f"This boardcell is clear (x:{x},y:{y})")
                            return x,y
                        else:
                            for _ in range(self.rows * self.cols):
                                x = self.rand.randrange(self.rows)
                                y = self.rand.randrange(self.cols)
                                if self.board[x][y] == BoardCell.CLEAR and self.check(x,y)==True:
                                    self.initialLocation=False
                                    self.initialLocation_x=x
                                    self.initialLocation_y=y
                                    self.direction=""
                                    print(f"This boardcell is clear (x:{x},y:{y})")
                                    return x, y
                if(self.direction=="E"):
                    self.previous_x=x+1
                    self.previous_y=y
                    if self.board[x+1][y]==BoardCell.CLEAR  and self.check(x,y)==True:
                        print(f"This boardcell is clear (x:{x+1},y:{y})")
                        return x+1,y
                    else:
                        #print("blocked east")
                        self.direction="W"
                        x=self.initialLocation_x
                        y=self.initialLocation_y+1
                        self.previous_x=x
                        self.previous_y=y
                        if self.board[x][y]==BoardCell.CLEAR and self.check(x,y)==True:
                            print(f"This boardcell is clear (x:{x},y:{y})")
                            return x,y
                        else:
                            for _ in range(self.rows * self.cols):
                                x = self.rand.randrange(self.rows)
                                y = self.rand.randrange(self.cols)
                                if self.board[x][y] == BoardCell.CLEAR and self.check(x,y)==True:
                                    self.initialLocation=False
                                    self.initialLocation_x=x
                                    self.initialLocation_y=y
                                    self.direction=""
                                    print(f"This boardcell is clear (x:{x},y:{y})")
                                    return x, y
                if(self.direction=="W"):
                    self.previous_x=x-1
                    self.previous_y=y
                    if self.board[x-1][y]==BoardCell.CLEAR and self.check(x,y)==True:
                        print(f"This boardcell is clear (x:{x-1},y:{y})")
                        return x-1,y
                    else:
                        #print("blocked west")
                        self.direction="W"
                        x=self.initialLocation_x
                        y=self.initialLocation_y+1
                        self.previous_x=x
                        self.previous_y=y
                        if self.board[x][y]==BoardCell.CLEAR and self.check(x,y)==True:
                            print(f"This boardcell is clear (x:{x},y:{y})")
                            return x,y
                        else:
                            for _ in range(self.rows * self.cols):
                                x = self.rand.randrange(self.rows)
                                y = self.rand.randrange(self.cols)
                                if self.board[x][y] == BoardCell.CLEAR and self.check(x,y)==True:
                                    self.initialLocation=False
                                    self.initialLocation_x=x
                                    self.initialLocation_y=y
                                    self.direction=""
                                    print(f"This boardcell is clear (x:{x},y:{y})")                      
#check 1,8 ca ceva nu i ok
    def notify_move(self, bot_uid: int, move: (int, int)) -> None:
        (x, y) = move
        self.board[x][y] = bot_uid


                    
                



#Code that i started working on but it got so fucked i wantet to rewrite everything
#         self.move=self.move+1
#         print(f"Move number #{self.move}")#number of moves
#         print(f"Initial Location x{self.initialLocation_x} and y:{self.initialLocation_y}")
#         while(True):
#             if(self.truemove==False):#random selection at first 
#                 x = self.rand.randrange(self.rows)
#                 y = self.rand.randrange(self.cols)
#                 #restarts again and checks all the directions
#                 if(self.check_vertical_up(x,y)==True):
#                     self.previous_x=x
#                     self.previous_y=y
#                     self.truemove=True
#                     self.direction="n"
#                     return x, y
#                 elif(self.check_vertical_down(x,y)==True):
#                     self.previous_x=x
#                     self.previous_y=y
#                     self.truemove=True
#                     self.direction="s"
#                     return x, y
#                 elif(self.check_orizontal_left(x,y)==True):
#                     self.previous_x=x
#                     self.previous_y=y
#                     self.truemove=True
#                     self.direction="w"
#                     return x, y
#                 elif(self.check_orizontal_right(x,y)==True):
#                     self.previous_x=x
#                     self.previous_y=y
#                     self.truemove=True
#                     self.direction="e"
#                     return x, y
#                 else:
#                     self.truemove=False
#                     self.initialLocation=False
#             else: 
#                 x = self.previous_x
#                 y = self.previous_y
#                 if(self.initialLocation==False):#checks for later ;)
#                     self.initialLocation_x=x
#                     self.initialLocation_y=y
#                     self.initialLocation=True

# #REMAKE THE IVERSION
# #THE REST OF THE CODE RUNS FINE

#                 if(self.direction=="n"):#goes up until win
#                     self.direction="n"
#                     self.truemove=True
#                     print("i got her")
#                     if self.board[x][y-1]== BoardCell.CLEAR:
#                         self.previous_x=x
#                         self.previous_y=y-1
#                         print("GOING UP")
#                         return x, y-1
#                     else:#if up was blocked continues down
#                         self.direction="s"
#                         print("GOING DOWN")
#                         x=self.initialLocation_x
#                         y=self.initialLocation_y
#                         if self.board[self.initialLocation_x][self.initialLocation_y+1]==BoardCell.CLEAR:
#                             return self.initialLocation_x, self.initialLocation_y+1
#                         else:
#                             while True:
#                                 x = self.rand.randrange(self.rows)
#                                 y = self.rand.randrange(self.cols)
#                                 self.initialLocation=False
#                                 if self.board[x][y] == BoardCell.CLEAR:
#                                     return x, y
                            
#                 elif self.direction=="s" :#goes down until win
#                     self.direction="s"
#                     self.truemove=True
#                     print("GOING DOWN")
#                     if self.board[x][y+1]== BoardCell.CLEAR:
#                         self.previous_x=x
#                         self.previous_y=y+1
#                         return x, y+1
#                     else: #if down is blocked continues up:
#                         self.previous_x=x
#                         self.previous_y=y-1
#                         print("GOING UP")
#                         self.direction="n"
#                         if self.board[x][y-1]==BoardCell.CLEAR:
#                             return x, self.initialLocation-1
#                         else:
#                             x = self.rand.randrange(self.rows)
#                             y = self.rand.randrange(self.cols)
#                             self.initialLocation=False
#                             if self.board[x][y] == BoardCell.CLEAR:
#                                 return x, y

                        
                


#                 elif(self.direction=="w"):#goes left until win
#                     self.direction="w"
#                     self.truemove=True
#                     if self.board[x-1][y]== BoardCell.CLEAR:
#                         self.previous_x=x-1
#                         self.previous_y=y
#                         print("GOING LEFT")
#                         return x-1, y
#                     else:#if left is blocked continues right
#                         self.previous_x=x-1
#                         self.previous_y=y
#                         print("GOING RIGHT")
#                         self.direction="e"
#                         if self.board[x-1][y]==BoardCell.CLEAR:
#                             return self.initialLocation_x+1, y
#                         else:
#                             x = self.rand.randrange(self.rows)
#                             y = self.rand.randrange(self.cols)
#                             self.initialLocation=False
#                             if self.board[x][y] == BoardCell.CLEAR:
#                                 return x, y




#                 elif(self.direction=="e"):#goes right until win
#                     self.direction="e"
#                     self.truemove=True
#                     if self.board[x+1][y]== BoardCell.CLEAR:
#                         self.previous_x=x+1
#                         self.previous_y=y
#                         print("GOING RIGHT")
#                         return x+1, y
#                     else:#if right is blocked continues left
#                         self.previous_x=x+1
#                         self.previous_y=y
#                         print("GOING LEFT")
#                         self.direction="w"
#                         if self.board[x+1][y]==BoardCell.CLEAR:
#                             return self.initialLocation_x-1, y
#                         else:
#                             x = self.rand.randrange(self.rows)
#                             y = self.rand.randrange(self.cols)
#                             self.initialLocation=False
#                             if self.board[x][y] == BoardCell.CLEAR:
#                                 return x, y

#                 else:
#                     while True:
#                         x = self.rand.randrange(self.rows)
#                         y = self.rand.randrange(self.cols)
#                         self.initialLocation=False
#                         if self.board[x][y] == BoardCell.CLEAR:
#                             self.initialLocation=False
#                             self.truemove=False
#                             self.direction=""
#                             return x, y 
#         return 0,0

















#START CODE
#    def __init__(self, uid) -> None:
#       # Make your bot personal
#        # Your code start here
#        name = "TeamYourNameBot"
#        color = (0, 255, 0)  # RGB color values, set the values between 0 and 255
#        # Your code ends here
#        super().__init__(uid, name, color)
#        # Your code start here
#        # E.g initialize extra object variables
#        # Your code ends here

#    def init_board(self, cols: int, rows: int, obstacles: [(int, int)], time_given: int) -> None:
#        """
#        This method is invoked at the game initialization.#
#        Parameters:
#        cols: The size of the same board in columns.
#        rows: The size of the game board in rows.
#        obstacles: The list of (x, y) coordinates of blocked board cells.
#        time_given: The total time given to the player bot for the game in ns.
#        """
#        pass

#    def make_a_move(self, time_left: int) -> (int, int):
#        """
#        This method is called when the bot needs to make a move. It will calculate the best move with the given board.#

#        Parameters:
#        time_left: a value indicating time remaining for the bot to complete a game in ns

#        Returns:
#        tuple: containing the bot move with the order (x, y)
#        """
#        # Implement the algorithm which will make the moves
#        # Your code starts here
#        x = -1
#        y = -1
#        # Your code ends here
#        return x, y

#    def notify_move(self, bot_uid: int, move: (int, int)) -> None:
#        """
#        This method is called when a move is made by a player.#

#        Parameters:
#        bot_uid: The Unique ID of the player making the move.
#        move: A tuple representing the move coordinates (x, y).
#        """
#        (x, y) = move
