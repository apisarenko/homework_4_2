import json
import os
from Phone_Book.classes.contact import Contact


class PhoneBook:
    def __init__(self, name_phonebook):
        self.name_phonebook = name_phonebook

    def new_contact_data(self):
        name = input('Введите имя: ')
        surname = input('Введите фамилию: ')
        phone = input('Введите Номер телефона: ')
        favorite = input('Введите 1 - если избранный контакт, и 0 - если обычный  ')
        key = ''
        list_key_kwargs = []
        list_value_kwargs = []
        while key != 'q':
            in_key = input('Введите наименование дополнительных данных: ')
            in_value = input('Введите значение дополнительных данных: ')
            list_key_kwargs.append(in_key)
            list_value_kwargs.append(in_value)
            key = input('Введите q чтобы закончить ввод дополнительных данных'
                        'или любую букву чтобы продолжить: ')
        list_kwargs = dict(zip(list_key_kwargs, list_value_kwargs))
        key = ''
        list_args = []
        while key != 'q':
            in_value = input('Введите любую дополнительную информацию: ')
            list_args.append(in_value)
            key = input('Введите q чтобы закончить ввод дополнительной информации: ')
        print([name, surname, phone, favorite, list_args, list_kwargs])
        return [name, surname, phone, favorite, list_args, list_kwargs]

    def write_contact_file(self, contact):
        output_data = {'Имя': contact.name,
                       'Фамилия': contact.surname,
                       'Телефон': contact.phone,
                       'В избранных': contact.favorite,
                       'Дополнительная информация': contact.args,
                       'Дополнительная информация 2': contact.kwargs}
        file_name = self.name_phonebook
        if os.path.isfile(file_name):
            with open(file_name, 'ab+') as outfile:
                outfile.seek(-1, os.SEEK_END)
                outfile.truncate()
                outfile.write(','.encode())
                outfile.write(json.dumps(output_data).encode())
                outfile.write(']'.encode())
        else:
            with open(file_name, 'w') as outfile:
                buf_list = []
                buf_list.append(output_data)
                json.dump(buf_list, outfile)

    def output_contacts(self):
        file_name = self.name_phonebook
        with open(file_name, 'r', encoding='utf8') as file:
            data_print = json.load(file)
            for contact in data_print:
                print(Contact(contact['Имя'], contact['Фамилия'], contact['Телефон'],
                              contact['В избранных'], *contact['Дополнительная информация'],
                              **contact['Дополнительная информация 2']))

    def contact_removal(self):
        file_name = self.name_phonebook
        number_delite = input('Введите номер телефона контакт которого Вы хотите удалить: ')
        with open(file_name, 'r', encoding='utf8') as file:
            data = json.load(file)
            i = 0
            for contact in data:
                if contact['Телефон'] == number_delite:
                    data.pop(i)
                i += 1
        with open(file_name, 'w', encoding='utf8') as file:
            json.dump(data, file, ensure_ascii=False)
            return data

    def search_favorite_numbers(self):
        file_name = self.name_phonebook
        with open(file_name, 'r', encoding='utf8') as file:
            data = json.load(file)
            i = 0
            for contact in data:
                if contact['В избранных'] == '1':
                    print(Contact(contact['Имя'], contact['Фамилия'], contact['Телефон'],
                              contact['В избранных'], *contact['Дополнительная информация'],
                                  **contact['Дополнительная информация 2']))
                i += 1

    def cearch_by_name(self):
        file_name = self.name_phonebook
        in_name = input('Введите имя: ')
        in_surname = input('Введите фамилию: ')
        with open(file_name, 'r', encoding='utf8') as file:
            data = json.load(file)
            i = 0
            for contact in data:
                if (contact['Имя'] == in_name) and (contact['Фамилия'] == in_surname):
                    print(Contact(contact['Имя'], contact['Фамилия'], contact['Телефон'],
                              contact['В избранных'], *contact['Дополнительная информация'],
                                  **contact['Дополнительная информация 2']))
                i += 1
