def shifrovanie(key, text):
    dimenshion = len(key)
    t = len(text)
    block = ''
    code = ''
    for i in range(0, t, dimenshion):
        block = [text[i + j] for j in range(dimenshion)]
        for j in range(dimenshion):
            code += block[key.index(j)]
    return code


def ltr(key, text):
    dimenshion = len(key)
    t = len(text)
    if t % dimenshion != 0:
        for i in range(dimenshion - (t % dimenshion)):
            text += str('#')
    print(shifrovanie(key, text))


def smn(key, text):
    dimenshion = len(key)
    quantity = int(input("Кол-во символов в группе "))
    txt = [text[i:i + quantity] for i in range(0, len(text), quantity)]
    if len(txt[-1]) != quantity:
        for i in range(quantity - (len(txt[-1]) % quantity)):
            txt[-1] += str("#")
    if len(txt) != dimenshion:
        for i in range(dimenshion - (len(txt) % dimenshion)):
            txt.append("#" * quantity)
    print(shifrovanie(key, txt))


def word(key, text):
    dimenshion = len(key)
    txt = text.split(" ")
    if len(txt) != dimenshion:
        for i in range(dimenshion - (len(txt) % dimenshion)):
            txt.append("#" * 5)
    t = len(txt)
    block = ''
    code = ''
    for i in range(0, t, dimenshion):
        block = [txt[i + j] for j in range(dimenshion)]
        for j in range(dimenshion):
            code += block[key.index(j)]
            code += " "
    print(code)


def interface():
    text = input("Введите предложение ")
    key = input("Введите ключ ")
    key_split = key.split()
    key_list = []
    for e in key_split:
        key_list.append(int(e))
    type = int(input("Способ шифровки: 1 - посимвольное шифрование  2 - шифрование группы  3 - шифрование слов"))
    if type == 1:
        ltr(key_list, text)
    if type == 2:
        smn(key_list, text)
    if type == 3:
        word(key_list, text)


def rasshifr(key, text):
    dimenshion = len(key)
    t = len(text)
    block = ''
    code = ''
    for i in range(0, t, dimenshion):
        block = [text[i + j] for j in range(dimenshion)]
        for j in range(dimenshion):
            code += block[key.index(j)]
    code = code.replace("#", "")
    return code


def rasltr(key, text):
    for i in range(len(key) // 2):
        key[i], key[-i - 1] = key[-i - 1], key[i]
    print(rasshifr(key, text))


def rassmn(key, text):
    quantity = int(input("Сколько символов в группе "))
    txt = [text[i:i + quantity] for i in range(0, len(text), quantity)]
    for i in range(len(key) // 2):
        key[i], key[-i - 1] = key[-i - 1], key[i]
    print(rasshifr(key,txt))


def rasword(key, text):
    txt = text.split()
    for i in range(len(key) // 2):
        key[i], key[-i - 1] = key[-i - 1], key[i]
    dimanshion = len(key)
    n = len(txt)
    block = ''
    code = ''
    for i in range(0, n, dimanshion):
        block = [txt[i + j] for j in range(dimanshion)]
        for j in range(dimanshion):
            code += block[key.index(j)]
            code += " "
    code = code.replace("#", "")
    print(code)


def interface_2():
    text = input("Введите предложение ")
    key = input("Введите ключ ")
    key_split = key.split()
    key_list = []
    for e in key_split:
        key_list.append(int(e))
    type = int(input("Способ шифровки: 1 - посимвольное шифрование  2 - шифрование группы  3 - шифрование слов"))
    if type == 1:
        rasltr(key_list, text)
    if type == 2:
        rassmn(key_list, text)
    if type == 3:
        rasword(key_list, text)


def begin():
    point = int(input("Выберите действие: 1 - зашировать 2 - расшифровать "))
    if point == 1:
        interface()
    else:
        interface_2()

begin()
text = 0
