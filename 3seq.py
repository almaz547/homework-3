
data_first = input('Введите елементы первого списка через запятую: ')
list_first = []
while len(data_first):
    data_first = data_first.split(',')
    for element in data_first:
        list_first.append(element)
    data_first = input('Дополните первый список через запятуя, или нажмите Enter: ')
print(list_first)
data_second = input('Введите второй список через запятуя: ')
list_second = []
while len(data_second):
    data_second = data_second.split(',')
    for element in data_second:
        list_second.append(element)
    data_second = input('Дополните второй список через запятуя, или нажмите Enter: ')
print(list_second)
i = 0
while i < len(list_first):
    if list_first[i] in list_second:
        list_first.pop(i)
    else:
        i += 1
print(list_first)





