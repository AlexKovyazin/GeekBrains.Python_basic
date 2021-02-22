def int_func(text):
    return text.title()


def int_func_2(text):
    text_list = text.split()
    result = []
    for i in text_list:
        result.append(int_func(i))
    return ' '.join(result)


print(int_func_2('aPPle text Hi 54'))
