from django.shortcuts import render
from .forms import ContactForm

def contactFunction(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "datasent.html", {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'write_here': form.cleaned_data['write_here']
            })
    else:
        form = ContactForm()
    return render(request, "datasent.html", {'form': form})

def indexfunction(request):
    return render(request, "index.html")

def conNavFunction(request):
    return render(request, "contact.html")

def backFunction(request):
    return render(request, "index.html")



# Create your views here.
