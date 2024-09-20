from django.shortcuts import render

def index(request):
    data = {
        'title': "Daraz | Index Page",
    }
    return render(request, 'index.html',data)

def about(request):
    data = {
        'title': "Daraz | About Page",
    }
    return render(request, 'about.html',data)

def contact(request):
    data = {
        'title': "Daraz | Contact Page",
    }
    return render(request, 'contact.html',data)

def categories(request):
    data = {
        'title': "Daraz | Categories Page",
    }
    return render(request, 'categories.html',data)
