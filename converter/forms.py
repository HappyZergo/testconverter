import re

from django import forms
from django.core.exceptions import ValidationError


class ConverterForm(forms.Form):
    number = forms.CharField(max_length=15)  # input поле для введения числа
    number.widget.attrs.update({'class': 'form-control mb-1 col-md-4', 'id': 'convetrible_number'})

    def clean_number(self):  # орпеделение правильности введенных данных
        number = self.cleaned_data['number']  # берем number

        number_identical = re.compile(r'^.*(.)(\1)(\1)(\1).*$')
        if not number.isdigit() and not re.findall(r'[IVXLCDM]',
                                                   number.upper()):  # если строка не является числом и в ней отстутствуют буквы "IVXLCDM"
            raise ValidationError('use symbols "IVXLCDM"')  # ыводим ошибку
        elif not number.isdigit() and number_identical.match(
                number):  # проверка на количество одинаковых символов(должно быть меньше 3)
            raise ValidationError('wrong number')  # выводим ошибку
        elif number.isdigit() and int(number) > 4000:  # если число больше 3999
            raise ValidationError('use numbers < 4000')  # выводим ошибку
        return number  # передаем только правильную строку
