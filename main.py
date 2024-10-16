import common
import view

moves = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))


def main():
    path = scout()
    view.print_path(path)
    view.animate_knight(path)


def scout():
    path = []
    visiting = set()
    re_scout(0, 0, visiting, path)
    return path


def re_scout(row, col, visiting, path):
    pos = (row, col)

    path.append(pos)
    if len(path) == common.total_size:
        return True

    visiting.add(pos)
    for move in moves:
        r = row + move[0]
        c = col + move[1]
        if r < 0 or r >= common.size or c < 0 or c >= common.size:
            continue

        if (r, c) in visiting:
            continue

        if re_scout(r, c, visiting, path):
            return True
    visiting.remove(pos)

    path.pop()
    return False


if __name__ == "__main__":
    main()
