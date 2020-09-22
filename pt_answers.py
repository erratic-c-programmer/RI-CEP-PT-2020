#! /usr/bin/python3

import csv
from math import sqrt

# Q1


def day_of_2009(day, month):
    lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    cday = 4
    for i in range(month - 1):
        cday += lengths[i]

    cday += day - 1
    cday %= 7

    if cday == 1:
        ans = 'Monday'
    elif cday == 2:
        ans = 'Tuesday'
    elif cday == 3:
        ans = 'Wednesday'
    elif cday == 4:
        ans = 'Thursday'
    elif cday == 5:
        ans = 'Friday'
    elif cday == 6:
        ans = 'Saturday'
    elif cday == 0:
        ans = 'Sunday'

    return ans


def test1():
    print('Q1')
    print(day_of_2009(1, 1) == 'Thursday')
    print(day_of_2009(17, 1) == 'Saturday')
    print(day_of_2009(25, 9) == 'Friday')
    print(
        day_of_2009(25, 12) not in
        ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Saturday', 'Sunday'])


test1()

# Q2(a)


def is_harshad(n):
    return not n % sum([int(x) for x in str(n)])


def test2a():
    print('Q2a')
    print(is_harshad(24))
    print(not is_harshad(25))
    print(is_harshad(156))
    print(not is_harshad(157))


test2a()

# Q2(b)


def harshad(n):
    while True:
        if is_harshad(n):
            return n
        n += 1


def test2b():
    print('Q2b')
    print(harshad(24) == 24)
    print(harshad(25) == 27)
    print(harshad(987654321) == 987654330)


test2b()

# Q3


def euclid_back(a, b):
    rem = a % b
    if not rem:
        return b

    a = b
    b = rem
    return euclid_back(a, b)


def euclid(a, b):
    if a < b:
        a, b = b, a
    return euclid_back(a, b)


def test3():
    print('Q3')
    print(euclid(119, 544) == 17)
    print(euclid(544, 119) == 17)
    print(euclid(64, 8) == 8)


test3()

# Q4


def winner(fname):
    scorefile = open(fname, 'r')
    t = []
    scores = []
    for i in range(5):
        t = []
        for _ in range(4):
            t.append(int(scorefile.read(2)[0]))
        scores.append((i + 1, sum(t)))

    greatest = 0
    for e in scores:
        if e[1] > scores[greatest][1]:
            greatest = i

    return scores[greatest]


def test4():
    print('Q4')
    print(winner('4_test1.txt') == (4, 19))
    print(winner('4_test2.txt') == (2, 17))


test4()

# Q5


def read_csv(csvfilename):
    """
    Reads a csv file and returns a list of list
    containing rows in the csv file and its entries.
    """
    rows = []

    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows.append(row)
    return rows


def top_k_hashtag(fname, k):
    ans = []
    acc = {}
    occ = []

    for cur in read_csv(fname):
        for e in cur[3].split(';'):
            if e != '':
                if e not in acc:
                    acc[e] = 1
                else:
                    acc[e] += 1

    occ = [(acc[x], x) for x in acc]
    occ.sort(reverse=True)
    for i in range(k):
        ans.append(occ[i][1])

    return ans


def test5():
    print('Q5')
    print(top_k_hashtag('donald-tweets.csv', 1) == ['Trump2016'])
    print(
        top_k_hashtag('donald-tweets.csv', 2) ==
        ['Trump2016', 'MakeAmericaGreatAgain'])
    print(
        top_k_hashtag('donald-tweets.csv', 3) ==
        ['Trump2016', 'MakeAmericaGreatAgain', 'MAGA'])
    print(
        top_k_hashtag('donald-tweets.csv', 5) == [
            'Trump2016', 'MakeAmericaGreatAgain', 'MAGA', 'DrainTheSwamp',
            'AmericaFirst'
        ])


test5()

# Q6


class Money:
    def __init__(self, dollars, cents):
        self.dol = dollars + (cents >= 100)
        self.cen = cents % 100

    def __str__(self):
        return f'SGD$ {self.dol}.{self.cen}'

    def get_dollars(self):
        return self.dol

    def get_cents(self):
        return self.cen

    def get_MYR(self):
        return f'{(self.dol + self.cen/100) * 3.1:.2f}'

    def __add__(self, value):
        return Money(self.dol + value.dol, self.cen + value.cen)


def test6():
    print('Q6')
    a = Money(5, 95)
    b = Money(10, 108)
    print(a.get_dollars() == 5)
    print(a.get_cents() == 95)
    print(b.get_dollars() == 11)
    print(b.get_cents() == 8)
    print(a.get_MYR() == '18.45')
    print(b.get_MYR() == '34.35')
    c = a + b
    print(c.get_dollars() == 17)
    print(c.get_cents() == 3)


test6()

###Question 7###

#Question 7a


def create_grid(n):
    ans = []
    for i in range(int(sqrt(4**n))):
        t = []
        for j in range(int(sqrt(4**n))):
            t.append((j, i))
        ans.append(t)

    return ans


def test7a():
    print('Q7a')
    print(create_grid(0) == [[(0, 0)]])
    print(create_grid(1) == [[(0, 0), (1, 0)], [(0, 1), (1, 1)]])
    print(
        create_grid(2) == [[(0, 0), (1, 0), (2, 0), (
            3, 0)], [(0,
                      1), (1,
                           1), (2, 1), (3, 1)], [(0, 2), (1, 2), (2, 2), (
                               3, 2)], [(0, 3), (1, 3), (2, 3), (3, 3)]])
    print(
        create_grid(3) ==
        [[(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)],
         [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)
          ], [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (
              7, 2
          )], [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3)],
         [(0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4)
          ], [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5)],
         [(0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)],
         [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7)]])


