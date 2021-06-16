from django.http.response import JsonResponse
from django.shortcuts import render, redirect

from quitzapp.models import Questions, Subject
from django.core.paginator import Paginator
from quitzapp.forms import Questions_Form
from django.contrib.auth.forms import UserCreationForm

from django.db import models
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect


# Create your views here.

def Add_Questions(request):
    form = Questions_Form()
    if request.method == 'POST':
        form = Questions_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("SubjectPage/")  # it's using the submit button function#
    return render(request, 'Quitzapp/Questions_Form.html', {'form': form})


def Delete_Qus(request, id):
    Qus = Questions.objects.get(id=id)
    Qus.delete()
    return redirect("/welcome/base")


def Subject_Page(request):
    subject = Subject.objects.all()
    context = {'subject': subject}
    return render(request, 'Quitzapp/Course_OptionPage.html', context)


def schoolPage(request):
    return render(request,"Quitzapp/schoolHomePage.html")

def Subject_Question_2(request, id):
    Qus = Questions.objects.filter(subject_id=id)
    count = Questions.objects.filter(subject_id=id).count()
    return render(request, 'Quitzapp/QuestionPage.html', {'Qus': Qus, 'count': count})


        


