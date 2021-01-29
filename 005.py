def summary():
    try:
        with open('text5.txt', 'w+', encoding='utf-8') as file:
            line = input('Введите цифры через пробел: \n')
            file.writelines(line)
            numb = line.split()

            print(sum(map(int, numb)))
    except ValueError:
        print('Ошибка ввода')


summary()
