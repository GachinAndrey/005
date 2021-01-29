import json

firm_dict = []
profit_firm = {}
pr_av = {}
my_dict = 0
average_profit = 0
i = 0
with open('text7.txt', 'r', encoding='utf-8') as file:
    for line in file:
        name, property_form, earning, costs = line.split()
        profit_firm[name] = int(earning) - int(costs)
        if profit_firm.setdefault(name) > 0:
            my_dict = my_dict + profit_firm.setdefault(name)
            i += 1
    if i != 0:
        average_profit = my_dict / i
    else:
        print(f'Прибыль отсутсвует. Все работают в убыток')
    pr_av = {'average_profit': round(average_profit)}
    firm_dict.append(profit_firm)
    firm_dict.append(pr_av)
    print(firm_dict)


with open('text7.json', 'w', encoding='utf-8') as write_js:
    json.dump(firm_dict, write_js)

    js_str = json.dumps(firm_dict)
    print(f'Создан файл с расширением json со следующим содержимым: \n 'f' {js_str}')