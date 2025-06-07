from django.urls import path

from quoteApp import views

urlpatterns = [
    path("viewQuotes/", views.viewQuotes, name="view_quotes"),
    path("addQuote/", views.addQuote, name="add_quote"),
    path("", views.home, name="home"),
    path("success/", views.addSuccess, name="quote_success"),
    path("give/", views.quote),
]
