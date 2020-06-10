from django.shortcuts import render
from django.http import HttpResponse


news = [
    {
      'title': 'д. Ларневск Красногорского района Брянской области',
      'text': 'Деревня Ларневск расположена в северо-западной части Красногорского района Брянской области.',
      'date': '08.06.2020',
      'autor':'Georgiy'
    },
{
      'title': 'Удалённость ',
      'text': 'Удаленность от районного центра Красная Гора составляет 21 км, от железной дороги города Клинцы – 90 км.',
      'date': '09.06.2020',
      'autor':''
    },
{
      'title': 'Жители ',
      'text': 'Старожилы Ларневска (по ИВ)-Белозор, Глазун, Реук, Рубан, Смоляк, Тикун, Удод, Хламов, Храмко, Чиграй',
      'date': '09.06.2020',
      'autor':''
    }

]
def home(request):
    data ={
        'news': news,
        'title':'Главная страница блога'
    }
    return render(request,'blog/home.html',data)

def contacts(request):
    return render(request,'blog/contacts.html',{'title':'Page about Us'})