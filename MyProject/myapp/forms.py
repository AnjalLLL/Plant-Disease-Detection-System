from django import forms

class ProfileUpdateForm(forms.Form):
  
    bio = forms.CharField(widget=forms.Textarea, required=False)
    profile_picture = forms.ImageField(required=False)
    occupation = forms.CharField(max_length=100, required=False)