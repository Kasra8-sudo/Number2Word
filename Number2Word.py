'''
Number To Word 

persion number python

@Kasra8-sudo

'''

sef_bis = ['sefr', 'yek', 'do', 'se', 'chahar',
           'panj', 'shish', 'haft', 'hasht', 'noh', 'dah', 'yazdah', 'davazdah', 'sizdah', 'chahardah',
           'panezdah', 'shanezdah', 'hefdah', 'hijdah', 'nuzdah']

tens = ['', '', 'bist', 'si', 'chehel',
        'panjah', 'shast', 'haftad', 'hashtad', 'navad']

tousend = ['', 'sad', 'divist', 'sisad', 'chaharsad',
           'pansad', 'shishsad', 'haftsad', 'hashsad', 'nohsad']

add_bozorg = ['', 'hezar ', 'milion ', 'milyadr ', 'Billion ', 'Trillion ', 'Quadrillion ', 'Quintillion ', 'Sextillion ', 'Septillion', 'Octillion', 'Nonillion',
              'Decillion', 'Undecillion', 'Dodecillion', 'Tredecillion', 'Quattuordecillion ', 'Quindecillion', 'Sexdecillion', 'Septendecillion', 'Octodecillion', 'Nov']

karbar = ('{:,}'.format(int(input('Enter : ')) * 10)).split(',')

def doraqam(num):
    if num >= 0 and num < 20:
        return f'{sef_bis[num]}'

    elif num >= 20 and num < 100:
        if num % 10 == 0:
            return f'{tens[num // 10]}'
        return f"{tens[num // 10]} o {sef_bis[num % 10]}"


def seragam(num):
    if num >= 0 and num < 100:
        return doraqam(num)
    elif num >= 100 and num < 1000:
        if num % 100 == 0:
            return f'{tousend[num // 100]}'
        else:
            return f'{tousend[num // 100]} o {doraqam(num % 100)} '


def koli(lst: list):
    global horof
    horof = ''
    for i in range(len(lst)):
        if lst[i] == '000':
            horof += ''
        else:
            horof += seragam(int(lst[i])) + ' ' + \
                add_bozorg[len(lst) - i - 1] + 'o '
    h1 = horof.split()
    h1.reverse()
    h2 = ''
    for i in h1:
        h2 += f'{i} '
    h3 = h2.lstrip('o')
    lsts = h3.split()
    lsts.reverse()

    result = ''
    for i in lsts:
        result += f'{i} '

    return result + ' RIYAL '


print(koli(karbar))
