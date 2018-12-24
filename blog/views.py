from django.shortcuts import render, HttpResponse
import time


# Create your views here.
def show_time(request):
    t = time.ctime()
    return render(request, "index.html", locals())
    # return render(request, "index.html", {"t": t})
