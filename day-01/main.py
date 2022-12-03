def getInput():
    return open('input.txt').read().rstrip('\n')


def getElfs():
    return getInput().split('\n\n')


def getElfCalories():
    elfCalories = []
    for elf in getElfs():
        elfCalories.append(sum(map(int, elf.split('\n'))))
    return elfCalories


def part_1():
    print('Part 1 answer: %s' % max(getElfCalories()))


def part_2():
    print('Part 2 answer: %s' %
          sum(sorted(getElfCalories(), reverse=True)[:3]))


part_1()
part_2()
