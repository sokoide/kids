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
    print("%d,%d='%s'" % (x, y, data[y][x]))
    if data[y][x] == 'G':
        print_result()
        return True
    if data[y][x] != ' ' and data[y][x] != 'S':
        return False

    data[y] = data[y][:x] + '*' + data[y][x + 1:]
    r = dfs(x + 1, y)
    if not r:
        r = dfs(x - 1, y)
    if not r:
        r = dfs(x, y + 1)
    if not r:
        r = dfs(x, y - 1)

    data[y] = data[y][:x] + ' ' + data[y][x + 1:]
    return r


dfs(1, 1)
