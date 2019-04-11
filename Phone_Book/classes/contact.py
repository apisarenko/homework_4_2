import json

class Contact:
    def __init__(self, name, surname, phone, favorite=False, *args, **kwargs):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.favorite = favorite
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        if str(self.favorite) == 'False':
            str_favorite = 'Нет'
        else:
            str_favorite = 'Да'
        out_str_args = ''
        out_str_kwargs = ''
        for value in self.args:
            out_str_args = '\t' + out_str_args + value
        for key, value in self.kwargs.items():
            out_str_kwargs = out_str_kwargs + '\t' + key + ': ' + value + '\n'
        return ('Имя: ' + self.name + '\n' +
                'Фамилия: ' + self.surname + '\n' +
                'Телефон: ' + self.phone + '\n' +
                'В избранных: ' + str_favorite + '\n' +
                'Дополнительная информация: ' + '\n' +
                out_str_kwargs + out_str_args
                )

