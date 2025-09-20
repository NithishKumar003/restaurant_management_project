from django import forms
from .models import ContactSubmission, Feedback

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message', 'rows': 4, 'class': 'form-control'}),
        }
        labels = {
            'name': 'Full Name', 
            'email': 'Email Address', 
            'message': 'Message',
        }

        email = forms.EmailField(
            required=True,
            widget=forms.EmailInput(attrs={'placeholder': 'Your email address'}),
            error_messages={
                'invalid': 'Enter a valid email address.',
                'required': 'Email is required.'
            }
        )

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'feedback_text']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your Name (optional)',
                'class': 'form-control'
            }),
            'feedback_text': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Write your feedback here...',
                'class': 'form-control'
            }),
        }
        lables = {
            'name': 'Name', 
            'feedback_text': 'Your Feedback', 
        }