from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateLink
from .models import Link

def homePage(request):
    data = {
        'title': 'Главная страница сайта'
    }
    return render(request, 'main/home.html', data)

def aboutPage(request):
    data = {
        'title': 'Страница с информацией'
    }
    return render(request, 'main/about.html', data)

def redirectPage(request, slug):
    # Получение ссылки для переадресации
    link = Link.objects.filter(short_link=slug).first()
    return redirect(link.long_link)

@login_required
def createLinkPage(request):
    if request.method == "POST":
        form = CreateLink(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('links')
    else:
        form = CreateLink()

    # Получение всех ссылок и передача их в шаблон
    links = Link.objects.filter(user=request.user)

    data = {
        'title': 'Создание сокращений',
        'form': form,
        'links': links
    }
    return render(request, 'main/links.html', data)