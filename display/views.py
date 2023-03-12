import json

from django.shortcuts import render
from .forms import UploadFileForm
from .readfile import display_clusters


def displaydoc(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            document = request.FILES['file']
            contenu = json.load(document)
            clusters = display_clusters(contenu)
            return render(request,'display/upload.html', {'clusters': clusters, 'form':form})
    else:
        form = UploadFileForm()
    return render(request, 'display/form.html', {'form': form})



