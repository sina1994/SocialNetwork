from django.forms import Form
"""
class User_info(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    e_mail = forms.EmailField()
    passwd = forms.CharField()
    

"""


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file  = forms.FileField(type='file')
