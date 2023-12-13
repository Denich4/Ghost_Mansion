from django.shortcuts import render
from django.http import request, HttpResponse
from django.utils.encoding import smart_str


def index(request):
    return render(request, 'index.html', {})

def download(request):
    file_name = "Ghost_Mansion_Win64.zip"
    path_to_file = ""
    response = HttpResponse(mimetype='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name)
    response['X-Sendfile'] = smart_str(path_to_file)
    return response