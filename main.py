input_list = input("Введіть список цілих чисел, розділених пробілами: ").split()
number_to_find = int(input("Введіть число, яке потрібно знайти: "))
input_list = [int(x) for x in input_list]
count = input_list.count(number_to_find)
print(f"Число {number_to_find} зустрічається {count} разів у введеному списку.")

