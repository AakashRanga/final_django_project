from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,"index.html")
def counter(request):
    text=request.POST['text']
    amount_of_words = len(text.split())
    return render(request,"counter.html",{'amount':amount_of_words})
def sum_of_numbers(request):
    text = request.POST['text']
    str_num = str(text)
    mapobj = map(int, str_num)
    a = list(mapobj)
    ans = 0
    for j in range(0, len(a)):
        ans = ans + a[j]
    return render(request,"sum_of_numbers.html",{'total':ans})

# Create your views here.
