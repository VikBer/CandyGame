
import random

greeting = ('Добро пожаловать в игру "Забери все конфеты!"' 
    '\nОсновные правила игры: дано некоторое число конфет.'
    ' Два игрока по очереди берут конфеты, не больше оговоренного числа'
    '\nЦель игры - забрать последнюю конфету. Победитель забирает все конфеты себе :-) '
    '\nИгрок, нарушающий правила и пытающийся взять больше конфет, чем можно выбывает из игры после трех попыток взять конфеты.')
            

messages = ['Ваша очередь брать конфеты', 'возьмите конфеты', 
            'сколько конфет возьмёте?', 'берите, не стесняйтесь', 'Ваш ход']


def play_game(total, maxPerTurn, players, messages):
    count = 0
    if total%10 == 1 and 9 > total > 10: letter = 'а'
    elif 1 < total%10 < 5 and 9 > total > 10: letter = 'ы'
    else: letter = ''
    while total > 0:
        print(f'{players[count%2]}, {random.choice(messages)}')
        move = int(input())
        if move > total or move > maxPerTurn:
            print(f'Это слишком много, можно взять не более {maxPerTurn} конфет{letter}, у нас всего {total} конфет{letter}')
            attempt = 3
            while attempt > 0:
                if total >= move <= maxPerTurn:
                    break
                print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                move = int(input())
                attempt -=1
            else: 
                print(f'Очень жаль, {players[count%2]} у Вас не осталось попыток. Вы выбываете из игры.')
                return players[not count%2]
        total = total - move
        if total > 0: print(f'Осталось {total} конфет{letter}')
        else: print('Все конфеты разобраны.')
        count +=1
    return players[not count%2]

print(greeting)

player1 = input('\nДавайте познакомимся. \nПервый игрок, как к Вам можно обращаться?\n')
player2 = input('Второй игрок,назовите свое имя\n')
players = [player1, player2]

total = int(input('Сколько конфет будем разыгрывать?\n'))
maxPerTurn = int(input('Сколько максимально будем брать конфет за один ход?\n'))

winner = play_game(total, maxPerTurn, players, messages)
if not winner:
    print('У нас нет победителя.')
else: print(f'Поздравляю! В этот раз победил {winner}! Ему достаются все конфеты!')