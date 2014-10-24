from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .forms import UploadPicForm
from pic.models import UploadPic

# Create your views here.
def uploadpic(request):
  if request.method == 'POST':
    form = UploadPicForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return render(request, 'pic/afterupload.html')
  else:
    form = UploadPicForm()
  return render(request, 'pic/upload.html', {'form':form})


def displaypic(request):
  imgNames = [p.file.name for p in UploadPic.objects.all()]
  return render(request, 'pic/listfiles.html', {'names': imgNames})

