# -*- coding: utf-8 -*-
from django.forms import forms, CharField
from django.http import HttpResponse
from django.shortcuts import render
from korean.fields import JuminFormField


class TestForm(forms.Form):
    jumin1 = JuminFormField()
    jumin2 = JuminFormField()


def demo(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            return HttpResponse('success : ' + form.cleaned_data['jumin'])

    else:
        form = TestForm(initial={'jumin1': '010203-4567890'})

    return render(request, 'demo.html', {'form': form})
