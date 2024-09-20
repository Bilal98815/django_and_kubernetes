from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView


def status(request):
    data = {
        "status": "ok",
        "environment": "production",
        "release": "28baa253a529cb84cf6fe7b5002a6fe6f9acbca2",
        "hostname": "bulkproducteditor-58f964b4f4-p75mv",
        "maintenance_mode": False,
        "uptime": 1733
    }
    return JsonResponse(data)


def home(request):
    return render(request, 'base.html')


class RobotsTextView(TemplateView):
    template_name = "robots.txt"
    content_type = "text/plain"
