from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseRedirect
import requests


def download(request, file_name):
    print("file_name", file_name)
    if not request.user.is_authenticated:
        return HttpResponseRedirect(
            "/admin/login/?next=/api/download/{}".format(file_name)
        )
    response = HttpResponse()
    del response["Content-Type"]
    response["X-Access-Redirect"] = "/internal/"
    response["Content-Disposition"] = "attachment; filename='%s'" % file_name
    return response
