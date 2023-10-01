input_list = input("Введіть елементи списку цілих чисел, розділені пробілами: ").split()

input_list = [int(x) for x in input_list]

sum_of_elements = sum(input_list)

average = sum_of_elements / len(input_list)

print(f"Сума всіх елементів: {sum_of_elements}")
print(f"Середнє арифметичне: {average}")

