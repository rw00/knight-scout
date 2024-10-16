def clear_screen():
    print_inline("\033[H\033[J")


def print_inline(s):
    print(s, end="")