test7a()

#Question 7b


def zoom(grid, n):
    ans = []
    t = []
    edgelen = len(grid[0])
    if edgelen == 0:
        t.append(grid[0])

    elif n == 0:
        for i in range(edgelen // 2):
            for j in range(edgelen // 2):
                t.append(grid[i][j])

    elif n == 1:
        for i in range(edgelen // 2, edgelen):
            for j in range(edgelen // 2):
                t.append(grid[i][j])

    elif n == 2:
        for i in range(edgelen // 2, edgelen):
            for j in range(edgelen // 2):
                t.append(grid[i][j])

    elif n == 3:
        for i in range(edgelen // 2, edgelen):
            for j in range(edgelen // 2, edgelen):
                t.append(grid[i][j])

    ans.append(t)
    return ans


def test7b():
    print('Q7b')
    print(
        zoom([[(0, 0), (1, 0), (2, 0), (3, 0)], [(0, 1), (1, 1), (2, 1), (
            3, 1)], [(0, 2), (1, 2), (2, 2), (
                3, 2)], [(0, 3), (1, 3), (2, 3), (3, 3)]], 2) == [[(
                    0, 2), (1, 2)], [(0, 3), (1, 3)]])
    print(
        zoom([[(0, 0), (1, 0), (2, 0), (3, 0)], [(0, 1), (1, 1), (2, 1), (
            3, 1)], [(0, 2), (1, 2), (2, 2), (
                3, 2)], [(0, 3), (1, 3), (2, 3), (3, 3)]], 3) == [[(
                    2, 2), (3, 2)], [(2, 3), (3, 3)]])
    print(
        zoom([[(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)],
              [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)],
              [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2)],
              [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3)],
              [(0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4)],
              [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5)],
              [(0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)],
              [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6,
                                                                7), (7,
                                                                     7)]], 2)
        == [[(0, 4), (1, 4), (2, 4), (3, 4)], [(0, 5), (1, 5), (2, 5), (
            3, 5)], [(0, 6), (1, 6), (2,
                                      6), (3,
                                           6)], [(0, 7), (1, 7), (2, 7), (3,
                                                                          7)]])


test7b()

#Question 7c


def quad_to_coor(quad):
    pass


def test7c():
    print('Q7c')
    print(quad_to_coor('3') == (1, 1, 1))
    print(quad_to_coor('130') == (3, 6, 2))
    print(quad_to_coor('13012') == (5, 26, 9))


#test7c()
