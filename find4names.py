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
                'дата': transform_string_date_to_list(robbery_list[4]),
                'пойман': robbery_list[5] == 'T',
                'речь': robbery_list[6]
            }
            robberies.append(robbery_dict)
    return robberies


def transform_string_date_to_list(string):
    """
    :param string: "11-11-2132"
    :return: [11, 11, 2132]
    """
    lst = string.split('-')  # ['11', '11', '2132']
    new_list = []
    for str_num in lst:
        new_list.append(int(str_num))
    return new_list


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


def find_konfetolub():  # Лопаточка
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


def find_city():  # Здесьтаун
    robberies = get_robberies()
    cities_counts = {}
    for robbery in robberies:
        if robbery['город'] == 'Джастленд':
            continue
        if robbery['город'] not in cities_counts:
            cities_counts[robbery['город']] = 0

        cities_counts[robbery['город']] += 1

    max_city = ""
    max_count = 0
    for city in cities_counts:
        if max_count < cities_counts[city]:
            max_count = cities_counts[city]
            max_city = city

    print(cities_counts)
    print(max_city)


def find_nuker():  # Воробоб
    robberies = get_robberies()
    thieves_counts = {}
    for robbery in robberies:
        if robbery['пойман']:
            count = count_nu_in_string(robbery['речь'])
            if robbery['имя'] not in thieves_counts:
                thieves_counts[robbery['имя']] = 0
            thieves_counts[robbery['имя']] += count

    print(thieves_counts)
    for thief in thieves_counts:
        if thieves_counts[thief] > 5:
            print(thieves_counts[thief], thief)


def count_nu_in_string(string):
    """
    "Ну нуно не винувен ну..." -> 2
    """
    count = 0
    words = string.split(' ')  # ['Ну', "нуно", "не", "винувен", "ну..."]
    for word in words:
        clear_word = word_cleaner(word)
        if clear_word == 'ну':
            count += 1

    return count


def word_cleaner(word):  # "Ну..!,?%" -> "ну"
    """
    .НУБЫвтфывФЫВФвфыПФПРФУ!"!№
    нубывтфывывывфыпфпрфу
    """
    clear_word = ""
    for symbol in word:
        if symbol.isalpha():
            clear_word += symbol.lower()
    return clear_word


def packer(robberies):
    """
    :param robberies: список ограблений
    :return: упакованный словарь с ворами и списками их дат
    {
    'Bob': [[12, 23, 1552], [14, 29, 1625]],
    'Boba': [...],
    ...
    }
    """
    thieves_dates = {}
    for robbery in robberies:
        if not robbery['пойман']:
            date = robbery['дата']
            name = robbery['имя']
            if name not in thieves_dates:
                thieves_dates[name] = []

            thieves_dates[name].append(date)
    return thieves_dates


def find_4_month_thief():  # Копырсанка
    robberies = get_robberies()
    thieves_dates = packer(robberies)
    for thief in thieves_dates:
        dates = thieves_dates[thief]
        sort_dates(dates)
        max_seria = find_max_seria(dates)
        if max_seria == 4:
            print(thief)


def sort_dates(dates):
    ogr = len(dates) - 1
    while ogr > 0:
        i = 0
        while i < ogr:
            if is_date_bigger(dates[i], dates[i+1]):
                temp = dates[i]
                dates[i] = dates[i + 1]
                dates[i + 1] = temp
            i += 1
        ogr -= 1


def is_date_bigger(date1, date2):
    """
    :param date1: [1, 4, 2020]
    :param date2: [12, 6, 2018]
    :return: True
    """
    i = 2
    while i >= 0:
        if date1[i] > date2[i]:
            return True
        if date1[i] < date2[i]:
            return False
        i -= 1

    return False


def testcase1():
    d = [[1, 14, 2020], [1, 11, 2030], [1, 11, 2020]]
    sort_dates(d)
    print(d)


def razryv(date1, date2):
    """
    date2 > date1
    :param date1:
    :param date2:
    :return:
    """
    years_dif = date2[2] - date1[2]  # 0
    month_dif = date2[1] - date1[1]  # 3
    dif = years_dif * 12 + month_dif
    return dif


def find_max_seria(dates):
    i = 1
    m = 1
    max_ = 0
    while i < len(dates):
        dif = razryv(dates[i - 1], dates[i])
        if dif == 1:
            m += 1
        else:
            if m > max_:
                max_ = m
                m = 1
        i += 1

    if m > max_:
        max_ = m

    return max_


find_4_month_thief()
