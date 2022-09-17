# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

from random import randint

rnge_cand = 5
candies = 27


def ht(num)->list:   
    nums = [n for n in range(num)]
    res = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            res.append(1)
        else: res.append(2)
    return res

def how_many_take(can, rngcan) ->int:
    res = can//rngcan * rngcan + 1
    if (can//rngcan == 0) or (can == rngcan):
        return can
    elif can - res < 1:
        return rngcan
    else:
        return can - res

whose_turn = ht(candies)
in_hand = 0
i = randint(0,1)

while candies > 0:
    i += 1
    print()
    if whose_turn[i] == 1:
        print(f"На столе {candies} конфет, ходит игрок {whose_turn[i]}")
        print(f"Вы можете взять от одной до {rnge_cand} конфет")
        in_hand = int(input("Сколько взять?"))
        while in_hand < 1 or in_hand > rnge_cand:
            print(f"можно взять только от 0 до {rnge_cand}")
            in_hand = int(input("Сколько взять? "))
        print(f"Игрок {whose_turn[i]} взял {in_hand} конфет")
        candies -= in_hand

    elif whose_turn[i] == 2:
        print(f"На столе {candies} конфет, ходит игрок {whose_turn[i]}")
        print("На игроке 2 бот")
        print(f"Бот забрал {how_many_take(candies, rnge_cand)} конфет")
        candies -= how_many_take(candies, rnge_cand)

print(f"Конфеты кончились побеждает игрок {whose_turn[i]}")
