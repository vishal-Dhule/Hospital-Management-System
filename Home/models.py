from django.db import models

class Contact(models.Model):
    DEPARTMENTS = [
        ("General Medicine", "General Medicine"),
        ("Cardiology", "Cardiology"),
        ("Neurology", "Neurology"),
        ("Orthopedics", "Orthopedics"),
        ("Pediatrics", "Pediatrics"),
        ("Emergency", "Emergency"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    department = models.CharField(max_length=100, choices=DEPARTMENTS)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):

    DEPARTMENTS = [
        ("General Medicine", "General Medicine"),
        ("Cardiology", "Cardiology"),
        ("Neurology", "Neurology"),
        ("Orthopedics", "Orthopedics"),
        ("Pediatrics", "Pediatrics"),
        ("Emergency", "Emergency"),
    ]

    GENDER = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    age = models.PositiveIntegerField()

    gender = models.CharField(
        max_length=20,
        choices=GENDER
    )

    department = models.CharField(
        max_length=100,
        choices=DEPARTMENTS
    )

    appointment_date = models.DateField()
    appointment_time = models.TimeField()

    symptoms = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.department}"


class BillingQuery(models.Model):
    ISSUE_CHOICES = [
        ('Invoice Request', 'Invoice Request'),
        ('Insurance Claim', 'Insurance Claim'),
        ('Payment Issue', 'Payment Issue'),
        ('Refund', 'Refund'),
        ('Other', 'Other'),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    issue = models.CharField(max_length=50, choices=ISSUE_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class EmergencyRequest(models.Model):

    name = models.CharField(max_length=100)

    phone = models.CharField(max_length=15)

    location = models.CharField(max_length=200)

    emergency_details = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name