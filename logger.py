from data_create import name_data, surname_data, phone_data, address_data 

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные?\n\n"
    f"1 Вариант:\n"         
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 Вариант:\n"
    f"{name}; {surname}; {phone}; {address}\n"
    f"Выберите вариант: "))

    while var !=1 and var !=2:
        print('Неправильный ввод')
        var = int(input('Выберите из двух вариантов '))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"\n{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"\n{name}; {surname}; {phone}; {address}\n\n")


def print_data():
    print('Вывожу данные из 1-го варианта: \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first)-1:
                data_first_list.append("".join(data_first[j:i+1]))
                j=i
        print(''.join(data_first_list))    

    print('Вывожу данные из 2-го варианта: \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second)





def change_data():
    var = int(input(f"В каком варианте вы хотите изменить данные?\n\n"
    f"Выберите 1-ый или 2-ой вариант: "))

    while var !=1 and var !=2:
        print('Неправильный ввод')
        var = int(input('Выберите из двух вариантов '))

    if var == 1:
        with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            data_first = f.readlines()
        print(*data_first)

        line_number=int(input("Введите номер строки, которую хотите изменить: "))
        while line_number < 1 or line_number > len(data_first):
            print("Неверный номер строки")
            line_number=int(input("Введите номер строки, которую хотите изменить: "))

        new_data_first=input("Введите новые данные")

        data_first[line_number-1] = new_data_first + " \n"

        with open("data_first_variant.csv", 'w', encoding='utf-8') as f:
            f.writelines(data_first)
        print ("Изменения сохранены")

    elif var == 2:
        with open("data_second_variant.csv", 'r', encoding='utf-8') as f:
            data_second = f.readlines()            
        print(*data_second)

        line_number = int(input("Введите номер строки, которую хотите изменить: "))
        while line_number < 1 or line_number > len(data_second):
            print("Неверный номер строки")
            line_number = int(input("Введите номер строки, которую хотите изменить: "))

        new_data_second = ("\n{name}; {surname}; {phone}; {address}\n\n")

        data_second[line_number-1] = new_data_second + "\n"

        with open("data_second_variant.csv", 'w', encoding='utf-8') as f:
            f.writelines(data_second)
        print ("Изменения сохранены")