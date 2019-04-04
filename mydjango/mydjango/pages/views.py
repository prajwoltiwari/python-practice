from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    # return HttpResponse('<h1>This my custom homepage view</h1>')
    return render(request, 'home.html', {})

def contact_view(request, *args, **kwargs):
    my_contacts = {
        'PJ': 9860832382,
        'Shekhar_dai': 'did not have a number',
        'Aashish_dai': 'easy to remember number',
        'Your_List': [123, 'a', 'b', 5656, 'fg56', 'Prajwol did this!!!']
    }
    # return HttpResponse('<h1>This is the contact page!!!</h1>')
    return render(request, 'contact.html', my_contacts)

def social_view(*args, **kwargs):
    return HttpResponse('<h1>My social media</h1><h2>prajwoltiwari</h2><h3>Gmail: prajwol.pt@gmail.com</h3>')

