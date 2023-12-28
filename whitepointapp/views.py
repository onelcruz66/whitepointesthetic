from django.shortcuts import render, redirect
from .models import RequestAppointment, MessageRequest, ApprovedAppointments
from whitepointapp.forms import RequestForm, MessageForm, CreateUserForm, CustomAuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views


# Create your views here.

# Landing page views.
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

# Admin page views.
@login_required
def dashboard(request):
    context = {}
    request_appointment_table = RequestAppointment.objects.all()
    message_request_table = MessageRequest.objects.all()
    approved_appointment_table = ApprovedAppointments.objects.all()
    context['request_appointment_table'] = request_appointment_table
    context['message_request_table'] = message_request_table
    context['approved_appointment_table'] = approved_appointment_table

    return render(request, "dashboard.html", context)

@login_required
def pending(request):
    context = {}
    try:
        pending_appointments = RequestAppointment.objects.all()
        context['pending_appointments'] = pending_appointments
    except Exception as e:
        return f"Error fetching records: {str(e)}"

    return render(request, "pending.html", context)

@login_required
def approved(request):
    context = {}
    try:
        approved_appointments = ApprovedAppointments.objects.all()
        context['approved_appointments'] = approved_appointments
    except Exception as e:
        return f"Error fetching records: {str(e)}"

    return render(request, "approved.html", context)

@login_required
def delete_appointment(request, appointment_id):
    appointment = RequestAppointment.objects.get(pk=appointment_id)
    appointment.delete()
    return redirect('pending')

@login_required
def accept_appointment(request, appointment_id):
    source_record = RequestAppointment.objects.get(pk=appointment_id)

    destination_record = ApprovedAppointments(
            first_name=source_record.first_name,
            last_name=source_record.last_name,
            email_address=source_record.email_address,
            phone_number=source_record.phone_number,
            service=source_record.service,
            date=source_record.date,
            time=source_record.time
        )
    destination_record.save()

    source_record.delete()

    return redirect('pending')

@login_required
def delete_approved_appointment(request, appointment_id):
    appointment = ApprovedAppointments.objects.get(pk=appointment_id)
    appointment.delete()
    return redirect('approved')

@login_required
def delete_message(request, message_id):
    message = MessageRequest.objects.get(pk=message_id)
    message.delete()
    return redirect('dashboard')

@login_required
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form}

    return render(request, 'register.html', context)

def logout(request):
    return redirect('login')

class CustomLoginView(auth_views.LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustomAuthenticationForm
