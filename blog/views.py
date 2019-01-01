from django.shortcuts import render, HttpResponse,render_to_response
import time
import datetime

# Create your views here.
def show_time(request):
    t = time.ctime()
    return render(request, "index.html", locals())
    # return render(request, "index.html", {"t": t})


def article(request, year):
    print(request)
    return HttpResponse('2004')


def articles(request, year, month):
    return HttpResponse('year: %s month: %s' % (year, month))


def register(request):
    if request.method == 'post':
        print(request.POST.get('user'))
        print(request.POST.get('age'))
        print(request.POST.get('hobby'))
    # return render(request,'register.html')
    return render_to_response('register.html')

class People():
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex

def query(request):
    t = datetime.datetime.now()
    action = ["春哥","阿毛","小强","大桥未久"]
    dict = {"name":"纯哥","hobby":"小乔","biantai":True}
    p = People("huazai","gong")

    num = 22
    st = 'matrix foo'
    st2 = 'matrix fool'
    l = []
    a = "<a href='www.baidu.com'>click here</a>"
    return render(request,"query.html",locals())