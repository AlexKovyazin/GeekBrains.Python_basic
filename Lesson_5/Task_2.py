with open('t1_file.txt', encoding='utf-8') as t1:
    print('Количеств строк в файле -', len(t1.readlines()) + 1)
    t1.seek(0)

    line_cnt = 1
    for word in t1.readlines():
        print(f'В строке № {line_cnt} - {len(word.split())} слов')
        line_cnt += 1
    print(f'В строке № {line_cnt} - нет слов')
