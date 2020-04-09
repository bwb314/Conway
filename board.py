import os
import random
import time 

class board:

    def __init__(self, rows, cols=None):
        
        self.rows = rows
        if cols is None:
            self.cols = rows
        else:
            self.cols = cols

        self.board = [[0]*self.cols for _ in range(self.rows)]
        self.randomly_populate()
    
    def randomly_populate(self):
        
        seed = random.getrandbits(self.rows*self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                self.board[i][j] = seed&1
                seed >>= 1
 
    def tick(self):

        #Any live cell with two or three neighbors survives.
        #Any dead cell with three live neighbors becomes a live cell.
        #All other live cells die in the next generation. Similarly, all other dead cells stay dead. 
        # -1 -> alive to dead
        # -2 -> dead to alive 
        for i in range(self.rows):
            for j in range(self.cols):
                alive = 0
                for di, dj in [(1,0), (0,1), (1,1), (-1,0), (0,-1), (-1,-1), (1,-1), (-1,1)]:
                    ni = i+di
                    nj = j+dj
                    if not 0 <= ni < self.rows:
                        continue
                    if not 0 <= nj < self.cols:
                        continue
                    if abs(self.board[ni][nj]) == 1:
                        alive += 1
                if self.board[i][j] == 1: 
                    if not 2 <= alive <= 3:
                        self.board[i][j] = -1
                elif alive == 3:
                    self.board[i][j] = -2
        
        mapping = {1:1, 0:0, -1:0, -2:1}
        for i in range(self.rows):
            for j in range(self.cols):
                self.board[i][j] = mapping[self.board[i][j]]
    
    def play(self, ticks):
       
        self.print_board() 
        for _ in range(ticks):
            time.sleep(0.2)
            self.tick() 
            self.print_board() 

    def print_board(self):
        os.system('clear')
        for row in self.board:
            print(''.join(map(str, row))) 
