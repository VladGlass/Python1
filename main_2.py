list_1 = []
question = int(input('Сколько кубов вычислить: '))
i = 0
#1
while (i < question):
    i += 1
    if (i % 2 != 0):
        list_1.append(i ** 3)
final_sum = 0
for i in list_1:
    def sum(n):
        summ = 0
        while n > 0:
            summ += n % 10
            n //= 10
        return summ
    if(sum(i) % 7 == 0):
        #print (i)
        #print (sum(i))
        if((sum(i)) % 7 == 0):
            final_sum = final_sum + i
#2
for i in range(len(list_1)):
      list_1[i] = list_1[i] + 17
final_sum_2 = 0
for i in list_1:
    def sum_2(n_2):
        summ_2 = 0
        while n_2 > 0:
            summ_2 += n_2 % 10
            n_2 //= 10
        return summ_2
    if(sum_2(i) % 7 == 0):
        #print (i)
        #print (sum(i))
        if ((sum(i)) % 7 == 0):
            final_sum_2 = final_sum_2 + i
print('Сумма чисел из списка нечётных кубов до', question,'сумма цифр которых делится на 7 нацело:', final_sum)
print('Сумма чисел из списка нечётных кубов до', question,'сумма цифр которых делится на 7 нацело, при сложении 17 к каждому числа из списка:', final_sum_2)
