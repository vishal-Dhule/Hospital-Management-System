from django.urls import path
from . import views

urlpatterns = [

    path("", views.index, name="home"),

    path("about/", views.about, name="about"),

    path("services/", views.services, name="services"),

    path("contact/", views.contact, name="contact"),

    path("doctor/", views.doctor, name="doctor"),

    path("appointment/", views.appointment, name="appointment"),

    path("advanced-surgery/", views.advanced_surgery, name="advanced_surgery"),

    path("diagnostic-services/", views.diagnostic_services, name="diagnostic_services"),

    path("pharmacy/", views.pharmacy, name="pharmacy"),

    path("patient-care/", views.patient_care, name="patient_care"),

path("billing/", views.billing, name="billing"),
path("faq/", views.faq, name="faq"),
path("blog/", views.blog, name="blog"),
path("news/", views.news, name="news"),
path("testimonials/", views.testimonials, name="testimonials"),
path("gallery/", views.gallery, name="gallery"),
path("emergency/", views.emergency, name="emergency"),
path("location/", views.location, name="location"),
path("privacy/", views.privacy, name="privacy"),
path("terms/", views.terms, name="terms"),

path('billing-support/', views.billing_support, name='billing_support'),

]