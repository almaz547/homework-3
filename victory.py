'''import random

dist_famous_people = {'Александр Сергеевич Пушнин': '26.06.1799', 'Михаил Юрьевич Лермонтов': '15.10.1814', 'Сергей Александрович Есенин': '03.10.1895', 'Владимир Семенович Высоцкий': '25.01.1938', 'Виктор Робертович Цой': '21.06.1962', 'Константин Эдуардович Циолковский': '17.09.1857', 'Сергей Павлович Королев': '12.01.1907', 'Валентин Петрович Глушко': '20.08.1908', 'Андрей Николаевич Туполев': '29.10.1888', 'Юрий Алексеевич Гагарин': '09.03.1934'}
dist_famous_people_x = {'Александр Сергеевич Пушнин': 'Двадцать шестого июня 1799 года', 'Михаил Юрьевич Лермонтов': 'Пятнадцатого октября 1814 года', 'Сергей Александрович Есенин': 'Третьего октября 1895 года', 'Владимир Семенович Высоцкий': 'Двадцать пятого января 1938 года', 'Виктор Робертович Цой': 'Двадцать первого июня 1962 года', 'Константин Эдуардович Циолковский': 'Семнадцатого сентября 1857 года', 'Сергей Павлович Королев': 'Двенадцатого января 1907 года', 'Валентин Петрович Глушко': 'Двадцатого августа 1908 года', 'Андрей Николаевич Туполев': 'Двадцать девятого октября 1888 года', 'Юрий Алексеевич Гагарин': 'Девятого марта 1934 года'}
famous_people = ['Александр Сергеевич Пушнин', 'Михаил Юрьевич Лермонтов', 'Сергей Александрович Есенин', 'Владимир Семенович Высоцкий', 'Виктор Робертович Цой', 'Константин Эдуардович Циолковский', 'Сергей Павлович Королев', 'Валентин Петрович Глушко', 'Андрей Николаевич Туполев', 'Юрий Алексеевич Гагарин']

new_test = 'да'
while new_test == "да":
    answer_es = 0
    data_quiz = random.sample(famous_people, 5)
    #print(data_quiz)
    print('Винторина: назовите дату рождения пяти знаменитых людей')
    question_1 = input(f'Назовите дату рождения {data_quiz[0]},в формате число.месяц.год: ')
    if question_1 == dist_famous_people.get(data_quiz[0]):
        print('Ответ верный !')
        answer_es += 1
        question_2 = input(f'Назовите дату рождения {data_quiz[1]}, в формате число.месяц.год: ')
    else:
        print(f'Неверно ! ,правильный ответ: {dist_famous_people_x.get(data_quiz[0])}')
        question_2 = input(f'Назовите дату рождения {data_quiz[1]}, в формате число.месяц.год: ')
    if question_2 == dist_famous_people.get(data_quiz[1]):
        print('Ответ верный !')
        answer_es += 1
        question_3 = input(f'Назовите дату рождения {data_quiz[2]}, в формате число.месяц.год: ')
    else:
        print(f'Неверно ! ,правильный ответ: {dist_famous_people_x.get(data_quiz[1])}')
        question_3 = input(f'Назовите дату рождения {data_quiz[2]}, в формате число.месяц.год: ')
    if question_3 == dist_famous_people.get(data_quiz[2]):
        print('Ответ верный !')
        answer_es += 1
        question_4 = input(f'Назовите дату рождения {data_quiz[3]}, в формате число.месяц.год: ')
    else:
        print(f'Неверно ! ,правильный ответ: {dist_famous_people_x.get(data_quiz[2])}')
        question_4 = input(f'Назовите дату рождения {data_quiz[3]}, в формате число.месяц.год: ')
    if question_4 == dist_famous_people.get(data_quiz[3]):
        print('Ответ верный !')
        answer_es += 1
        question_5 = input(f'Назовите дату рождения {data_quiz[4]}, в формате число.месяц.год: ')
    else:
        print(f'Неверно ! ,правильный ответ: {dist_famous_people_x.get(data_quiz[3])}')
        question_5 = input(f'Назовите дату рождения {data_quiz[4]}, в формате число.месяц.год: ')
    if question_5 == dist_famous_people.get(data_quiz[4]):
        print('Ответ верный !')
        answer_es += 1
    else:
        print(f'Неверно ! ,правильный ответ: {dist_famous_people_x.get(data_quiz[4])}')
    print(f'Количество правильных ответов: {answer_es}')
    print(f'Количество неправильных ответов: {5 - answer_es}')
    new_test = input("Если хотите продолжить тест введите: да ,если не хотите, введите: нет:  ")
    while new_test != 'да' and new_test != 'нет':
        print("Введите либо: да , либо: нет !")
        new_test = input("Если хотите продолжить тест введите: да ,если не хотите, введите: нет!: ")'''






