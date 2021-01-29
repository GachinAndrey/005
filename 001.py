with open('text1.txt', 'w', encoding='utf-8') as f:
    line = input('Введите текст: \n')
    while line:
        f.write(line + '\n')
        line = input('Введите текст: \n')
        if not line:
            break
