import re
from num2words import num2words

with open('txt3.txt', 'r') as f:
    while True:
        block = f.read()
        if not block:
            break


        for match in re.findall(r'\b[13579]\d*[13579]\b', block):

            num_str = match[0] + ''.join(filter(lambda c: int(c) % 2 == 1, match[1:]))
            num = int(num_str)


            if num % 2 == 0 and len(re.findall(r'[13579]', num_str)) <= 3:

                print(num_str + '- ' + num2words(num, lang='ru'))