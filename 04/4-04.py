# Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.

my_list = [1, 1, 2, 3, 3, 4, 11, 12, 11, 45, 5, 6, 77, 99]
print(my_list)
new_list = [el for el in my_list if my_list.count(el) == 1]
print(new_list)