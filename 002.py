with open('text2.txt', 'r', encoding='utf-8') as f:
    line = 0
    for i in f:
        line += 1

        flag = 0
        word = 0
        for j in i:
            if j != ' ' and flag == 0:
                word += 1
                flag = 1
            elif j == ' ':
                flag = 0

        print(f'{line} - {word}, слов(о).')
    print('Строк в файле:', line)
