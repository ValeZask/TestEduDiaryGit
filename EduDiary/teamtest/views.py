from django.http import HttpResponse

def welcome(request):
    return HttpResponse("<h1>Добро пожаловать на EduDiary!</h1>")
