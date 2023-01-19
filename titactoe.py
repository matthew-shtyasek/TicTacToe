
class TicTacToe:
    table = []
    player_x = ''
    player_0 = ''
    winner = ''
    current_move = ''

    def __init__(self, player_x, player_0):  # конструктор
        self.player_x = player_x
        self.player_0 = player_0
        self.reload()

    def move(self):  # ход
        def is_move_valid(x, y):
            return 1 <= x <= 3 and 1 <= y <= 3 and self.table[x-1][y-1] == '*'

        print(f'Ход игрока {self.get_current_player_name()}:')
        is_coords_valid = False
        x, y = 0, 0
        while not is_coords_valid:
            y, x = input('Введите координаты x и y через пробел: ').split()
            x, y = int(x), int(y)
            is_coords_valid = is_move_valid(x, y)
            if not is_coords_valid:
                print('Ошибка, вы ввели неправильные координаты!')
        self.table[x-1][y-1] = self.current_move

    def change_current_move(self):  # изменение знака
        if self.current_move == 'x':
            self.current_move = '0'
        else:
            self.current_move = 'x'

    def get_winner(self):  # поиск победителя
        count_stars = 0
        for line in self.table:
            if line[0] != '*' and len(set(line)) == 1:
                self.winner = self.current_move
                return None
            if '*' in line:
                count_stars += 1

        for i in range(3):
            if '*' != self.table[0][i] == self.table[1][i] == self.table[2][i]:
                self.winner = self.current_move
                return None
        if '*' != self.table[0][0] == self.table[1][1] == self.table[2][2] and '*' != self.table[0][2] == self.table[1][1] == self.table[2][0]:
            self.winner = self.current_move
            return None

        if count_stars == 0:
            self.winner = 'n'
            return None

    def reload(self):  # перезагрузка игры
        print('Началась игра!')
        self.table = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
        if self.winner == '' or self.winner == 'n':
            self.current_move = 'x'
        else:
            self.current_move = self.winner
        self.winner = ''
        self.start()

    def start(self):  # начало игры
        while True:
            self.move()  # делаем ход
            print(self)
            self.get_winner()  # ищем победителя
            if self.winner:  # если победитель есть - завершаем игру
                break
            self.change_current_move()
        if self.winner == 'x' or self.winner == '0':
            print(f"Победил игрок {self.get_current_player_name()}, который играл {self.winner}")  # вывод победителя
        else:
            print('Ничья!')
        self.reload()  # перезагрузка игры

    def get_current_player_name(self):  # получение имени текущего игрока
        return self.player_x if self.current_move == 'x' else self.player_0

    def __str__(self):  # преобразование объекта к строке
        result = ""
        for line in self.table:
            result += ''.join(line) + '\n'  # \n - символ перевода на новую строку
        return result + "---"

ttt = TicTacToe(input('Введите имя первого игрока: '), input('Введите имя второго игрока: '))
