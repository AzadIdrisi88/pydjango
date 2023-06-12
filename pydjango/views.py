from django.shortcuts import render, HttpResponse, redirect


def star(request):
    return HttpResponse("Hello")


def home(request):
    n1 = 0
    n2 = 0
    result = 0
    if request.GET:
        print("Get")
        n1 = int(request.GET["a"])
        print(n1)
        n2 = int(request.GET["b"])
        print(n2)
        cmd=request.GET["cmd"]
        if cmd=="Add":
            result = n1+n2
        if cmd=="Sub":
            result=n1-n2
        if cmd=="Mul":
            result=n1*n2
        if cmd=="Div":
            result=n1//n2

    return render(request, "home.html", {"a": n1, "b": n2, "result": result})


def radio(request):
    n1 = 0
    n2 = 0
    result = 0
    if request.GET:
        print("Get")
        n1 = int(request.GET["a"])
        print(n1)
        n2 = int(request.GET["b"])
        print(n2)
        cmd=request.GET["cmd"]
        if cmd=="Add":
            result = n1+n2
        if cmd=="Sub":
            result=n1-n2
        if cmd=="Mul":
            result=n1*n2
        if cmd=="Div":
            result=n1//n2

    return render(request, "radio.html", {"a": n1, "b": n2, "result": result})


def slct(request):
    n1 = 0
    n2 = 0
    result = 0
    if request.GET:
        print("Get")
        n1 = int(request.GET["a"])
        print(n1)
        n2 = int(request.GET["b"])
        print(n2)
        cmd=request.GET["cmd"]
        if cmd=="Add":
            result = n1+n2
        if cmd=="Sub":
            result=n1-n2
        if cmd=="Mul":
            result=n1*n2
        if cmd=="Div":
            result=n1/n2

    return render(request, "slct.html", {"a": n1, "b": n2, "result": result})


