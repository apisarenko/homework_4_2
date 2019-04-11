from Phone_Book.classes.contact import Contact
from Phone_Book.classes.phonebook import PhoneBook


def main():
    phone_book = PhoneBook('phone_book.json')
    command = input('Введите команду: ' + '\n' +
                   '1 - вывод контактов из телефонной книги' + '\n' +
                   '2 - добавить новый контакт' + '\n' +
                   '3 - удалить контакт по номру телефона' + '\n' +
                   '4 - поиск всех избранных номеров' + '\n' +
                   '5 - поиск контакта по имени и фамилии' + '\n' + ': ')
    if command == '1':
        phone_book.output_contacts()
    elif command == '2':
        contact_info = phone_book.new_contact_data()
        new_contact = Contact(contact_info[0], contact_info[1], contact_info[2],
                              contact_info[3], *contact_info[4], **contact_info[5])
        phone_book.write_contact_file(new_contact)
        print(new_contact)
    elif command == '3':
        phone_book.contact_removal()
    elif command == '4':
        phone_book.search_favorite_numbers()
    elif command == '5':
        phone_book.cearch_by_name()


if __name__ == "__main__":

    main()
