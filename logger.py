from data_create import name_data, surname_data, phone_data, address_data 

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные?\n\n"
    f"1 Вариант:\n"         
    f"{name}\n {surname}\n {phone}\n {address}\n\n"
    f"2 Вариант:\n"
    f"{name}; {surname}; {phone}; {address}\n"
    f"Выберите вариан: "))


def print_data():
    pass