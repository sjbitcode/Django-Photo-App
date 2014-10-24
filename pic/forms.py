from django import forms
from pic.models import UploadPic

class UploadPicForm(forms.ModelForm):
  class Meta:
    model = UploadPic
    
