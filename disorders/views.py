from django.shortcuts import render

def disorder(request):
    return render(request, "disorder.html", {})
