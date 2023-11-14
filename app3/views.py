from django.shortcuts import render

# Create your views here.
def sis(request):
    return render(request,'sis.html')
def mom(request):
    return render(request,'mom.html')
def dad(request):
    return render(request,'dad.html')
def aunt(request):
    return render(request,'aunt.html')