from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (ListView, UpdateView, TemplateView, CreateView, DeleteView)

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



# class ListSportsBetAccounts(LoginRequiredMixin, ListView):
#     """
#     Lists all the bet account information
#     """
#
#     model = SportsBetAccounts
#     template_name = 'sportsbet/sportsbets_list.html'
