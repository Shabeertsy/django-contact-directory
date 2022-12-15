from django.shortcuts import render,redirect

from .models import contact


# Create your views here.
def index(request):
    contact_data=contact.objects.all()
    return render(request,'index.html',{'data':contact_data})

# data add  model
def add_data(request):

    if request.method=='POST':
        name=request.POST['name']
        address=request.POST['address']
        phone=request.POST['phone']
        data=contact(name=name,address=address,phone=phone)
        data.save()

        contact_data=contact.objects.all()
        return render(request,'index.html',{'data':contact_data})
    else:
        return render(request,'index.html')


#delete function        
def delete(request,del_id):
    delete=contact.objects.get(id=del_id)
    delete.delete()
    return redirect('index')


#update function
def form_update(request,id):
    if request.method=='POST':
        add=contact.objects.get(id=id)
        add.name=request.POST['name']
        add.address=request.POST['address']
        add.phone=request.POST['phone']
        add.save()
        return redirect('index')


#edit function
def edit(request,id):
    user_data=contact.objects.get(id=id)
    return render(request,'edit.html',{"data":user_data})


