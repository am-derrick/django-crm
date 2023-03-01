from django.shortcuts import render
from django.http import HttpResponse
from .models import Prospect


def prospect_list(request):
    prospects = Prospect.objects.all()
    context = {
        "prospects": prospects
    }
    return render(request, "prospects_list.html", context)

def prospect_detail(request, pk):
    prospect = Prospect.objects.get(id=pk)
    context = {
        "prospects": prospect
    }
    return render(request, "prospects_detail.html", context)