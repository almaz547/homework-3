
numbers = input('Введите элементы списка через одинаковый разделитель:  ')
for element in numbers:
    if not element.isalnum():
        sep = element
        break
mmist = [i for i in numbers.split(sep)]
mmist_rezult = list(set(mmist))
print(mmist_rezult)

