from django.shortcuts import render, redirect
from django.contrib import messages #import messages
from django.core.mail import send_mail

# Create your views here.
def main(request):
    if request.method == 'POST':
        email = request.POST['email']
        number = request.POST['number']
        name = request.POST['name']
        catagory = request.POST['catagory']
        try:
            send_mail(
                'Booking a slot',
                'email -- > ' + email + '\n\n' + 'mobile number --> ' + number + '\n\n' +'name --> ' + name + '\n\n' + 'catagory--> '+catagory,
                'khannaharshit064@gmail.com',
                [ 'kumarshalu18831@gmail.com','khannaharshit1064@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, 'Thank you !! we will contact you soon')

        except:
            messages.error(request, 'Some error occured !!')
        return redirect('/')
    return render(request, 'app/index.html')
def about(request):
    return render(request, 'app/about.html')
def contact(request):
    if request.method == 'POST':
        email = request.POST['email']
        number = request.POST['number']
        textarea = request.POST['textarea']
        try:
            send_mail(
                'Contact Us',
                'email -- > ' + email + '\n\n'+'mobile number --> ' + number + '\n\n'+ 'textarea --> ' + textarea,
                'khannaharshit064@gmail.com',
                ['kumarshalu18831@gmail.com', 'khannaharshit1064@gmail.com'],
                fail_silently=False,
            )

            messages.success(request, 'We get your query, we will contact you soon !!')
        except:
            messages.error(request, 'Some error occured !!')
        return redirect('/')
    else:
        return render(request, 'app/contact.html')

