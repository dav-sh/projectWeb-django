from django import forms


class ContactForm(forms.Form):
    your_name = forms.CharField(label="Name", widget=forms.TextInput({ "placeholder": "your name"}),max_length=100, required=True)
    your_email = forms.EmailField(label="Email", widget=forms.TextInput({ "placeholder": "example@example.com"}),required=True)
    your_message = forms.CharField(label='Message', widget = forms.Textarea ,  required=False)