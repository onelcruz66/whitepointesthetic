from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path("", views.home, name="home"),
    path("services/", views.services, name="services"),
    path("gallery/", views.gallery, name="gallery"),
    path("contact/", views.contact, name="contact"),
    path("appointment/", views.appointment, name="appointment"),
    path("admin-dashboard/", views.dashboard, name="dashboard"),
    path("pending-appointments/", views.pending, name="pending"),
    path("approved-appointments/", views.approved, name="approved"),
    path('delete_appointment/<int:appointment_id>/', views.delete_appointment, name="delete_appointment"),
    path('accept_appointment/<int:appointment_id>/', views.accept_appointment, name="accept_appointment"),
    path('delete_approved_appointment/<int:appointment_id>/', views.delete_approved_appointment, name="delete_approved_appointment"),
    path('delete_message/<int:message_id>/', views.delete_message, name="delete_message"),
    path('register/', views.register, name='register'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', views.logout, name='logout'),
]