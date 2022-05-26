class Game:
    def __init__(self):
        """Game constructor"""
        self.fields = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.player_turn = "X"
        self.count_x_wins = 0
        self.count_o_wins = 0
        self.count_draws = 0
        self.actual_play_count = 0

    def play(self, change_turn: bool, game_finish: bool) -> None:
        if change_turn:
            self.change_player_turn()
            self.actual_play_count += 1
        if game_finish:
            self.reset_fields()
            print("X wins counter: {} --- O wins counter: {} --- Draws counter: {}".format(self.count_x_wins,
                                                                                           self.count_o_wins,
                                                                                           self.count_draws))
        self.show_player_turn()
        print(self.get_displayed_fields())
        played_square = input("\nChoose a field to play")
        if not self.validate_field(played_square):
            print("Invalid field, choose again")
            self.play(False, False)
            return
        self.move(int(played_square))
        if self.get_game_state() == "D":
            self.count_draws += 1
            print("Draw!")
            self.play(True, True)
            return
        if self.get_game_state() == "W":
            print("Player {} wins!".format(self.player_turn.upper()))
            if self.player_turn == "X":
                self.count_x_wins += 1
            else:
                self.count_o_wins += 1
            self.play(True, True)
            return
        self.play(True, False)
        return

    def change_player_turn(self) -> None:
        self.player_turn = "X" if self.player_turn == "O" else "O"

    def show_player_turn(self) -> None:
        print(f'Turn of {0}!'.format(self.player_turn))

    def reset_fields(self) -> None:
        self.fields = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.actual_play_count = 0

    def get_displayed_fields(self) -> str:
        displayed_fields = ""
        for i in range(3):
            for j in range(3):
                actual_field_value = self.fields[i][j]
                actual_field_number = i + j
                if i >= 1:
                    actual_field_number += 2
                if i >= 2:
                    actual_field_number += 2
                if j == 1:
                    displayed_fields += " | {0} | ".format(actual_field_value) if actual_field_value != " " else \
                        " | {0} | ".format(actual_field_number)
                    continue
                displayed_fields += self.fields[i][j] if actual_field_value != " " else str(actual_field_number)
            if i < 2:
                displayed_fields += "\n----------\n"
        return displayed_fields

    def validate_field(self, field) -> bool:
        try:
            int_field = int(field)
            if not int_field < 0 or not int_field > 8:
                if str(int_field) in self.get_displayed_fields():
                    return True
            return False
        except ValueError:
            return False

    def move(self, played_field: int) -> None:
        i = 0
        j = 0
        if played_field <= 2:
            i = 0
            j = played_field
        elif played_field <= 5:
            i = 1
            j = played_field - 3
        elif played_field <= 8:
            i = 2
            j = played_field - 6
        self.fields[i][j] = self.player_turn

    def get_game_state(self) -> str:
        """ Test game result,
        returns:
            W (have a winner)
            D (draw)
            C (game continue)
        """
        if self.test_rows_result() or self.test_columns_result() or self.test_diagonals_result():
            return "W"
        if self.test_has_field_empty():
            return "D"
        return "C"

    def test_rows_result(self) -> bool:
        for i in range(3):
            if self.fields[i][0] != " " \
                    and self.fields[i][0] == self.fields[i][1] and self.fields[i][0] == self.fields[i][2]:
                return True
        return False

    def test_columns_result(self) -> bool:
        for i in range(3):
            if self.fields[0][i] != " " \
                    and self.fields[0][i] == self.fields[1][i] and self.fields[0][i] == self.fields[2][i]:
                return True
        return False

    def test_diagonals_result(self) -> bool:
        for i in range(3):
            if self.fields[0][0] != " " \
                    and self.fields[0][0] == self.fields[1][1] and self.fields[0][0] == self.fields[2][2]:
                return True
            elif self.fields[0][0] != " " \
                    and self.fields[0][2] == self.fields[1][1] and self.fields[0][2] == self.fields[2][0]:
                return True
        return False

    def test_has_field_empty(self) -> bool:
        if self.actual_play_count < 9:
            return False
        return True


