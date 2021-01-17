from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        "class": 'form-control',
        "id": 'p_name',
        "placeholder": 'Full Name...'
    }))
    email = forms.EmailField(max_length=150, widget=forms.EmailInput(attrs={
        "class": 'form-control',
        "id": 'p_email',
        "placeholder": 'Enter Address...'
    }))
    subject = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        "class": 'form-control',
        "id": 'p_subject',
        "placeholder": 'Subject...'
    }))
    message = forms.CharField(max_length=255, widget=forms.Textarea(attrs={
        "class": 'form-control',
        "id": 'p_message',
        "rows": 6,
        "placeholder": 'Write message'
    }))

