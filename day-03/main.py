import string


def getInput():
    return open('input.txt').read().rstrip('\n')


def getRucksacks():
    return getInput().split('\n')


def getGroups(rucksacks, size):
    for i in range(0, len(rucksacks), size):
        yield rucksacks[i:i + size]


def part_1():
    prio = 0
    for rucksack in getRucksacks():
        middle = int(len(rucksack)/2)
        left, right = rucksack[:middle], rucksack[middle:]
        character = ''.join(set(left).intersection(right))
        prio += string.ascii_letters.index(character) + 1

    print('Part 1 answer: %s' % prio)


def part_2():
    prio = 0
    for group in getGroups(getRucksacks(), 3):
        character = ''.join(set(group[0]).intersection(group[1]))
        character = ''.join(set(character).intersection(group[2]))
        prio += string.ascii_letters.index(character) + 1

    print('Part 2 answer: %s' % prio)


part_1()
part_2()