import random

dist_famous_people = {'Александр Сергеевич Пушкин': '26.06.1799', 'Михаил Юрьевич Лермонтов': '15.10.1814', 'Сергей Александрович Есенин': '03.10.1895', 'Владимир Семенович Высоцкий': '25.01.1938', 'Виктор Робертович Цой': '21.06.1962', 'Константин Эдуардович Циолковский': '17.09.1857', 'Сергей Павлович Королев': '12.01.1907', 'Валентин Петрович Глушко': '20.08.1908', 'Андрей Николаевич Туполев': '29.10.1888', 'Юрий Алексеевич Гагарин': '09.03.1934'}
dist_famous_people_x = {'Александр Сергеевич Пушкин': 'Двадцать шестого июня 1799 года', 'Михаил Юрьевич Лермонтов': 'Пятнадцатого октября 1814 года', 'Сергей Александрович Есенин': 'Третьего октября 1895 года', 'Владимир Семенович Высоцкий': 'Двадцать пятого января 1938 года', 'Виктор Робертович Цой': 'Двадцать первого июня 1962 года', 'Константин Эдуардович Циолковский': 'Семнадцатого сентября 1857 года', 'Сергей Павлович Королев': 'Двенадцатого января 1907 года', 'Валентин Петрович Глушко': 'Двадцатого августа 1908 года', 'Андрей Николаевич Туполев': 'Двадцать девятого октября 1888 года', 'Юрий Алексеевич Гагарин': 'Девятого марта 1934 года'}
famous_people = ['Александр Сергеевич Пушкин', 'Михаил Юрьевич Лермонтов', 'Сергей Александрович Есенин', 'Владимир Семенович Высоцкий', 'Виктор Робертович Цой', 'Константин Эдуардович Циолковский', 'Сергей Павлович Королев', 'Валентин Петрович Глушко', 'Андрей Николаевич Туполев', 'Юрий Алексеевич Гагарин']

new_test = 'да'
while new_test == "да":
    data_quiz = random.sample(famous_people, 5)
    print('Винторина: назовите дату рождения пяти знаменитых людей')
    answer_es = 0
    for i in range(len(data_quiz)):
        question = input(f'Назовите дату рождения {data_quiz[i]},в формате число.месяц.год: ')
        if question == dist_famous_people.get(data_quiz[i]):
            print('Ответ верный !')
            answer_es += 1
        else:
            print(f'Неверно ! ,правильный ответ: {dist_famous_people_x.get(data_quiz[i])}')
    print(f'Количество правильных ответов: {answer_es}')
    print(f'Количество неправильных ответов: {5 - answer_es}')
    print(f'Процент правильных ответов {answer_es*100/5}')
    print(f'Процент неправильных ответов {(5-answer_es)*100/5}')
    new_test = input("Если хотите продолжить тест введите: да ,если не хотите, введите: нет:  ")
    while new_test != 'да' and new_test != 'нет':
        print("Введите либо: да , либо: нет !")
        new_test = input("Если хотите продолжить участие в викторине введите: да ,если не хотите, введите: нет!: ")
print('Спасибо за участие в викторине !')







