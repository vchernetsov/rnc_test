from django import forms
import dateutil.parser

from itsdangerous import Signer
signer = Signer("secret-key")

class ToSForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'style': 'display:none'}))
    signature = forms.CharField(widget=forms.HiddenInput)
    timestamp = forms.CharField(widget=forms.HiddenInput)

    def clean_text(self):
        text = self.cleaned_data['text']
        text = text.replace("\r\n", "\n")
        self.cleaned_data['text'] = text
        return text

    def clean_timestamp(self):
        timestamp = self.cleaned_data['timestamp']
        timestamp = dateutil.parser.parse(timestamp)
        return timestamp

    def clean_signature(self):
        text = self.cleaned_data['text']
        text = text.replace("\r\n", "\n")
        signature = self.cleaned_data['signature']
        if not signer.verify_signature(text.encode(), signature):
            raise forms.ValidationError("Signature is not valid!")
        return signature
