
numbers = input('Введите элементы списка через одинаковый разделитель:  ')
for element in numbers:
    if not element.isalnum():
        sep = element
        break
num_list = [i for i in numbers.split(sep)]
num_list_rezult = []
#num_list_rezult = list(set(num_list))
for element in num_list:
    if num_list.count(element) == 1:
        num_list_rezult.append(element)


print(num_list_rezult)

