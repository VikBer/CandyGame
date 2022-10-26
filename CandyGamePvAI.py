from random import randint, choice

greeting = ('Добро пожаловать в игру "Забери все конфеты!"' 
    '\nОсновные правила игры: дано некоторое число конфет.'
    ' Два игрока по очереди берут конфеты, не больше оговоренного числа'
    '\nЦель игры - забрать последнюю конфету. Победитель забирает все конфеты себе :-) '
    '\nИгрок, нарушающий правила и пытающийся взять больше конфет, чем можно выбывает из игры после трех попыток взять конфеты.')
            

messages = ['Ваша очередь брать конфеты', 'возьмите конфеты', 
            'сколько конфет возьмёте?', 'берите, не стесняйтесь', 'Ваш ход']


def introduce_players():
    player1 = input('Давайте познакомимся. Как Вас зовут?\n')
    player2 = 'Терминатор'
    print(f'Очень приятно, меня зовут {player2}. Я принесу славу роду машин своей победой над тобой!')
    return [player1, player2]


def get_rules(players):
    total = int(input('Сколько конфет будем разыгрывать?\n '))
    maxPerTurn = int(input('Сколько максимально будем брать конфет за один ход?\n '))
    first = int(input(
        f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу\n'))
    if first != 1:
        first = 0
    return [total, maxPerTurn, int(first)]


def play_game(rules, players, messages):
    count = rules[2]
    if rules[0] % 10 == 1 and 9 > rules[0] > 10:
        letter = 'а'
    elif 1 < rules[0] % 10 < 5 and 9 > rules[0] > 10:
        letter = 'ы'
    else:
        letter = ''
    while rules[0] > 0:
        if not count % 2:
            move = randint(1, rules[1])
            print(f'Я забираю {move}')
        else:
            print(f'{players[0]}, {choice(messages)}')
            move = int(input())
            if move > rules[0] or move > rules[1]:
                print(
                    f'Это слишком много, можно взять не более {rules[1]} конфет{letter}, у нас всего {rules[0]} конфет{letter}')
                attempt = 3
                while attempt > 0:
                    if rules[0] >= move <= rules[1]:
                        break
                    print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                    move = int(input())
                    attempt -= 1
                else:
                    return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
        rules[0] = rules[0] - move
        if rules[0] > 0:
            print(f'Осталось {rules[0]} конфет{letter}')
        else:
            print('Все конфеты разобраны.')
        count += 1
    return players[count % 2]


print(greeting)

players = introduce_players()
rules = get_rules(players)

winner = play_game(rules, players, messages)
if not winner:
    print('У нас нет победителя.')
else:
    print(
        f'Поздравляю! В этот раз победил {winner}! Ему достаются все конфеты!')