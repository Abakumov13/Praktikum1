import random

class SuperNim:
    def __init__(self, size=8):
        self.size = size  # Размер шахматной доски
        self.board = [[random.choice([0, 1]) for _ in range(size)] for _ in range(size)]

    def print_board(self):
        for row in self.board:
            print(' '.join(map(str, row)))
        print('')

    def is_game_over(self):
        return all(cell == 0 for row in self.board for cell in row)

    def make_move(self, coord_type, index):
        if coord_type.lower() == 'r':
            self.board[index] = [0] * self.size
        elif coord_type.lower() == 'c':
            for i in range(self.size):
                self.board[i][index] = 0
        else:
            print("Некорректный тип координаты. Используйте 'r' для строки и 'c' для столбца.")
            return False

        return True

def play(game):
    game.print_board()
    current_player = 1

    while not game.is_game_over():
        print(f"Ход игрока {current_player}")
        coord_type = input("Выберите строку (r) или столбец (c): ")
        index = int(input(f"Выберите номер {coord_type}: "))
        
        if game.make_move(coord_type, index):
            game.print_board()
            if game.is_game_over():
                print(f"Игрок {current_player} выигрывает!")
                return
            current_player = 3 - current_player  # Switch player (from 1 to 2 or from 2 to 1)
        else:
            print("Некорректный ход. Попробуйте еще раз.")

play(SuperNim())
