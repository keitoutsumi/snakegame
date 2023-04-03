import numpy as np
import tkinter as tk
import time as time
import random as rand

UP = (-1,0)
DOWN = (1,0)
LEFT = (0,-1)
RIGHT = (0,1)

MOVES = [UP,DOWN,LEFT,RIGHT]

EMPTY = 0
FOOD = 99

class Game:
    def __init__(self,board_size,player,max_turns = 400,display = False,gui = None):
        self.board_size = board_size
        self.player = player
        self.max_turns = max_turns

        self.init_snakesize = 3
        self.food_num = 4
        self.turns = 0

        self.snake = [(board_size//2,board_size//2+i)for i in range(self.init_snakesize)]
        self.snake_death = False
        self.foodxys = [(self.board_size//4,self.board_size//4),(3*self.board_size//4,self.board_size//4),(self.board_size//4,3*self.board_size//4),(3*self.board_size//4,3*self.board_size//4)]


        self.board = np.zeros([self.board_size,self.board_size])
        self.display = display
        self.gui = gui

        self.food_index = 0
        #change to random afterwards!!
        self.food_list = [(2, 9), (8, 3), (8, 2), (7, 0), (8, 3), (8, 8), (5, 1), (1, 9), (9, 4), (9, 9), (6, 6), (6, 7), (0, 0), (8, 7), (6, 9), (3, 5), (8, 5), (5, 3), (7, 3), (8, 5), (6, 0), (1, 4), (9, 2), (9, 8), (6, 7), (0, 4), (1, 2), (5, 8), (2, 0), (0, 8), (8, 4), (8, 2), (4, 4), (4, 4), (6, 4), (1, 9), (5, 6), (4, 5), (7, 9), (1, 7), (5, 4), (4, 4), (2, 4), (0, 1), (2, 3), (3, 8), (9, 7), (4, 7), (0, 6), (3, 7), (2, 6), (1, 2), (0, 0), (3, 6), (6, 2), (4, 5), (6, 9), (3, 7), (5, 7), (5, 9), (4, 3), (7, 2), (2, 6), (7, 1), (6, 8), (7, 0), (5, 1), (4, 3), (6, 0), (7, 6), (0, 0), (8, 0), (1, 9), (1, 6), (0, 1), (8, 9), (6, 9), (4, 9), (3, 7), (1, 3), (2, 6), (8, 2), (3, 2), (9, 3), (8, 7), (5, 9), (5, 4), (1, 3), (3, 0), (7, 7), (0, 2), (0, 4), (2, 9), (0, 3), (3, 9), (2, 2), (1, 5), (6, 8), (5, 9), (5, 5), (8, 3), (0, 1), (4, 7), (0, 0), (1, 2), (5, 2), (8, 2), (6, 0), (3, 4), (8, 9), (7, 3), (6, 8), (9, 3), (8, 6), (3, 4), (2, 3), (0, 8), (8, 9), (9, 6), (6, 6), (3, 1), (1, 9), (3, 8), (9, 3), (2, 7), (1, 0), (2, 1), (5, 3), (0, 0), (4, 0), (5, 8), (4, 8), (4, 0), (1, 2), (2, 2), (8, 1), (5, 5), (9, 8), (0, 6), (0, 6), (0, 8), (6, 1), (7, 9), (5, 7), (8, 6), (3, 1), (4, 8), (8, 0), (9, 1), (3, 5), (1, 5), (6, 8), (7, 7), (7, 3), (2, 4), (4, 8), (2, 1), (9, 2), (6, 1), (6, 5), (9, 7), (0, 5), (8, 0), (8, 8), (6, 3), (7, 1), (4, 8), (4, 9), (2, 7), (1, 5), (5, 3), (8, 3), (1, 0), (9, 1), (1, 2), (4, 8), (6, 7), (1, 2), (9, 6), (7, 9), (3, 8), (6, 4), (8, 1), (1, 5), (1, 7), (0, 5), (6, 1), (1, 8), (3, 0), (4, 7), (1, 9), (1, 4), (5, 0), (8, 8), (0, 9), (5, 2), (2, 3), (5, 1), (2, 5), (9, 9)]


        for bodyxy in self.snake:
            self.board[bodyxy[0]][bodyxy[1]] = 1
        for foodxy in self.foodxys:
            self.board[foodxy[0]][foodxy[1]] = FOOD

        # self.food_index = 0
        # #change to random afterwards!!
        # self.food_list = [(2, 9), (8, 3), (8, 2), (7, 0), (8, 3), (8, 8), (5, 1), (1, 9), (9, 4), (9, 9), (6, 6), (6, 7), (0, 0), (8, 7), (6, 9), (3, 5), (8, 5), (5, 3), (7, 3), (8, 5), (6, 0), (1, 4), (9, 2), (9, 8), (6, 7), (0, 4), (1, 2), (5, 8), (2, 0), (0, 8), (8, 4), (8, 2), (4, 4), (4, 4), (6, 4), (1, 9), (5, 6), (4, 5), (7, 9), (1, 7), (5, 4), (4, 4), (2, 4), (0, 1), (2, 3), (3, 8), (9, 7), (4, 7), (0, 6), (3, 7), (2, 6), (1, 2), (0, 0), (3, 6), (6, 2), (4, 5), (6, 9), (3, 7), (5, 7), (5, 9), (4, 3), (7, 2), (2, 6), (7, 1), (6, 8), (7, 0), (5, 1), (4, 3), (6, 0), (7, 6), (0, 0), (8, 0), (1, 9), (1, 6), (0, 1), (8, 9), (6, 9), (4, 9), (3, 7), (1, 3), (2, 6), (8, 2), (3, 2), (9, 3), (8, 7), (5, 9), (5, 4), (1, 3), (3, 0), (7, 7), (0, 2), (0, 4), (2, 9), (0, 3), (3, 9), (2, 2), (1, 5), (6, 8), (5, 9), (5, 5), (8, 3), (0, 1), (4, 7), (0, 0), (1, 2), (5, 2), (8, 2), (6, 0), (3, 4), (8, 9), (7, 3), (6, 8), (9, 3), (8, 6), (3, 4), (2, 3), (0, 8), (8, 9), (9, 6), (6, 6), (3, 1), (1, 9), (3, 8), (9, 3), (2, 7), (1, 0), (2, 1), (5, 3), (0, 0), (4, 0), (5, 8), (4, 8), (4, 0), (1, 2), (2, 2), (8, 1), (5, 5), (9, 8), (0, 6), (0, 6), (0, 8), (6, 1), (7, 9), (5, 7), (8, 6), (3, 1), (4, 8), (8, 0), (9, 1), (3, 5), (1, 5), (6, 8), (7, 7), (7, 3), (2, 4), (4, 8), (2, 1), (9, 2), (6, 1), (6, 5), (9, 7), (0, 5), (8, 0), (8, 8), (6, 3), (7, 1), (4, 8), (4, 9), (2, 7), (1, 5), (5, 3), (8, 3), (1, 0), (9, 1), (1, 2), (4, 8), (6, 7), (1, 2), (9, 6), (7, 9), (3, 8), (6, 4), (8, 1), (1, 5), (1, 7), (0, 5), (6, 1), (1, 8), (3, 0), (4, 7), (1, 9), (1, 4), (5, 0), (8, 8), (0, 9), (5, 2), (2, 3), (5, 1), (2, 5), (9, 9)]

    def move(self):
        snake = self.snake
        move = self.player.get_move(self.board,snake)
        new_headxy = (snake[-1][0] + move[0], snake[-1][1] + move[1])
        snake.append(new_headxy)

        headxy = snake[-1]
        if headxy not in self.foodxys:
            self.board[snake[0][0]][snake[0][1]] = EMPTY
            snake.pop(0)
        else:
            self.foodxys.remove(headxy)
        
        if headxy[0] >= self.board_size or headxy[1] >= self.board_size or headxy[0] < 0 or headxy[1] < 0:
            self.snake_death = True
        else:
            self.board[headxy[0]][headxy[1]] = 1

        if headxy in snake[:-1]:
            self.snake_death = True

        # while len(self.foodxys) < self.food_num:
        #     nextfoodxy = (rand.randint(0,self.board_size-1),rand.randint(0,self.board_size-1))
        #     while self.board[nextfoodxy[0]][new_headxy[1]] != EMPTY:
        #         print("bug?")
        #         nextfoodxy = (rand.randint(0,self.board_size-1),rand.randint(0,self.board_size-1))
        #     self.foodxys.append(nextfoodxy)
        #     self.board[nextfoodxy[0]][new_headxy[1]] = FOOD
        # return move

        while len(self.foodxys) < self.food_num:
            x = self.food_list[self.food_index][0]
            y = self.food_list[self.food_index][1]
            while self.board[x][y] != EMPTY:# if unable to generate foodxys, try next coordinate
                self.food_index += 1
                x = self.food_list[self.food_index][0]
                y = self.food_list[self.food_index][1]
            self.foodxys.append((x,y))
            self.board[x][y] = FOOD
            self.food_index += 1
        return move

    def play(self):
        if self.display:
            self.display_board()
        while True:
            if len(self.snake) - self.turns/20 <= 0:
                self.snake_death = True
                return -2
            if self.snake_death:
                return -1
            if self.turns >= self.max_turns:
                return 0
            self.turns += 1
            move = self.move()
            if self.display:
                if move == UP:
                    print("UP")
                elif move == RIGHT:
                    print("RIGHT")
                elif move == LEFT:
                    print("LEFT")
                else:
                    print("DOWN")
                self.display_board()
                if self.gui is not None:
                    self.gui.update()
                time.sleep(0.2)

    def display_board(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board[i][j] == EMPTY:
                    print(".",end="")
                elif self.board[i][j] == FOOD:
                    print("#",end="")
                else:
                    print("1",end="")
            print("")

class Gui:
    def __init__(self,game,gui_size):
        self.game = game
        self.game.gui = self
        self.size = gui_size

        self.ratio = self.size / self.game.board_size

        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root,width = self.size, height = self.size,bg = "black")
        self.canvas.pack()

        snake = self.game.snake
        self.canvas.create_rectangle(self.ratio*(snake[-1][1]+0.05),self.ratio*(snake[-1][0]+0.05),self.ratio*(snake[-1][1]+0.95),self.ratio*(snake[-1][0]+0.95),fill="blue2")
        for i in range(len(snake)-1):
            self.canvas.create_rectangle(self.ratio*(snake[i][1]+0.05),self.ratio*(snake[i][0]+0.05),self.ratio*(snake[i][1]+0.95),self.ratio*(snake[i][0]+0.95),fill="green2")
        
        for foodxy in self.game.foodxys:
            self.canvas.create_rectangle(self.ratio*(foodxy[1]),self.ratio*(foodxy[0]),self.ratio*(foodxy[1]+1),self.ratio*(foodxy[0]+1),fill="red")

    def update(self):
        self.canvas.delete("all")
        snake = self.game.snake
        self.canvas.create_rectangle(self.ratio*(snake[-1][1]+0.05),self.ratio*(snake[-1][0]+0.05),self.ratio*(snake[-1][1]+0.95),self.ratio*(snake[-1][0]+0.95),fill="blue2")
        for i in range(len(snake)-1):
            self.canvas.create_rectangle(self.ratio*(snake[i][1]+0.05),self.ratio*(snake[i][0]+0.05),self.ratio*(snake[i][1]+0.95),self.ratio*(snake[i][0]+0.95),fill="green2")
        
        for foodxy in self.game.foodxys:
            self.canvas.create_rectangle(self.ratio*(foodxy[1]),self.ratio*(foodxy[0]),self.ratio*(foodxy[1]+1),self.ratio*(foodxy[0]+1),fill="red")
        
        self.canvas.pack()
        self.root.update()
