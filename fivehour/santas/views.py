from django.shortcuts import render
from .models import Destination

'''Product id is set to 1 by default'''
idnumber = 1
def home(request):
    '''The Home function renders the base page which is used in all the other pages
    '''
    '''Request.POST method allows the user to stay on the same page but get different products'''
    if request.method == 'POST':
        global idnumber
        idnumber = request.POST.get('interface')
        obj = Destination.objects.all()
        original = obj.filter(id=int(idnumber))
        context = {'base':obj,'original':original,'idnumber':idnumber}
        return render(request,'sidebar.html',context=context)

    obj = Destination.objects.all()
    original = obj.filter(id=idnumber)
    context = {'base':obj,'original':original,'idnumber':idnumber}
    return render(request,'sidebar.html',context=context)

def Travel(request):
    '''Instead of using javascript the different sections were divided up into pages
    This is for the Travel Guide section'''
    global idnumber
    obj = Destination.objects.all()
    original = obj.filter(id=idnumber)
    context = {'base':obj,'original':original,'idnumber':idnumber}
    return render(request,'sidebar_travel_guide.html',context=context)

def Things(request):
    '''This was an alternative to using javascript same for the one above'''
    global idnumber

    obj = Destination.objects.all()
    original = obj.filter(id=idnumber)
    context = {'base':obj,'original':original,'idnumber':idnumber}
    return render(request,'sidebar_thing_to_do.html',context=context)