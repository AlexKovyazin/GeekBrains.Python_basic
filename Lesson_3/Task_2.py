def personal_data(name, surname, city, email, phone_num):
    """Возвращает словарь с аргументами из args"""
    personal_data_dict = {'name': name, 'surname': surname, 'city': city, 'email': email, 'phone number': phone_num}
    return personal_data_dict


my_name = 'Alex'
my_surname = 'Kovyazin'
my_city = 'Moscow'
my_email = 'blablabla@gmail.com'
my_phone_nun = '+79181234567'

for key, value in personal_data(name=my_name, city=my_city, surname=my_surname, email=my_email,
                                phone_num=my_phone_nun).items():
    print(f'{key} - {value}, ', end='')
