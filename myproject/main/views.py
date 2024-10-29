from django.shortcuts import render
from .models import btns, imgs

# Create your views here.

def index(request):
    btn = btns.objects.all()[:1]
    img = imgs.objects.last()
    return render(request, 'main/site.html', {'btnonename': btn, 'whichimage': img})