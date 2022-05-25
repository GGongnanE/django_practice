from django.shortcuts import render

# Create your views here.
def indexA(request):
    return render(request, 'indexA.html')