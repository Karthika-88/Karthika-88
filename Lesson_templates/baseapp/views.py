from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'baseapp/index.html')

def relative(request):
    return render(request, 'baseapp/relative_url_template.html')

def other(request):
    return render(request, 'baseapp/other.html')

def base(request):
    return render(request, 'baseapp/base.html')
