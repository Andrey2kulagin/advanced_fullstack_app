from django.shortcuts import render
from .forms import CandidateForm
from django.http import HttpResponseRedirect
from django.contrib import messages


def home(request):
    context = {}
    form = CandidateForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Register is successfully")
        return HttpResponseRedirect('/')
    context["form"] = form
    return render(request, "home.html", context)
