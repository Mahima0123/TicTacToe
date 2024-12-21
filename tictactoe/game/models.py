from django.db import models

class Game(models.Model):
    board = models.CharField(max_length=9, default=' ' * 9)  # 9 characters for the board
    current_turn = models.CharField(max_length=1, default='X')  # X or O
    winner = models.CharField(max_length=1, blank=True, null=True)  # X, O, or None for draw

    def is_winner(self):
        win_positions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)              # Diagonals
        ]
        for pos in win_positions:
            if self.board[pos[0]] == self.board[pos[1]] == self.board[pos[2]] != ' ':
                return self.board[pos[0]]
        return None

    def is_draw(self):
        return ' ' not in self.board and not self.is_winner()

    def make_move(self, position):
        print(f"Move made at position: {position}")
        print(f"Current board before move: {self.board}")
        if self.board[position] == ' ' and not self.winner:
            board_list = list(self.board)
            board_list[position] = self.current_turn
            self.board = ''.join(board_list)
            self.winner = self.is_winner()
            if not self.winner and not self.is_draw():
                self.current_turn = 'O' if self.current_turn == 'X' else 'X'
            self.save()

