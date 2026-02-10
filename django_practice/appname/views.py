from django.shortcuts import render
from django.http import HttpResponse
def tale(req):
    return render(req, template_name="index.html")
def aboutTale(req):
    return render(req, template_name="about.html")

def hel(req):
    return render(req, template_name="help.html")
def save_data(req):
    print(req.POST)
    return HttpResponse("Data Saved")