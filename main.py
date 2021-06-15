duration = int(input('Введите кол-во секунд: '))
minutes = ((duration // 60) % 60)
hours = ((duration // 3600) % 24)
days = ((duration // 86400) % 31)
month = ((duration // 2592000) % 12)
years = ((duration // 30585600) % 100)
century = ((duration // 935478927360000) % 100)
word_1 = ('минут')
word_2 = ('часов')
word_3 = ('дней')
word_4 = ('месяцев')
word_5 = ('лет')
word_6 = ('веков')
list_nums_1_1 = [1, 21, 31, 41, 51]
list_nums_1_2 = [2, 22, 32, 42, 52, 3, 23, 33, 43, 53, 4, 24, 34, 44, 54]
list_nums_2_1 = [1, 21]
list_nums_2_2 = [2, 3, 4, 22, 23, 24]
list_nums_3_1 = [1, 21, 31]
list_nums_3_2 = [2, 3, 4, 22, 23, 24]
list_nums_4_1 = [1]
list_nums_4_2 = [2, 3, 4]
list_nums_5_1 = [1, 21, 31, 41, 51, 61, 71, 81, 91]
list_nums_5_2 = [2, 3, 4, 22, 32, 42, 52, 62, 72, 82, 92, 23,
33, 43, 53, 63, 73, 83, 93, 24, 34, 44, 54, 64, 74, 84, 94]
list_nums_6_1 = [1, 21, 31, 41, 51, 61, 71, 81, 91]
list_nums_6_2 = [2, 3, 4, 22, 32, 42, 52, 62, 72, 82, 92, 23, 33,
43, 53, 63, 73, 83, 93, 24, 34, 44, 54, 64, 74, 84, 94]
if minutes in list_nums_1_1:
    word_1 = ('минута')
if minutes in list_nums_1_2:
    word_1 = ('минуты')
if hours in list_nums_2_1:
    word_2 = ('час')
if hours in list_nums_2_2:
    word_2 = ('часа')
if days in list_nums_3_1:
    word_3 = ('день')
if days in list_nums_3_2:
    word_3 = ('дня')
if month in list_nums_4_1:
    word_4 = ('месяц')
if month in list_nums_4_2:
    word_4 = ('месяца')
if years in list_nums_5_1:
    word_5 = ('год')
if years in list_nums_5_2:
    word_5 = ('года')
if century in list_nums_6_1:
    word_6 = ('век')
if century in list_nums_6_2:
    word_6 = ('века')
print(century, word_6, '-', years, word_5,'-', month, word_4, '-', days, word_3, '-', hours, word_2, '-', minutes, word_1)