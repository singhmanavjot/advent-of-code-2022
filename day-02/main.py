def getInput():
    return open('input.txt').read().rstrip('\n')


def getMatches():
    return getInput().split('\n')


def getShapePoints(shape):
    return {'X': 1, 'Y': 2, 'Z': 3}[shape]


def getMatchPoints(me, opponent):
    return {('X', 'B'): 0, ('X', 'A'): 3, ('X', 'C'): 6,
            ('Y', 'C'): 0, ('Y', 'B'): 3, ('Y', 'A'): 6,
            ('Z', 'A'): 0, ('Z', 'C'): 3, ('Z', 'B'): 6}[(me, opponent)]


def convertShape(shape, opponent):
    return {('X', 'A'): 'Z', ('X', 'B'): 'X', ('X', 'C'): 'Y',
            ('Y', 'A'): 'X', ('Y', 'B'): 'Y', ('Y', 'C'): 'Z',
            ('Z', 'A'): 'Y', ('Z', 'B'): 'Z', ('Z', 'C'): 'X'}[(shape, opponent)]


def part_1():
    score = 0
    for match in getMatches():
        opponent, me = match.split()
        score += getShapePoints(me)
        score += getMatchPoints(me, opponent)
    print('Part 1 answer: %s' % score)


def part_2():
    score = 0
    for match in getMatches():
        opponent, me = match.split()
        me = convertShape(me, opponent)
        score += getShapePoints(me)
        score += getMatchPoints(me, opponent)
    print('Part 2 answer: %s' % score)


part_1()
part_2()
