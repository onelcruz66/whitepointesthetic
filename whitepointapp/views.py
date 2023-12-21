from django.shortcuts import render, HttpResponse, redirect
from .models import RequestAppointment, MessageRequest
from whitepointapp.forms import RequestForm, MessageForm

# Create your views here.
def home(request):
    context = {}

    # Handle form submissions
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path) 
    else:
        # Render the form for GET requests
        form = RequestForm()

    context['form'] = form

    return render(request, "index.html", context)

def services(request):

    context = {}

    # Handle form submissions
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path)  
    else:
        # Render the form for GET requests
        form = RequestForm()

    context['form'] = form

    return render(request, "services.html", context)

def gallery(request):
    return render(request, "gallery.html")

def contact(request):
    context = {}

    # Handle form submissions
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path)  
    else:
        # Render the form for GET requests
        form = MessageForm()

    context['form'] = form
    return render(request, "contact.html", context)

def appointment(request):
    context = {}

    # Handle form submissions
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path)  
    else:
        # Render the form for GET requests
        form = RequestForm()

    context['form'] = form
    return render(request, "appointment.html", context)