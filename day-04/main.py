import string


def getInput():
    return open('input.txt').read().rstrip('\n')


def getPairs():
    return getInput().split('\n')


def getSections(elf):
    return list(range(int(elf.split('-')[0]), int(elf.split('-')[1])+1))


def part_1():
    contained = 0
    for pair in getPairs():
        elf1, elf2 = pair.split(',')
        elf1Sections = getSections(elf1)
        elf2Sections = getSections(elf2)
        if all(item in elf1Sections for item in elf2Sections) or all(item in elf2Sections for item in elf1Sections):
            contained += 1

    print('Part 1 answer: %s' % contained)


def part_2():
    overlapped = 0
    for pair in getPairs():
        elf1, elf2 = pair.split(',')
        elf1Sections = getSections(elf1)
        elf2Sections = getSections(elf2)
        if any(item in elf1Sections for item in elf2Sections) or any(item in elf2Sections for item in elf1Sections):
            overlapped += 1

    print('Part 2 answer: %s' % overlapped)


part_1()
part_2()
