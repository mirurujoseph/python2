from django.shortcuts import render, redirect
from .models import Contact


# Create your views here.
def index(request):
    return render(request,'index.html')
def blog(request):
    return render(request,'blog.html')
def about(request):
    return render(request,'blog-single.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        query=Contact.objects.create(name=name,email=email,subject=subject,message=message)
        query.save()
        return redirect('/')