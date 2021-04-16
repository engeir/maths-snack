width = 75
height = 52
nsteps = 12000


class Dir:
    up, right, down, left = range(4)


class Turn:
    left, right = False, True


class Color:
    white, black = ".", "#"


M = [[Color.white] * width for _ in range(height)]

x = width // 2
y = height // 2
direc = Dir.up

i = 0
while i < nsteps and 0 <= x < width and 0 <= y < height:
    turn = Turn.left if M[y][x] == Color.black else Turn.right
    M[y][x] = Color.white if M[y][x] == Color.black else Color.black

    direc = (4 + direc + (1 if turn else -1)) % 4
    direc = [Dir.up, Dir.right, Dir.down, Dir.left][direc]
    if direc == Dir.up:
        y -= 1
    elif direc == Dir.right:
        x -= 1
    elif direc == Dir.down:
        y += 1
    elif direc == Dir.left:
        x += 1
    else:
        assert False
    i += 1

print("\n".join("".join(row) for row in M))
