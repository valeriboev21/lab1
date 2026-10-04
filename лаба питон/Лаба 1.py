import time

BLUE = '\u001b[44m'
RED = '\u001b[41m'
WHITE = '\u001b[47m'
RESET = '\u001b[0m'
ERASE = '\x1B[2K'
BEGIN = '\x1B[1G'
GREEN = '\u001b[42m'

# Задание 1: флаг Таиланда (полосы 1:1:2:1:1, красная-белая-синяя-белая-красная)
def flag():
    pixel = '  '
    lenght = 18
    stripe = 2  # высота одной единицы полосы в строках
    colors = [RED, WHITE, BLUE, BLUE, WHITE, RED]  # синяя полоса в 2 раза шире

    for color in colors:
        for i in range(stripe):
            print(color + pixel * lenght + RESET)


# Задание 2: повторяющийся узор f
def pattern():
    # Узор f: две дуги, сходящиеся в вершине. Форма задана списками, анимация - 4 кадра.
    pixel = '  '
    height = 7                          # высота узора в строках
    width = 14                          # ширина узора в пикселях
    offsets = [5, 5, 4, 4, 2, 0, 0]     # в каждой строке: сколько пикселей пропустить от дуги
    lenghts = [2, 2, 3, 2, 3, 4, 3]     # в каждой строке: длина дуги в пикселях
    colors = [87, 196, 226, 46]         
 
    while True:                                   
        for frame, color in enumerate(colors):    # enumerate даёт номер кадра (0-3) и его цвет
            for line in range(height):            # рисуем узор строка за строкой
                offset = offsets[line]            # берём из списков значения для этой строки
                lenght = lenghts[line]
                gap = width - offset * 2 - lenght * 2   # пустое место между дугами
                # Левая дуга + пробел + правая дуга (зеркальная копия, поэтому те же offset и lenght)
                figure = pixel * offset + f'\u001b[48;5;{color}m' + pixel * lenght + RESET
                figure += pixel * gap + f'\u001b[48;5;{color}m' + pixel * lenght + RESET
                #pixel * frame сдвигает узор вправо на номер кадра
                print(ERASE + pixel * frame + figure)
            # Два print ниже добавляют по переводу строки, поэтому вверх на height + 2:
            # так курсор возвращается ровно к первой строке узора, и следующий кадр рисуется поверх
            print(f'\u001b[{height + 2}A')
            print(BEGIN)
            time.sleep(0.5)


# диаграмма для последовательности (больше 5 и меньше 5, отрицательные отбросить)
def sequence():
    file = open('sequence.txt', 'r')
    more = []
    less = []
    for line in file: # читаем файл построчно
        number = float(line)
        if number < 0:
            continue
        if number > 5:
            more.append(number)
        elif number < 5:
            less.append(number)
    file.close()
    total = len(more) + len(less)
    print(f'{BLUE}{" " * int(len(more) / 5)}{RESET} {len(more) / total * 100}%')
    print(f'{RED}{" " * int(len(less) / 5)}{RESET} {len(less) / total * 100}%')


#flag()
#pattern()
#sequence()

