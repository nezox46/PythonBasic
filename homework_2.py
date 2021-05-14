# Задание со звездочкой сделать не смог, не создавая новый список.
my_list = [i ** 3 for i in range(1, 1001, 2)]
sum = 0
second_num = 0
final_num = 0
for num_1 in my_list:
    second_list = list(str(num_1))
    for val_2 in second_list:
        second_num += int(val_2)
        if second_num % 7 == 0:
            sum += second_num
            final_num += sum
print(final_num)