from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "index.html")

def services(request):
    return render(request, "services.html")

def gallery(request):
    return render(request, "gallery.html")

def contact(request):
    return render(request, "contact.html")

def appointment(request):
    return render(request, "appointment.html")