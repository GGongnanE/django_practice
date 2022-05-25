from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Board

# Create your views here.
def index(request):
    print("request :", request)
    print("request2 :", dir(request), type(request))
    print('=========================================')
    print("request POST value :", request.POST)
    print("request GET value :", request.GET)
    return render(request, 'index.html')

def test(request):
    # return render(request, 'test.html')
    # return redirect('/')
    # return HttpResponse('Hello world')
    dictionary = {"mickey":123}
    return JsonResponse(dictionary)

def sample(request):
    dic = {"mickey": '밐키'}
    l = [100, 200, 300]
    return render(request, 'sample.html', {'value': l, 'value2':dic})

def sample2(request):
    data = Board.objects.all()

    return render(request, 'sample.html', {'board': data})