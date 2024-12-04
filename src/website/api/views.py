from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required(login_url="/admin/login/")
def download(request, file_name: str) -> HttpResponse:
    response = HttpResponse()
    del response["Content-Type"]
    response["X-Accel-Redirect"] = f"/internal/{file_name}"
    response["Content-Disposition"] = f"attachment; filename={file_name}"
    return response
