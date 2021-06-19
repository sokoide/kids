def fib(a):
    if a <= 1:
        return a
    else:
        return fib(a - 1) + fib(a - 2)


for i in range(1, 10):
    print('fib(%d)=%d' % (i, fib(i)))

data = ['##########',
        '#S   #   #',
        '#  # # # #',
        '#  #   # #',
        '#  ##### #',
        '#    #   #',
        '#  ### # #',
        '#  # # ###',
        '#    #  G#',
        '##########',
        ]


def print_result():
    print("Goal!")
    for line in data:
        print(line)


def dfs(x, y):
    if x < 0 or x >= len(data[0]) or y < 0 or y >= len(data):
        return False
    print("checking (%d,%d)='%s'" % (x, y, data[y][x]))
    if data[y][x] == 'G':
        return True
    if data[y][x] != ' ' and data[y][x] != 'S':
        return False

    data[y] = data[y][:x] + '*' + data[y][x + 1:]

    # 1. ifでDFS
    r = dfs(x + 1, y)
    if not r:
        r = dfs(x - 1, y)
    if not r:
        r = dfs(x, y + 1)
    if not r:
        r = dfs(x, y - 1)
    data[y] = data[y][:x] + ' ' + data[y][x + 1:]
    return r

    # 2. [(1,0),...]を使って四方の探索を簡略化. やっている内容は1同じです
    # for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
    #     if dfs(x+d[0], y+d[1]):
    #         return True
    # data[y] = data[y][:x] + ' ' + data[y][x + 1:]
    # return False


if dfs(1, 1):
    print_result()
else:
    print('パスが見つかりませんでした')
