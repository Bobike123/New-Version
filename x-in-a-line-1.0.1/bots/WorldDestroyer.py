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
        name = "WorldDestroyer"
        self.color = (255, 255, 255)  # RGB color values, set the values between 0 and 255
        super().__init__(uid, f"{self.__class__.__name__}_{uid}", self.color)
        self.cols = 0
        self.rows = 0
        self.board = [[int]]
    def init_board(self, cols: int, rows: int, win_length: int, obstacles: [(int, int)], time_given: int) -> None:
        self.cols = cols
        self.rows = rows
        self.win_length=win_length
        self.board = [[BoardCell.CLEAR for _ in range(rows)] for _ in range(cols)]
        for x, y in obstacles:
            self.board[x][y] = BoardCell.BLOCKED
    def check(self,x,y) -> bool:
        #1,0
        #010
        #000
        if y >= 0 and y < self.rows and x>=0 and x < self.cols:
            return True
        return False
    def check_vertical_up(self,x,y)->bool:      #check up the winning steps(ask for how to get the winning moves)
        print("Checking...u.")
        #print(range(1,6))
        if y >= 0 and y < self.rows:      
            for c in range(1,6):    
                cy = y - c
                if self.check(x,cy)==True:
                    if cy < 0 or self.board[x][cy] != BoardCell.CLEAR:
                        return False
                else:
                    return False
            return True
        return False
    def check_vertical_down(self,x,y)->bool:    #check down the winning steps(ask for how to get the winning moves)
        print("Checking...d")
        if y >= 0 and y < self.rows:      
            for c in range(1,6):    
                cy = y + c
                if self.check(x,cy)==True:
                    if cy >= self.cols or self.board[x][cy] != BoardCell.CLEAR:
                        return False
                else:
                    return False
            return True
        return False
    def check_orizontal_left(self,x,y)->bool:   #check left the winning steps(ask for how to get the winning moves)
        print("Checking...l")
        if x >= 0 and x < self.cols:
            for c in range(1,6):    
                cx = x - c
                #print(f"x:{cx},y:{y}")
                if self.check(cx,y)==True:
                    if cx < 0 or self.board[cx][y] != BoardCell.CLEAR:
                        return False
                else:
                    return False
            return True
        return False
    def check_orizontal_right(self,x,y)->bool:  #check right the winning steps(ask for how to get the winning moves)
        print("Checking R")
        if x >= 0 and x < self.cols: 
            for c in range(1,6):    
                cx = x + c
                if self.check(cx,y)==True:
                    if cx >= self.rows or self.board[cx][y] != BoardCell.CLEAR:
                        return False
                else:
                    return False
            return True
        return False
    def check_diagonal_up_r(self,x,y)->bool: #check diagonalupR the winning steps
        c=0
        cx=x
        cy=y
        if y >= 0 and y < self.rows:
            print("Checking UR")
            while c!=range(1,6):
                cy = cy - c
                cx = cx + c
                if self.check(cx,cy)==True:
                    if self.board[cx][cy] !=BoardCell.CLEAR:
                        return False
                else:
                    return False
                c+=1
            return True
        return False
    def check_diagonal_down_r(self,x,y)->bool: #check diagonaldownR the winning steps
        c=0
        cx=x
        cy=y
        if y >= 0 and y < self.rows:
            print("Checking DR")
            while c!=range(1,6):
                cy = cy + c
                cx = cx + c
                if self.check(cx,cy)==True:
                    if self.board[cx][cy] !=BoardCell.CLEAR:
                        return False
                else:
                    return False
                c+=1
            return True
        return False
    def check_diagonal_up_l(self,x,y)->bool: #check diagonaldownL the winning steps
        c=0
        cx=x
        cy=y
        if y >= 0 and y < self.rows:
            print("Checking UL")
            while c!=range(1,6):
                cy = cy - c
                cx = cx - c
                if self.check(cx,cy)==True:
                    if self.board[cx][cy] !=BoardCell.CLEAR:
                        return False
                else:
                    return False
                c+=1
            return True
        return False
    def check_diagonal_down_l(self,x,y)->bool: #check diagonaldownL the winning steps
        c=0
        cx=x
        cy=y
        if y >= 0 and y < self.rows:
            #print("Checking...dl")
            while c!=range(1,6):
                print("Checking DL")
                cy = cy + c
                cx = cx - c
                if self.check(cx,cy)==True:
                    if self.board[cx][cy] !=BoardCell.CLEAR:
                        return False
                else:
                    return False
                c+=1
            return True
        return False
    #TODOs: CHECK WHICH WAY IS THE WINNING POSITION AND DONT WRITE IN THAT POSITION IF YOU CANNOT WIN
    def make_a_move(self, time_left: int) -> (int, int):
        self.move=self.move+1
        print(f"Move number #{self.move}")#number of moves
        #checking for winner:
        print(self.rows)
        print(self.cols)
        countr=0
        countc=0
        for ly in range(self.rows):
            for lx in range(self.cols):
                print(f"lx:{lx},ly:{ly}")
                if self.check(lx,ly)==True:

                    if self.board[lx][ly] == BoardCell.BOT:
                        print(f"Blocked {lx},{ly}")
                        countr =countr + 1
                        print(f"Counter1 {countr}, win length{self.win_length-1}")
                        if countr == self.win_length-1:
                            print(f"YOOOOOOOO {lx},{ly}")
                            if self.board[lx][ly]==BoardCell.CLEAR:
                                if self.check(lx,ly+1):
                                    return lx,ly+1
                    else:
                        countr = 0
                if self.check(ly,lx)==True:
                    if self.board[ly][lx] == BoardCell.BOT:
                        print(f"Blocked {lx},{ly}")
                        countr =countr + 1
                        print(f"Counter2 {countr}, win length{self.win_length-1}")
                        if countr == self.win_length-1:
                            print(f"YOOOOOOOO {lx},{ly}")
                            if self.board[lx][ly]==BoardCell.CLEAR:
                                if self.check(ly,lx+1):
                                    return lx,ly+1
                    else:
                        countr = 0
                    
        print("end")
        #print(f"Initial X:{self.initialLocation_x}")
        #print(f"Initial Y:{self.initialLocation_y}")
        #print(f"Previous X:{self.previous_x}")
        #print(f"Previous Y:{self.previous_y}")
        while(True):#looking for its next move to conquer the world
            if(self.initialLocation==False):   
                self.direction=""
                x = self.rand.randrange(self.cols)
                y = self.rand.randrange(self.rows)
                if(self.check_diagonal_up_r(x,y)==True):#going up-right
                    self.initialLocation_x=x
                    self.initialLocation_y=y
                    self.previous_x=x
                    self.previous_y=y
                    self.initialLocation=True
                    self.direction="NE"
                    if self.board[x][y]==BoardCell.CLEAR:
                        #print(f"This boardcell is clear (x:{x},y:{y})")
                        #print("UUUH I am going north-east")
                        if(self.check(x,y)==True):
                            return x,y
                        else:
                            continue
                
                if(self.check_diagonal_down_r(x,y)==True):#going down-right
                    self.initialLocation_x=x
                    self.initialLocation_y=y
                    self.previous_x=x
                    self.previous_y=y
                    self.initialLocation=True
                    self.direction="SE"
                    if self.board[x][y]==BoardCell.CLEAR:
                        #print(f"This boardcell is clear (x:{x},y:{y})")
                        #print("UUUH I am going south-east")
                        if(self.check(x,y)==True):
                            return x,y
                        else:
                            continue
                
                if(self.check_diagonal_up_l(x,y)==True):#going up-left
                    self.initialLocation_x=x
                    self.initialLocation_y=y
                    self.previous_x=x
                    self.previous_y=y
                    self.initialLocation=True
                    self.direction="NW"
                    if self.board[x][y]==BoardCell.CLEAR:
                        #print(f"This boardcell is clear (x:{x},y:{y})")
                        #print("UUUH I am going north-west")
                        if(self.check(x,y)==True):
                            return x,y
                        else:
                            continue
                
                if(self.check_diagonal_down_l(x,y)==True):#going down-left
                    self.initialLocation_x=x
                    self.initialLocation_y=y
                    self.previous_x=x
                    self.previous_y=y
                    self.initialLocation=True
                    self.direction="SW"
                    if self.board[x][y]==BoardCell.CLEAR:
                        #print(f"This boardcell is clear (x:{x},y:{y})")
                        #print("UUUH I am going south-west")
                        if(self.check(x,y)==True):
                            return x,y
                        else:
                            continue
                
                if(self.check_vertical_up(x,y)==True):#going up
                    self.initialLocation_x=x
                    self.initialLocation_y=y
                    self.previous_x=x
                    self.previous_y=y
                    self.initialLocation=True
                    self.direction="N"
                    if self.board[x][y]==BoardCell.CLEAR:
                        #print(f"This boardcell is clear (x:{x},y:{y})")
                        #print("UUUH I am going north")
                        if(self.check(x,y)==True):
                            return x,y
                        else:
                            continue

                if(self.check_vertical_down(x,y)==True):#going down
                    self.initialLocation_x=x
                    self.initialLocation_y=y
                    self.previous_x=x
                    self.previous_y=y
                    self.initialLocation=True
                    self.direction="S"
                    if self.board[x][y]==BoardCell.CLEAR:
                        #print(f"This boardcell is clear (x:{x},y:{y})")
                        #print("UUUH I am going south")
                        if(self.check(x,y)==True):        
                            return x,y
                        else:
                            continue
           
                if(self.check_orizontal_right(x,y)==True):#going right
                    self.initialLocation_x=x
                    self.initialLocation_y=y
                    self.previous_x=x
                    self.previous_y=y
                    self.initialLocation=True
                    self.direction="E"
                    if self.board[x][y]==BoardCell.CLEAR:
                        #print(f"This boardcell is clear (x:{x},y:{y})")
                        #print("UUUH I am going east")
                        if(self.check(x,y)==True):
                            return x,y
                        else:
                            continue
 
                if(self.check_orizontal_left(x,y)==True):#going left
                    self.initialLocation_x=x
                    self.initialLocation_y=y
                    self.previous_x=x
                    self.previous_y=y
                    self.initialLocation=True
                    self.direction="W"
                    if self.board[x][y]==BoardCell.CLEAR:
                        #print(f"This boardcell is clear (x:{x},y:{y})")
                        #print("UUUH I am going west")
                        if(self.check(x,y)==True):
                            return x,y
                        else:    
                            continue
   
                else:#if there are no winning moves, only draw so fuck it, go random
                    print("I went rambo")
                    for _ in range(self.rows * self.cols):
                        x = self.rand.randrange(self.cols)
                        y = self.rand.randrange(self.rows)
                        if self.board[x][y] == BoardCell.CLEAR:
                            self.initialLocation=False
                            self.initialLocation_x=x
                            self.initialLocation_y=y
                            self.direction=""
                            #print("Everything is fucked, I go rambo")
                            #print(f"This boardcell is clear (x:{x},y:{y})")
                            if(self.check(x,y)==True):
                                return x,y
                            else:
                                continue
            else:
                x=self.previous_x
                y=self.previous_y
                if(self.direction=="NE"):
                    self.previous_x=x+1
                    self.previous_y=y-1
                    if self.board[x+1][y-1]==BoardCell.CLEAR and self.check(x+1,y-1)==True:
                        #print(f"This boardcell is clear (x:{x+1},y:{y-1})")
                        #print("UUUH I am going north east")
                        if(self.check(x+1,y-1)==True):
                            return x+1,y-1
                        else:
                            continue
                    else:
                        ##print("blocked north")
                        self.direction="SW"
                        x=self.initialLocation_x-1
                        y=self.initialLocation_y+1
                        self.previous_x=x
                        self.previous_y=y
                        if self.board[x][y]==BoardCell.CLEAR and self.check(x,y)==True:
                            #print(f"This boardcell is clear (x:{x},y:{y})")
                            #print("UUUH I am going south east")
                            if(self.check(x,y)==True):
                                return x,y
                            else:
                                continue
                        else:
                            for _ in range(self.rows * self.cols):
                                x = self.rand.randrange(self.cols)
                                y = self.rand.randrange(self.rows)
                                if self.board[x][y] == BoardCell.CLEAR:
                                    self.initialLocation=False
                                    self.initialLocation_x=x
                                    self.initialLocation_y=y
                                    self.direction=""
                                    #print(f"This boardcell is clear (x:{x},y:{y})")
                                    if(self.check(x,y)==True):
                                        return x, y
                                    else:
                                        continue
      
                if(self.direction=="SE"):
                    self.previous_x=x+1
                    self.previous_y=y+1
                    if self.board[x+1][y+1]==BoardCell.CLEAR and self.check(x+1,y+1)==True:
                        #print(f"This boardcell is clear (x:{x+1},y:{y+1})")
                        #print("UUUH I am going south east")
                        return x+1,y+1
                    else:
                        ##print("blocked north")
                        self.direction="NW"
                        x=self.initialLocation_x-1
                        y=self.initialLocation_y-1
                        self.previous_x=x
                        self.previous_y=y
                        if self.board[x][y]==BoardCell.CLEAR and self.check(x,y)==True:
                            #print(f"This boardcell is clear (x:{x},y:{y})")
                            #print("UUUH I am going north east")
                            if(self.check(x,y)==True):
                                     x,y
                            else:
                                continue
                        else:
                            for _ in range(self.rows * self.cols):
                                x = self.rand.randrange(self.cols)
                                y = self.rand.randrange(self.rows)
                                if self.board[x][y] == BoardCell.CLEAR:
                                    self.initialLocation=False
                                    self.initialLocation_x=x
                                    self.initialLocation_y=y
                                    self.direction=""
                                    #print(f"This boardcell is clear (x:{x},y:{y})")
                                    if(self.check(x,y)==True):
                                      return x, y
                                    else:
                                        continue
                                
                if(self.direction=="NW"):
                    self.previous_x=x-1
                    self.previous_y=y-1
                    if self.board[x-1][y-1]==BoardCell.CLEAR and self.check(x-1,y-1)==True:
                        #print(f"This boardcell is clear (x:{x-1},y:{y-1})")
                        #print("UUUH I am going north west")
                        return x-1,y-1
                    else:
                        ##print("blocked north")
                        self.direction="SE"
                        x=self.initialLocation_x+1
                        y=self.initialLocation_y+1
                        self.previous_x=x
                        self.previous_y=y
                        if self.board[x][y]==BoardCell.CLEAR and self.check(x,y)==True:
                            #print(f"This boardcell is clear (x:{x},y:{y})")
                            #print("UUUH I am going south west")
                            if(self.check(x,y)==True):
                                return x,y
                            else:
                                continue
                        else:
                            for _ in range(self.rows * self.cols):
                                x = self.rand.randrange(self.cols)
                                y = self.rand.randrange(self.rows)
                                if self.board[x][y] == BoardCell.CLEAR:
                                    self.initialLocation=False
                                    self.initialLocation_x=x
                                    self.initialLocation_y=y
                                    self.direction=""
                                    #print(f"This boardcell is clear (x:{x},y:{y})")
                                    return x, y
                
                if(self.direction=="SW"):
                    self.previous_x=x-1
                    self.previous_y=y+1
                    if self.board[x+1][y-1]==BoardCell.CLEAR and self.check(x-1,y+1)==True:
                        #print(f"This boardcell is clear (x:{x-1},y:{y+1})")
                        #print("UUUH I am going south west")
                        return x-1,y+1
                    else:   
                        ##print("blocked north")
                        self.direction="NE"
                        x=self.initialLocation_x+1
                        y=self.initialLocation_y-1
                        self.previous_x=x
                        self.previous_y=y
                        if self.board[x][y]==BoardCell.CLEAR and self.check(x,y)==True:
                            #print(f"This boardcell is clear (x:{x},y:{y})")
                            #print("UUUH I am going north east")
                            if(self.check(x,y)==True):
                                return x,y
                            else:
                                continue
                        else:
                            for _ in range(self.rows * self.cols):
                                x = self.rand.randrange(self.cols)
                                y = self.rand.randrange(self.rows)
                                if self.board[x][y] == BoardCell.CLEAR:
                                    self.initialLocation=False
                                    self.initialLocation_x=x
                                    self.initialLocation_y=y
                                    self.direction=""
                                    #print(f"This boardcell is clear (x:{x},y:{y})")
                                    if(self.check(x,y)==True):
                                        return x, y
                                    else:
                                        continue
                
                if(self.direction=="N"):
                    self.previous_x=x
                    self.previous_y=y-1
                    if self.board[x][y-1]==BoardCell.CLEAR:
                        #print(f"This boardcell is clear (x:{x},y:{y-1})")
                        #print("UUUH I am going north")
                        if(self.check(x,y-1)==True):
                            return x,y-1
                        else:
                            continue
                    else:
                        ##print("blocked north")
                        self.direction="S"
                        x=self.initialLocation_x
                        y=self.initialLocation_y+1
                        self.previous_x=x
                        self.previous_y=y
                        if self.board[x][y]==BoardCell.CLEAR and self.check(x,y)==True:
                            #print(f"This boardcell is clear (x:{x},y:{y})")
                            #print("UUUH I am going south")
                            if(self.check(x,y)==True):
                                return x,y
                            else:
                                continue
                        else:
                            for _ in range(self.rows * self.cols):
                                x = self.rand.randrange(self.cols)
                                y = self.rand.randrange(self.rows)
                                if self.board[x][y] == BoardCell.CLEAR:
                                    self.initialLocation=False
                                    self.initialLocation_x=x
                                    self.initialLocation_y=y
                                    self.direction=""
                                    #print(f"This boardcell is clear (x:{x},y:{y})")
                                    if(self.check(x,y)==True):
                                        return x, y
                                    else:
                                        continue
                
                if(self.direction=="S"):
                    self.previous_x=x
                    self.previous_y=y+1
                    if self.board[x][y+1]==BoardCell.CLEAR and self.check(x,y)==True:
                        #print(f"This boardcell is clear (x:{x},y:{y+1})")
                        #print("UUUH I am going south")
                        if(self.check(x,y+1)==True):
                            return x,y+1
                        else:
                            continue
                    else:
                        ##print("blocked south")
                        self.direction="N"
                        x=self.initialLocation_x
                        y=self.initialLocation_y-1
                        self.previous_x=x
                        self.previous_y=y
                        if self.board[x][y]==BoardCell.CLEAR and self.check(x,y)==True:
                            #print(f"This boardcell is clear (x:{x},y:{y})")
                            #print("UUUH I am going north")
                            if(self.check(x,y)==True):
                                return x,y
                            else:
                                continue
                        else:
                            for _ in range(self.rows * self.cols):
                                x = self.rand.randrange(self.cols)
                                y = self.rand.randrange(self.rows)
                                if self.board[x][y] == BoardCell.CLEAR and self.check(x,y)==True:
                                    self.initialLocation=False
                                    self.initialLocation_x=x
                                    self.initialLocation_y=y
                                    self.direction=""
                                    #print(f"This boardcell is clear (x:{x},y:{y})")
                                    if(self.check(x,y)==True):
                                        return x, y
                                    else:
                                        continue
             
                if(self.direction=="E"):
                    self.previous_x=x+1
                    self.previous_y=y
                    if self.board[x+1][y]==BoardCell.CLEAR  and self.check(x+1,y)==True:
                        #print(f"This boardcell is clear (x:{x+1},y:{y})")
                        #print("UUUH I am going east")
                        return x+1,y
                    else:
                        ##print("blocked east")
                        self.direction="W"
                        x=self.initialLocation_x-1
                        y=self.initialLocation_y
                        self.previous_x=x
                        self.previous_y=y
                        if self.board[x][y]==BoardCell.CLEAR and self.check(x,y)==True:
                            #print(f"This boardcell is clear (x:{x},y:{y})")
                            #print("UUUH I am going west")
                            if(self.check(x,y)==True):
                                return x,y
                            else:
                                continue
                        else:
                            for _ in range(self.rows * self.cols):
                                x = self.rand.randrange(self.cols)
                                y = self.rand.randrange(self.rows)
                                if self.board[x][y] == BoardCell.CLEAR and self.check(x,y)==True:
                                    self.initialLocation=False
                                    self.initialLocation_x=x
                                    self.initialLocation_y=y
                                    self.direction=""
                                    #print(f"This boardcell is clear (x:{x},y:{y})")
                                    if(self.check(x,y)==True):
                                        return x, y
                                    else:
                                        continue
              
                if(self.direction=="W"):
                    self.previous_x=x-1
                    self.previous_y=y
                    if self.board[x-1][y]==BoardCell.CLEAR and self.check(x-1,y)==True:
                        #print(f"This boardcell is clear (x:{x-1},y:{y})")
                        #print("UUUH I am going west")
                        return x-1,y
                    else:
                        ##print("blocked west")
                        self.direction="W"
                        x=self.initialLocation_x+1
                        y=self.initialLocation_y
                        self.previous_x=x
                        self.previous_y=y
                        if self.board[x][y]==BoardCell.CLEAR and self.check(x,y)==True:
                            #print(f"This boardcell is clear (x:{x},y:{y})")
                            #print("UUUH I am going west")
                            if(self.check(x,y)==True):
                                return x,y
                            else:
                                continue
                        else:
                            for _ in range(self.rows * self.cols):
                                x = self.rand.randrange(self.cols)
                                y = self.rand.randrange(self.rows)
                                if self.board[x][y] == BoardCell.CLEAR and self.check(x,y)==True:
                                    self.initialLocation=False
                                    self.initialLocation_x=x
                                    self.initialLocation_y=y
                                    self.direction=""
                                    #print(f"This boardcell is clear (x:{x},y:{y})")
                                    if(self.check(x,y)==True):
                                        return x, y
                                    else:
                                        continue                    
    def notify_move(self, bot_uid: int, move: (int, int)) -> None:
        (x, y) = move
        self.board[x][y] = bot_uid