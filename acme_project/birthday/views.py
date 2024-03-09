from django.shortcuts import render
from .forms import BirthdayForm
from .utils import calculate_birthday_countdown


def birthday(request):
    form = BirthdayForm(request.GET or None)
    # Создаём словарь контекста сразу после инициализации формы.
    context = {'form': form}
    # Если форма валидна...
    if form.is_valid():
        # ...вызовем функцию подсчёта дней:
        birthday_countdown = calculate_birthday_countdown(
            # ...и передаём в неё дату из словаря cleaned_data.
            form.cleaned_data['birthday']
        )
        # Обновляем словарь контекста: добавляем в него новый элемент.
        context.update({'birthday_countdown': birthday_countdown})
    return render(request, 'birthday/birthday.html', context)
'''
def birthday(request):
    if request.GET:
        form = BirthdayForm(request.GET)
        if form.is_valid():
            pass
    else:
        form = BirthdayForm()
    context = {'form': form}
    return render(request, 'birthday/birthday.html', context)
'''

'''def birthday(request):
    form = BirthdayForm(request.GET or None)
    if form.is_valid():
        pass
    context = {'form': form}
    return render(request, 'birthday/birthday.html', context) 
Этот код гораздо короче, а работает точно так же, как и предыдущий вариант.
Весь фокус в выражении BirthdayForm(request.GET or None). 
Его логика такова: если в GET-запросе были переданы параметры — значит,
объект request.GET не пуст и этот объект передаётся в форму;
если же объект request.GET пуст — срабатывает условиe or и форма создаётся без параметров,
через BirthdayForm(None) — это идентично обычному BirthdayForm().'''
