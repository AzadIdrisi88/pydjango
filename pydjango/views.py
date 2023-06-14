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


def chck(request):
    n1 = 0
    n2 = 0
    result = 0
    if request.GET:
        print("Get")
        n1 = int(request.GET["a"])
        print(n1)
        n2 = int(request.GET["b"])
        print(n2)
        value="checked"
        try:
            cmd=request.GET["cmd"]
        except:
            value=""
            cmd="Sub"
        if cmd=="Add":
            result = n1+n2
        if cmd=="Sub":
            result=n1-n2

        value="checked"
        try:
            cmd=request.GET["cmd"]
        except:
            value=""
            cmd="Div"
        if cmd=="Mul":
            result=n1*n2
        if cmd=="Div":
            result=n1/n2

    return render(request, "chck.html", {"a": n1, "b": n2, "result": result,"value":value})


def marksheet(request):
    p=0
    c=0
    m=0
    total=0
    percent=0
    result=""
    Div=""
    
    if request.GET:
        print("get")
        p=int(request.GET["a"])
        print(p)
        c=int(request.GET["b"])
        print(c)
        m=int(request.GET["c"])
        print(m)

        total=p+c+m
        percent=total/3
        print(total)
        print(percent)
        if p<35 or c<35 or m<35:
            result="fail"
        else:
            result="Pass"
            print("fail")
            

        if percent<55:
            Div="3rd Division"
            print("3rd Division")
        elif percent<65:
            Div="2nd Division"
            print("2nd Division")
        else:
            Div="1st Division"
            print("1st Division")
    return render(request,"marksheet.html",{"a":p,"b":c,"c":m,"t":total,"percent":percent,"r":result,"d":Div})


    

     
