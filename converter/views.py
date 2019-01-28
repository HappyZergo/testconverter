import json
import re

from django.shortcuts import render
from django.views import View

from converter.convert import roman_to_arabic, arabic_to_roman
from converter.forms import ConverterForm


class ConverterView(View):

    def get(self, request):  # обработка get запроса, відача пустой формы
        form = ConverterForm()
        return render(request, 'konverter.html', context={'form': form})

    def post(self, request):  # обработка post запроса
        bound_form = ConverterForm(request.POST)
        if bound_form.is_valid():  # если ворма валидна
            some_number = bound_form.clean_number()  # очищеная строка(меньше 4000 и содержащее символы "IVXCDML")
            if some_number.isdigit():  # если в строке только цифры отправляем конвертировать из арабских с римские
                n = json.dumps(arabic_to_roman(some_number))
                n = re.sub('["]', '', n)
                return render(request, 'konverter.html', context={'n': n, 'form': bound_form})
            else:  # если в строке только буквы - конвертация из римких с арабские
                n = json.dumps(roman_to_arabic(some_number.upper()))
                n = re.sub('["]', '', n)
                return render(request, 'konverter.html', context={'n': n, 'form': bound_form})
        else:  # если не валидна
            return render(request, 'konverter.html', context={'form': bound_form})
