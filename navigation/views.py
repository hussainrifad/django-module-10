from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    contact = {
        'branch' : 'London',
        'contact_list' : [
            '121331',
            '121332',
            '321331'
        ]
    }
    return render(request, 'contact.html', contact)