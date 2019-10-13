
number_elements = int(input('Введите количество элементов:  '))
elements = []
for i in range(number_elements):
    element = int(input(f'Вводите элемент № {i + 1}:   '))
    elements.append(element)
elements.sort()
print(elements)
