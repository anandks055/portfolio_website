from django.shortcuts import render
from index.models import Contact

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
     if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        print(name,email,message)
        obj=Contact(name=name,email=email,message=message)
        obj.save()
     return render(request,'contact.html')
def project(request):
   
    return render(request,'project.html')

