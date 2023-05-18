from django.shortcuts import render


# Create your views here.
def hello_world(request):
    context = {}
    return render(request, 'main/hello.html', context)


def kontakty(request):
    context = {}
    return render(request, 'main/contacts.html', context)
