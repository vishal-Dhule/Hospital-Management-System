from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from .models import Appointment
from .models import EmergencyRequest

from .forms import BillingQueryForm


def index(request):
    return render(request, "home/index.html")


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")


def contact(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        department = request.POST.get("department")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            department=department,
            subject=subject,
            message=message
        )

        messages.success(
            request,
            "Your message has been sent successfully!"
        )

        return redirect("contact")


    return render(request, "contact.html")


def doctor(request):
    return render(request, "doctor.html")





def appointment(request):

    if request.method == "POST":

        Appointment.objects.create(

            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            age=request.POST.get("age"),
            gender=request.POST.get("gender"),
            department=request.POST.get("department"),
            appointment_date=request.POST.get("date"),
            appointment_time=request.POST.get("time"),
            symptoms=request.POST.get("symptoms"),

        )

        messages.success(
            request,
            "Appointment booked successfully!"
        )

        return redirect("appointment")

    return render(request, "appointment.html")


def advanced_surgery(request):
    return render(request, "advanced_surgery.html")



def diagnostic_services(request):
    return render(request, "diagnostic_services.html")



def pharmacy(request):
    return render(request, "pharmacy.html")


# views.py
def patient_care(request):
    return render(request, "patient_care.html")


def billing(request):
    return render(request, "billing.html")

def faq(request):
    return render(request, "faq.html")

def blog(request):
    return render(request, "blog.html")

def news(request):
    return render(request, "news.html")

def testimonials(request):
    return render(request, "testimonials.html")

def gallery(request):
    return render(request, "gallery.html")




def emergency(request):

    if request.method == "POST":

        name = request.POST.get('name')
        phone = request.POST.get('phone')
        location = request.POST.get('location')
        emergency_details = request.POST.get('emergency_details')


        EmergencyRequest.objects.create(
            name=name,
            phone=phone,
            location=location,
            emergency_details=emergency_details
        )


        messages.success(
            request,
            "Emergency request submitted successfully. Our team will contact you."
        )


    return render(request, 'emergency.html')

def location(request):
    return render(request, "location.html")

def privacy(request):
    return render(request, "privacy.html")

def terms(request):
    return render(request, "terms.html")

def billing_support(request):

    if request.method == "POST":
        form = BillingQueryForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Your billing request has been submitted successfully. Our team will contact you shortly."
            )

            return redirect("billing_support")

    else:
        form = BillingQueryForm()

    return render(request, "billing_support.html", {"form": form})