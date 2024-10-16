import common
import util
import time

black = "  "
white = "\u2588" + "\u2588"
knight = "k "  # u'\u265e'


def animate_knight(path):
    for pos in path:
        util.clear_screen()
        print_knight(pos)
        time.sleep(0.5)  # simple animation


def print_knight(knight_position):
    for row in range(common.size):
        for col in range(common.size):
            if knight_position == (row, col):
                util.print_inline(knight)
            else:
                util.print_inline(cell_color(row, col))
        print()  # new line


def print_path(path):
    readable_positions = map(lambda pos: cell(pos[0], pos[1]), path)
    print(list(readable_positions))


def cell_color(r, c):
    if (r + c) % 2 == 0:
        return white
    else:
        return black


def cell(r, c):
    # this is how the chess board looks like
    # a8 b c d e f g h8
    # 7              h7
    # 6              h6
    # 5              h5
    # 4              h4
    # 3              h3
    # 2              h2
    # 1a b c d e f g h1
    # (0, 0) == a8
    return chr(c + ord("a")) + str(common.size - r)
