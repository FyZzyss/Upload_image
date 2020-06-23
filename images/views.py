import requests
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.files.base import ContentFile

from test_django.settings import MEDIA_URL
from .models import Document
from .forms import DocumentForm
import hashlib


def list(request):
    documents = Document.objects.filter(docfile__contains=('.png' or '.jpg'))
    for doc in documents:
        doc.text = str(doc.docfile).split('/')[-1]
    return render(request,
                  'list.html',
                  {'documents': documents, 'MEDIA_URL': MEDIA_URL},
                  )


def upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            if request.POST['url_file']:
                temp_doc = ContentFile(requests.get(request.POST['url_file']).content)
                newdoc = Document(
                    docfile=ContentFile(temp_doc.read(), hashlib.md5(temp_doc.read()).hexdigest() + '.png'))
                newdoc.save()
                return HttpResponseRedirect(reverse('list'))
            elif request.FILES['docfile']:
                temp_doc = request.FILES['docfile']
                _, extension = str(temp_doc).split('.')
                newdoc = Document(
                    docfile=ContentFile(temp_doc.read(),
                                        hashlib.md5(temp_doc.read()).hexdigest() + f'.{extension}'))
                newdoc.save()
                return HttpResponseRedirect(reverse('list'))
            else:
                form = DocumentForm()
                return render(request, 'upload_image.html', {'form': form})
        else:
            form = DocumentForm()
            return render(request, 'upload_image.html', {'form': form})

    else:
        form = DocumentForm()
        return render(request, 'upload_image.html', {'form': form})


def get_image(request, hash):
    width = None
    height = None
    if request.method == 'GET':
        width = request.GET.get('width')
        height = request.GET.get('height')
    return render(request, 'single_image.html',
                  {'image': hash, 'MEDIA_URL': MEDIA_URL, 'height': height, 'width': width})
