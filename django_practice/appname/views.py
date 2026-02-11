from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

def tale(req):
    return render(req, template_name="index.html")
def aboutTale(req):
    return render(req, template_name="about.html")

def hel(req):
    return render(req, template_name="help.html")
def save_data(req):
    print(req.POST)
    title = req.POST.get("title", "")
    description = req.POST.get("description", "")

    if not title or not description:
            messages.error(req, "Fill all details")
            return redirect("/help")

        
    return HttpResponse(f"title: {title}, description = {description}")
