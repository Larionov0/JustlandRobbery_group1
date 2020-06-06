def get_robberies():
    robberies = []
    with open('грабители.csv', 'rt', encoding='utf-8') as file:
        headers = file.readline()
        for line in file:  # "Валли, Хайптаун, минимаркет ЛютыйГусь, трусы#28, 11-11-2132, F, -\n"
            robbery_list = line.rstrip().split(', ')  # ["Валли", "Хайптаун", "минимаркет ЛютыйГусь", "трусы#28", ...]

            robbery_dict = {
                'имя': robbery_list[0],
                'город': robbery_list[1],
                'жертва': robbery_list[2],
                'украл': robbery_list[3],
                'дата': robbery_list[4],
                'пойман': robbery_list[5] == 'T',
                'речь': robbery_list[6]
            }
            robberies.append(robbery_dict)
    return robberies





def find_guy():
    robberies = get_robberies()
    thieves = {}
    for robbery in robberies:
        if robbery['имя'] not in thieves:
            thieves[robbery['имя']] = {
                'успехов': 0,
                'провалов': 0,
                'речи': []
            }

        if robbery['пойман']:
            thieves[robbery['имя']]['провалов'] += 1
            thieves[robbery['имя']]['речи'].append(robbery['речь'])
        else:
            thieves[robbery['имя']]['успехов'] += 1

    for name in thieves:
        if thieves[name]['успехов'] == 5 and thieves[name]['провалов'] == 1:
            print(name)
            print(thieves[name]['речи'])


find_guy()
