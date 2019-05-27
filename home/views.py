from django.core.mail import send_mail
from django.shortcuts import render


def home(request):
    if request.method == 'GET':
        return render(request, 'home/home.html')
    elif request.method == 'POST':
        message = "We will contact you "
        user_name = request.POST.get('name')
        user_mail = request.POST.get('email')
        user_ph = request.POST.get('phone')
        user_msg = request.POST.get('message')
        to_list = [
            'ravirajclasses@gmail.com'
        ]
        send_mail(subject="Mail by " + user_name, message="", from_email=user_mail, recipient_list=to_list,
                  fail_silently=True,
                  html_message=user_msg + " " + user_ph)
        return render(request, 'home/home.html', {'message': message})
