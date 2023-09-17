from django.shortcuts import render
from .forms import MyCustomUserForm
from django.contrib import messages
# Create your views here.
######################
def show_index(request):
    if request.method == 'POST':
        fm=MyCustomUserForm(request.POST, label_suffix=' ')
        
        if fm.is_valid():
           fm.save() 
           print(fm)
        fm=MyCustomUserForm()   
    else:
     fm=MyCustomUserForm()
    return render(request, 'myapp/index.html',{'form':fm})


def show_blog(request):
    return render(request, 'myapp/blog.html')

def show_about(request):
    return render(request, 'myapp/about.html')

def show_contact(request):
    if request.method == 'POST':
        fm=MyCustomUserForm(request.POST)
        if fm.is_valid():
           messages.success(request,'Your Form have been Submit Successfully!!')
           fm.save() 
        fm=MyCustomUserForm()   
    else:
     fm=MyCustomUserForm(label_suffix='')
    return render(request, 'myapp/contact.html',{'form':fm})

 

def show_single(request):
    return render(request, 'myapp/single.html')


