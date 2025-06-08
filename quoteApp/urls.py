from django.urls import path

from quoteApp import views

urlpatterns = [
    path("viewQuotes/", views.viewQuotes, name="view_quotes"),
    path("addQuote/<int:pk>", views.update_quote, name="update_quote"),
    path("addQuote/", views.addQuote, name="add_quote"),
    path("", views.home, name="home"),
    path("delete/", views.delete_quote, name="delete_quote"),
    path("success/", views.addSuccess, name="quote_success"),
    path("give/", views.quote),
]
