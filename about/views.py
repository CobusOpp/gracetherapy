from django.shortcuts import render

def dotnortje(request):
    return render(request, "dotnortje.html", {})

def gracetherapy(request):
    return render(request, "gracetherapy.html", {})

def remedial(request):
    return render(request, "remedial.html", {})
