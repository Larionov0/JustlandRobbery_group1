with open('Странное письмо.txt', 'rt') as file:
    text = file.read()  # "1234 516 513 1253 1331"
    numbers = text.split(' ')  # ['1234', '516']

    text2 = ''
    for number_str in numbers:
        if number_str != '':
            number = int(number_str)
            sym = chr(number)
            text2 += sym

with open('Странное письмо (расшифр).txt', 'wt', encoding='utf-8') as file:
    file.write(text2)
