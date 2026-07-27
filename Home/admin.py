from django.contrib import admin
from .models import Contact
from .models import Appointment
from .models import BillingQuery
from .models import EmergencyRequest

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "phone",
        "department",
        "subject",
        "created_at",
    )
    search_fields = ("name", "email", "phone")
    list_filter = ("department", "created_at")


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "department",
        "appointment_date",
        "appointment_time",
        "phone",
    )

    search_fields = (
        "name",
        "phone",
        "email",
    )

    list_filter = (
        "department",
        "appointment_date",
    )

@admin.register(BillingQuery)
class BillingQueryAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "email",
        "phone",
        "issue",
        "created_at",
    )

    search_fields = (
        "full_name",
        "email",
        "phone",
    )

    list_filter = (
        "issue",
        "created_at",
    )


@admin.register(EmergencyRequest)
class EmergencyRequestAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'phone',
        'location',
        'created_at'
    )

    search_fields = (
        'name',
        'phone'
    )