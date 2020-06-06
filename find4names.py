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
                'украл': ukral_string_to_dict(robbery_list[3]),
                'дата': robbery_list[4],
                'пойман': robbery_list[5] == 'T',
                'речь': robbery_list[6]
            }
            robberies.append(robbery_dict)
    return robberies


def ukral_string_to_dict(string):
    """
    :param string: "булка#16; трусы; носки"
    :return: {
        "булка": 16,
        'трусы': 1
        'носки': 1
    }
    """
    thefts = string.split('; ')  # ['булка#16', 'трусы', 'носки']
    thefts_dict = {}

    for theft in thefts:  # 'булка#16'
        if '#' in theft:
            theft_count = theft.split('#')  # ['булка', '16']
            thefts_dict[theft_count[0]] = int(theft_count[1])
        else:  # 'трусы'
            thefts_dict[theft] = 1

    return thefts_dict


def find_konfetolub():
    robberies = get_robberies()
    thieves_counts = {}
    for robbery in robberies:
        if 'конфета' in robbery['украл']:
            if robbery['имя'] not in thieves_counts:
                thieves_counts[robbery['имя']] = 0

            thieves_counts[robbery['имя']] += robbery['украл']['конфета']

    max_count = 0
    max_name = ""

    for thief in thieves_counts:
        if thieves_counts[thief] > max_count:
            max_count = thieves_counts[thief]
            max_name = thief

    print(thieves_counts)
    print(f"{max_name} : {max_count}")


find_konfetolub()
