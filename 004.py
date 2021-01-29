translation = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('text4.txt', 'r', encoding='utf-8') as file:
    for i in file:
        i = i.split(' ', 1)
        new_file.append(translation[i[0]] + '  ' + i[1])
    print(new_file)

with open('text4_new.txt', 'w', encoding='utf-8') as file_2:
    file_2.writelines(new_file)
