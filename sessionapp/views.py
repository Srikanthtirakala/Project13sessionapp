from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def input(request):
    return render(request,template_name="base.html")
def mul(request):
    x=int(request.POST['t1'])
    y=int(request.POST['t2'])
    z=x*y
    request.session['z']=z
    request.session.set_expiry(50)
    return HttpResponse('data submitted successfully')
def display(request):
    if request.session.has_key('z'):
        z=request.session['z']
        return HttpResponse("the sum is:"+str(z))
    else:
        return render(request,template_name="base.html")