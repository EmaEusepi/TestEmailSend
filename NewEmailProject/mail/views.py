from django.shortcuts import render
from django.core.mail import EmailMessage, get_connection
from django.conf import settings

#email test:

def send_email(request):  
   if request.method == "POST": 
       with get_connection(  
           host=settings.EMAIL_HOST, 
     port=settings.EMAIL_PORT,  
     username=settings.EMAIL_HOST_USER, 
     password=settings.EMAIL_HOST_PASSWORD, 
     use_tls=settings.EMAIL_USE_TLS  
       ) as connection:  
           subject = "WARNING: NEW VULNERABILITIES ON YOUR DEVICES" 
           email_from = settings.EMAIL_HOST_USER  
           recipient_list = [request.POST.get("email"), ]  
           vulns = request.POST.get("vulns")
           message = "New vulnerabilities have been detected on your devices:\n\n%s\n\nLog into https://iothreatracker.azurewebsites.net/ with your credentials to obtain more info." %  vulns
           EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()  
 

   return render(request, 'mail/home.html')

