import unittest
from game import Game


class TestGame(unittest.TestCase):

    def test_change_player_turn_when_is_x_turn(self):
        game = Game()
        game.player_turn = "X"
        game.change_player_turn()
        self.assertEqual("O", game.player_turn)

    def test_change_player_turn_when_is_o_turn(self):
        game = Game()
        game.player_turn = "O"
        game.change_player_turn()
        self.assertEqual("X", game.player_turn)

    def test_reset_fields(self):
        game = Game()
        game.fields = [["X", "X", "X"], ["O", "O", "O"], ["X", "O", "X"]]
        game.reset_fields()
        self.assertEqual([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]], game.fields)

    def test_show_fields_on_start(self):
        game = Game()
        fields = game.get_displayed_fields()
        expected_display = "0 | 1 | 2\n----------\n3 | 4 | 5\n----------\n6 | 7 | 8"
        self.assertEqual(fields, expected_display)

    def test_show_fields_with_values(self):
        game = Game()
        game.fields = [["X", " ", "X"], [" ", "X", "O"], ["X", "X", "O"]]
        display = game.get_displayed_fields()
        expected_display = "X | 1 | X\n----------\n3 | X | O\n----------\nX | X | O"
        self.assertEqual(expected_display, display)

    def test_validate_correct_field_choose(self):
        game = Game()
        game.fields = [["X", " ", "X"], [" ", "X", "O"], ["X", "X", "O"]]
        validation = game.validate_field("3")
        self.assertEqual(True, validation)

    def test_validate_incorrect_field_not_in_range_choose(self):
        game = Game()
        game.fields = [["X", " ", "X"], [" ", "X", "O"], ["X", "X", "O"]]
        validation = game.validate_field("10")
        self.assertEqual(False, validation)

    def test_validate_incorrect_field_in_range_choose(self):
        game = Game()
        game.fields = [["X", " ", "X"], [" ", "X", "O"], ["X", "X", "O"]]
        validation = game.validate_field("2")
        self.assertEqual(False, validation)

    def test_validate_incorrect_not_number_choose(self):
        game = Game()
        game.fields = [["X", " ", "X"], [" ", "X", "O"], ["X", "X", "O"]]
        validation = game.validate_field("AAA")
        self.assertEqual(False, validation)

    def test_validate_player1_move(self):
        game = Game()
        game.move(4)
        expected_fields = [[" ", " ", " "], [" ", "X", " "], [" ", " ", " "]]
        self.assertEqual(expected_fields, game.fields)

    def test_validate_player2_move(self):
        game = Game()
        game.change_player_turn()
        game.move(7)
        expected_fields = [[" ", " ", " "], [" ", " ", " "], [" ", "O", " "]]
        self.assertEqual(expected_fields, game.fields)

    def test_rows_result_1(self):
        game = Game()
        game.fields = [["X", "X", "X"], [" ", " ", " "], [" ", " ", " "]]
        self.assertEqual(True, game.test_rows_result())


