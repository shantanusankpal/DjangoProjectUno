from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from quoteApp.forms import QuoteAddForm
from quoteApp.models import Quote


def quote(request):
    return HttpResponse("This is a sample quote.")


def update_quote(request, pk):
    quote = get_object_or_404(Quote, pk=pk)
    if request.method == "POST":
        form = QuoteAddForm(request.POST, instance=quote)
        if form.is_valid():
            form.save()
            return redirect("view_quotes")  # change as per your view name
    else:
        form = QuoteAddForm(instance=quote)
    return render(request, "quoteApp/quoteInput.html", {"form": form})


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


def delete_quote(request):
    if request.method == "POST":
        ids = request.POST.getlist("quote_ids")
        Quote.objects.filter(id__in=ids).delete()
    return redirect("view_quotes")
