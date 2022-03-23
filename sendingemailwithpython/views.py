from email import message
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
import re

def index(request):
    if request.method == 'POST':
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        valid_email = '^\w+(?:[.\+!%]\w+)*@\w+(?:[.\-]\w+)+$'

        if (re.search(valid_email, email)):
            data = {
                'name': name,
                'email': email,
                'subject': subject,
                'message': message
            }
            message = '''
            New message: {}

            From:{}
            '''.format(data['message'], data['email'])
            send_mail(data['subject'], message, '', 
            ['example@mail.com'])
        else:
            return render(request, 'sendingemailwithpython/invalid.html', {})

    return render(request, 'sendingemailwithpython/index.html', {})