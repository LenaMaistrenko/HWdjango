from django.shortcuts import render

# Create your views here.
# weekday/views.py

from django.shortcuts import render
from datetime import datetime


def weekday(request):

    current_day = datetime.now().weekday()

    days_of_week = [
        'Понеділок', 'Вівторок', 'Середа', 'Четвер', 'П’ятниця', 'Субота', 'Неділя'
    ]

    background_colors = [
        '#FFDDC1',
        '#FFABAB',
        '#FFC3A0',
        '#FF6F61',
        '#D4E157',
        '#7C4DFF',
        '#3D5AFE'
    ]

    day_name = days_of_week[current_day]
    background_color = background_colors[current_day]

    return render(request, 'weekday.html', {'day_name': day_name, 'background_color': background_color})
