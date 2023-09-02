from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def contact(request):
    return HttpResponse(
        """
                        <h1>This is Contact Us Page</h1>
                        <a href='/first/about/'>Go to About</a>
                        """
    )


def about(request):
    return HttpResponse(
        """
                        <h1>This is About Us Page</h1>
                        <a href='/first/contact/'>Go to Contact Us</a>
                        """
    )


def home(request):
    return render(request, "index.html")
