with open('text3.txt', 'r', encoding='utf-8') as f:
    salary = []
    poorly_paid = []
    my_list = f.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            poorly_paid.append(i[0])
        salary.append(i[1])
print(f'Оклад меньше 20.000 {poorly_paid}')
print(f'Cредний оклад: {sum(map(int, salary)) / len(salary)}')
