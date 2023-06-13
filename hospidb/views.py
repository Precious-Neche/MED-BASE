from django.shortcuts import render, redirect
from . models import Hospidb
# Create your views here.

def index(request):

    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        age = request.POST['age']
        gender = request.POST['gender']
        description = request.POST['description']

        insert_data = Hospidb(fname = fname, lname = lname, age = age, gender = gender, description = description)
        insert_data.save()
        
        return redirect('index')

    return render(request, 'hospidb/index.html')

def detail(request, ):
    get_data = Hospidb.objects.all().order_by('created_at')
    context = {
        'patients': get_data
    }
    return render(request, 'hospidb/detail.html',context)

def delete(request, id):
    get_data = Hospidb.objects.get(id = id)
    context = {
        'patients': get_data
    }

    if request.method == 'POST':
        get_data.delete()
        return redirect('detail')

    return render(request, 'hospidb/delete.html',context)

def edit(request, id):
    get_data = Hospidb.objects.get(id = id)
    context = {
        'patients': get_data
    }

    if request.method == 'POST':
        get_data.fname = request.POST['fname']
        get_data.lname = request.POST['lname']
        get_data.age = request.POST['age']
        get_data.gender = request.POST['gender']
        get_data.description = request.POST['description']

        get_data.save()
        return redirect('detail')
    return render(request, 'hospidb/edit.html',context)
