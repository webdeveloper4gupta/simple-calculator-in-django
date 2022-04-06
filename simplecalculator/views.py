from django.shortcuts import render



def aman(request):
    ans=0
    data={}
    try:
        n1=int(request.POST.get('num1'))
        n2=int(request.POST.get('num2'))
        n3=(request.POST.get("opr"))
        if n3=='+':
            ans=n1+n2
        elif n3=='-':
            ans=n1-n2
        elif n3=='*':
            ans=n1*n2
        else:
            ans=n1/n2
        data={
            'n1':n1,
            'n2':n2,
            'result':ans
        }

    except:
        pass

 

    return render(request,"index.html",data)