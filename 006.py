import re


subj = {}
with open('text6.txt', 'r', encoding='utf-8') as f:
    for line in f:
        sum_hours = 0
        hours = re.findall(r'\d+', line)
        for hour in hours:
            sum_hours += int(hour)
        subj[line.split()[0]] = sum_hours
    print(f'Общее количество часов по предмету:\n{subj}')
