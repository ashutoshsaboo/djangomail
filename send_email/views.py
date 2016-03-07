from django.shortcuts import render
from django.http import HttpResponse
import django
from django.conf import settings
from django.core.mail import send_mail


def index(request):
    return render(request, 'index.html')


def success(request):
    email = request.POST.get('email', '')
    data = """
Mail.
    """
    send_mail('Welcome!', data, "ABC",
              [email], fail_silently=False)
    return render(request, 'success.html')
