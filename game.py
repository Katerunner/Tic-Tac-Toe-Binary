from board import *


class Game:
    """Represents tic-tac-toe game"""
    def __init__(self):
        """Initialization"""
        self.mainboard = Board()
        # You can choose whether user starts first
        self.user_starts = True

    def play(self):
        """Main play function"""
        state = self.mainboard.has_winner()
        if not self.user_starts:
            print("Computer starts")
            self.mainboard.move_random()
            print(self.mainboard)
        else:
            print("User starts")
        while not state:
            print(state)
            suc = 1
            while suc:
                try:
                    coord = input("Enter coordinates: ").split()
                    self.mainboard.move((int(coord[0]), int(coord[1])))
                    suc = 0
                except CellIsNotEmptyError:
                    print("Cell is already taken. Try again.")
                except (ValueError, IndexError):
                    print("Invalid format (must be'1 2' for exp.). Try again.")

            print(self.mainboard)
            state = self.mainboard.has_winner()
            if state:
                break
            board_1 = copy.deepcopy(self.mainboard)
            board_2 = copy.deepcopy(self.mainboard)
            try:
                board_1.move_random()
                board_2.move_random()
            except IndexError:
                print(1)
            if board_1.compute_score() >= board_2.compute_score():
                self.mainboard = board_1
            else:
                self.mainboard = board_2
            print("Computer's choice")
            print(self.mainboard)
            state = self.mainboard.has_winner()

        if state == 2:
            print("DRAW\nGame Over")
        elif state == 1:
            print("NOUGHT WINNER!\nGame Over")
        else:
            print("CROSS WINNER!\nGame Over")


if __name__ == "__main__":
    game = Game()
    game.play()
