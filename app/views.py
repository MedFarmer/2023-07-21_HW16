from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import json
from .models import Student

def profile(request):
    
    if request.user.is_authenticated:
        return HttpResponse('Hello, User')
    else:
        return HttpResponseRedirect(reverse('login'))

def login(request):
    return HttpResponse('This is a login page, please sign in')

def save_text_file(request):
    data = Student.objects.all().values()
    file_path = 'file.json'
    
    data_json = json.dumps(list(data))
    
    with open(file_path, 'w') as file:
        file.write(data_json)
    return HttpResponse('data saved')