import random


def getRandomSequence(begin, end, lenght):
    numbers = list()
    while len(numbers) < lenght:
        num = random.randrange(begin, end + 1, 1)
        if num not in numbers:
            numbers.append(num)

    return numbers


def generateCard():
    numbers = getRandomSequence(1, 30, 15)
    card = []
    n = 0
    for line in range(3):
        positions = getRandomSequence(0, 9, 5)
        positions = sorted(positions)

        for i in range(9):
            if i in positions:
                card.append(numbers[n])
                n += 1
            else:
                card.append(0)
    print(card)
    return card


def drowCard(card, owner_name):
    len_card = 15 * 2

    # first line
    pref = 10 * '-' + owner_name
    print(pref + (len_card - len(pref)) * '-')

    for pos in range(27):
        if pos % 9 == 0:
            print()
        if card[pos] == 0:
            print('  ', end=' ')
        elif card[pos] == -1:
            print('--', end=' ')
        elif card[pos] / 10 < 1:
            print('0' + str(card[pos]), end=' ')
        else:
            print(card[pos], end=' ')

    print()
    print(len_card * '-')


out = []


def getNum():
    r = random.randrange(1, 30, 1)
    if r not in out:
        out.append(r)
        print(out)
        print(r)
        return r
    else:
        getNum()


card = generateCard()
comp_card = generateCard()

drowCard(card, 'Ваша карта')
drowCard(comp_card, 'Карта компа')

cont = 'y'

while cont == 'y':
    r = getNum()

    # your move

    res = input('Зачеркнуть или продолжить (x/c)')
    if res == 'x':
        if r in card:
            index = card.index(r)
            card.remove(r)
            card.insert(index, -1)
        else:
            break
    elif res == 'c':
        if r in card:
            break

    # comp move
    if r in comp_card:
        index = comp_card.index(r)
        comp_card.remove(r)
        comp_card.insert(index, -1)

    # cont = input('continue?(y)')

    drowCard(card, 'Ваша карта')
    drowCard(comp_card, 'Карта компа')
