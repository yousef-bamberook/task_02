from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        "asd": "Hello Worlds"}
    return render(request, 'hello.html', context)
