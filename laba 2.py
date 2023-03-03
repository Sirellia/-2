import re
digit_words = {
    '1': 'один',
    '2': 'два',
    '3': 'три',
    '4': 'четыре',
    '5': 'пять',
    '6': 'шесть',
    '7': 'семь',
    '8': 'восемь',
    '9': 'девять'
}
pattern = re.compile(r'\d+')
with open('txt3.txt', 'r') as f:
    for line in f:
        numbers = pattern.findall(line)
        for number in numbers:
            if int(number) > 0:
                if int(number) % 2 == 0:
                    if len([x for x in number if int(x) % 2 == 1]) <= 3:
                        if int(number[0]) % 2 == 1:
                            print(number, digit_words[number[0]], '-', ' '.join([digit_words[x] for x in number if int(x) % 2 == 1]))
