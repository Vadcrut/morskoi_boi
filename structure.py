from random import randint

a1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
a2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
a3 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
d = {4: 1, 3: 2, 2: 3, 1: 4}


def check(x, y, kolp, napr, a):
    if napr == 2:
        if x + kolp <= 10:
            f = True
            for i in range(kolp):
                if a[y][x + i] != 0:
                    f = False
            if f:
                for i in range(kolp):
                    a[y][x + i] = 4
                fillmas(x, y, napr, kolp, a)
                return True
    elif napr == 1:
        if y + kolp <= 10:
            f = True
            for i in range(kolp):
                if a[y + i][x] != 0:
                    f = False
            if f:
                for i in range(kolp):
                    a[y + i][x] = 4
                fillmas(x, y, napr, kolp, a)
                return True
    return False


def fillmas(x, y, napr, kolp, a):
    if napr == 2:
        for i in range(kolp):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    if (y + j >= 0 and y + j < 10) and (x + i + k >= 0 and x + i + k < 10) and a[y + j][x + i + k] == 0:
                        a[y + j][x + i + k] = 3
    elif napr == 1:
        for i in range(kolp):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    if (y + j + i >= 0 and y + j + i < 10) and (x + k >= 0 and x + k < 10) and a[y + j + i][x + k] == 0:
                        a[y + j + i][x + k] = 3


def makerasstanovka():
    for key in d.keys():
        for i in range(d[key]):
            f = False
            while not f:
                x = randint(0, 9)
                y = randint(0, 9)
                napr = randint(1, 2)
                f = check(x, y, key, napr, a2)


def dead(x, y, a):
    f1 = True
    f2 = True
    f3 = True
    f4 = True
    d = {'yu': 0, 'xl': 0, 'yd': 0, 'xr': 0}
    d1 = {'yu': 0, 'xl': 0, 'yd': 0, 'xr': 0}
    for i in range(1, 4):
        if y + i <= 9:
            if a[y + i][x] == 1 or a[y + i][x] == 3:
                f1 = False
            if f1:
                if a[y + i][x] == 4:
                    d['yd'] += 1
                if a[y + i][x] == 2:
                    d1['yd'] += 1

        if y - i >= 0:
            if a[y - i][x] == 1 or a[y - i][x] == 3:
                f2 = False
            if f2:
                if a[y - i][x] == 4:
                    d['yu'] += 1
                if a[y - i][x] == 2:
                    d1['yu'] += 1

        if x + i <= 9:
            if a[y][x + i] == 1 or a[y][x + i] == 3:
                f3 = False
            if f3:
                if a[y][x + i] == 4:
                    d['xr'] += 1
                if a[y][x + i] == 2:
                    d1['xr'] += 1

        if x - i >= 0:
            if a[y][x - i] == 1 or a[y][x - i] == 3:
                f4 = False
            if f4:
                if a[y][x - i] == 4:
                    d['xl'] += 1
                if a[y][x - i] == 2:
                    d1['xl'] += 1
    return d, d1


def fillneardead(x, y, napr, kolp, a):
    if napr == 2:
        for i in range(kolp):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    if (y + j >= 0 and y + j < 10) and (x + i + k >= 0 and x + i + k < 10):
                        a[y + j][x + i + k] = 1
    elif napr == 1:
        for i in range(kolp):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    if (y + j + i >= 0 and y + j + i < 10) and (x + k >= 0 and x + k < 10):
                        a[y + j + i][x + k] = 1


def comphod():
    f = False
    while not f:
        x = randint(0, 9)
        y = randint(0, 9)
        if a1[y][x] != 1 and a1[y][x] != 2 and a1[y][x] != 5:
            f = True
    if a1[y][x] == 4:
        k, e = dead(x, y, a1)
        for key in k.keys():
            if k[key] > 0:
                f = True
                break
        if f:
            a1[y][x] = 2
        if not f:
            if e['xl'] > 0 or e['xr'] > 0:
                fillneardead(x - e['xl'], y, 2, e['xl'] + e['xr'] + 1, a1)
            elif e['yu'] > 0 or e['yd'] > 0:
                fillneardead(x, y - e['yu'], 1, e['yu'] + e['yd'] + 1, a1)
            elif e['xl'] == 0 and e['xr'] == 0 and e['yu'] == 0 and e['yd'] == 0:
                fillneardead(x, y - e['yu'], 1, e['yu'] + e['yd'] + 1, a1)
            for key in e.keys():
                if e[key] >= 0:
                    for i in range(e[key] + 1):
                        if key == 'yd':
                            a1[y + i][x] = 5
                        if key == 'yu':
                            a1[y - i][x] = 5
                        if key == 'xr':
                            a1[y][x + i] = 5
                        if key == 'xl':
                            a1[y][x - i] = 5
        return True
    else:
        a1[y][x] = 1
        return False
