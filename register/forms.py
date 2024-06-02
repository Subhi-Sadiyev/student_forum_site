from django import forms
from main.models import Author

class UpdateForm(forms.ModelForm):
    
    class Meta:
        model = Author
        fields = ("fullname", "bio", "profile_pic")
        labels={
            "fullname" : "Tam adınız",
            "bio" : "Haqqınızda",
            "profile_pic" : "Profil şəkliniz",
        }
