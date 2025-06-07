from django.shortcuts import render, redirect
from django.http import HttpResponse
from quoteApp.forms import QuoteAddForm
from quoteApp.models import Quote


def quote(request):
    return HttpResponse("This is a sample quote.")


def addQuote(request):
    form = QuoteAddForm()
    if request.method == "POST":
        form = QuoteAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("quote_success")
        else:
            form = QuoteAddForm()
    return render(request, "quoteApp/quoteInput.html", {"form": form})


def home(request):
    return render(request, "quoteApp/home.html")


def viewQuotes(request):
    quote = Quote.objects.all()
    return render(request, "quoteApp/view_quotes.html", {"quotes": quote})


def addSuccess(request):
    return render(request, "quoteApp/quote_success.html")


# Create your views here.
