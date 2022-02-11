import numpy as np
import pygame as pg


class Environment():

    def __init__(self, wait_time):
        self.width = 880
        self.height = 880
        self.n_rows = 10
        self.n_columns = 10
        self.init_snake_len = 2
        self.def_reward = -0.03  # kara za życie
        self.neg_reward = -1.  # nagroda za umieranie
        self.pos_reward = 2.  # nagroda za zebranie jablka
        self.wait_time = wait_time

        if self.init_snake_len > self.n_rows / 2:
            self.init_snake_len = int(self.n_rows / 2)

        self.screen = pg.display.set_mode((self.width, self.height))

        self.snake_pos = list()

        # tworzenie tablicy zawierającej matematyczną reprezentację planszy gry
        self.screen_map = np.zeros((self.n_rows, self.n_columns))

        for i in range(self.init_snake_len):
            self.snake_pos.append((int(self.n_rows / 2) + i, int(self.n_columns / 2)))
            self.screen_map[int(self.n_rows / 2) + i][int(self.n_columns / 2)] = 0.5  # wartosc węża

        self.apple_pos = self.place_apple()

        self.draw_screen()

        self.collected = False
        self.last_move = 0

    def place_apple(self):
        posx = np.random.randint(0, self.n_columns)
        posy = np.random.randint(0, self.n_rows)
        while self.screen_map[posy][posx] == 0.5:
            posx = np.random.randint(0, self.n_columns)
            posy = np.random.randint(0, self.n_rows)
        self.screen_map[posy][posx] = 1  # wartosc jabłka
        return (posy, posx)

    def draw_screen(self):
        self.screen.fill((0, 0, 0))
        cell_width = self.width / self.n_columns
        cell_height = self.height / self.n_rows
        for i in range(self.n_rows):
            for j in range(self.n_columns):
                if self.screen_map[i][j] == 0.5:
                    pg.draw.rect(self.screen, (255, 255, 255),
                                 (j * cell_width + 1, i * cell_height + 1, cell_width - 2, cell_height - 2))
                elif self.screen_map[i][j] == 1:
                    pg.draw.rect(self.screen, (255, 0, 0),
                                 (j * cell_width + 1, i * cell_height + 1, cell_width - 2, cell_height - 2))
        pg.display.flip()

    def move_snake(self, next_pos, col):
        self.snake_pos.insert(0, next_pos)
        if not col:
            self.snake_pos.pop(len(self.snake_pos) - 1)
        self.screen_map = np.zeros((self.n_rows, self.n_columns))
        for i in range(len(self.snake_pos)):
            self.screen_map[self.snake_pos[i][0]][self.snake_pos[i][1]] = 0.5
        if col:
            self.apple_pos = self.place_apple()
            self.collected = True
        self.screen_map[self.apple_pos[0]][self.apple_pos[1]] = 1

    def step(self, action):  # metoda aktualizująca środowisko, coś na wzór update z unity
        # action: 0 w góre, 1 w dół, 2 w prawo, 3 w lewo
        game_over = False
        reward = self.def_reward
        self.collected = False

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        snake_x = self.snake_pos[0][1]
        snake_y = self.snake_pos[0][0]
        # sprawdzanie czy akcja jest wykonywalna
        if action == 1 and self.last_move == 0:
            action = 0
        if action == 0 and self.last_move == 1:
            action = 1
        if action == 3 and self.last_move == 2:
            action = 2
        if action == 2 and self.last_move == 3:
            action = 3

        if action == 0:
            if snake_y > 0:
                if self.screen_map[snake_y - 1][snake_x] == 0.5:
                    game_over = True
                    reward = self.neg_reward
                elif self.screen_map[snake_y - 1][snake_x] == 1:
                    reward = self.pos_reward
                    self.move_snake((snake_y - 1, snake_x), True)
                elif self.screen_map[snake_y - 1][snake_x] == 0:
                    self.move_snake((snake_y - 1, snake_x), False)
            else:
                game_over = True
                reward = self.neg_reward

        elif action == 1:
            if snake_y < self.n_rows - 1:
                if self.screen_map[snake_y + 1][snake_x] == 0.5:
                    game_over = True
                    reward = self.neg_reward
                elif self.screen_map[snake_y + 1][snake_x] == 1:
                    reward = self.pos_reward
                    self.move_snake((snake_y + 1, snake_x), True)
                elif self.screen_map[snake_y + 1][snake_x] == 0:
                    self.move_snake((snake_y + 1, snake_x), False)
            else:
                game_over = True
                reward = self.neg_reward

        elif action == 2:
            if snake_x < self.n_columns - 1:
                if self.screen_map[snake_y][snake_x + 1] == 0.5:
                    game_over = True
                    reward = self.neg_reward
                elif self.screen_map[snake_y][snake_x + 1] == 1:
                    reward = self.pos_reward
                    self.move_snake((snake_y, snake_x + 1), True)
                elif self.screen_map[snake_y][snake_x + 1] == 0:
                    self.move_snake((snake_y, snake_x + 1), False)
            else:
                game_over = True
                reward = self.neg_reward

        elif action == 3:
            if snake_x > 0:
                if self.screen_map[snake_y][snake_x - 1] == 0.5:
                    game_over = True
                    reward = self.neg_reward
                elif self.screen_map[snake_y][snake_x - 1] == 1:
                    reward = self.pos_reward
                    self.move_snake((snake_y, snake_x - 1), True)
                elif self.screen_map[snake_y][snake_x - 1] == 0:
                    self.move_snake((snake_y, snake_x - 1), False)
            else:
                game_over = True
                reward = self.neg_reward

        self.draw_screen()
        self.last_move = action
        pg.time.wait(self.wait_time)

        return self.screen_map, reward, game_over

    def reset(self):
        self.screen_map = np.zeros((self.n_rows, self.n_columns))
        self.snake_pos = list()
        for i in range(self.init_snake_len):
            self.snake_pos.append((int(self.n_rows/2) + i, int(self.n_columns / 2)))
            self.screen_map[int(self.n_rows/2) + i][int(self.n_columns / 2)] = 0.5
        self.screen_map[self.apple_pos[0]][self.apple_pos[1]] = 1
        self.last_move = 0
