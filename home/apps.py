from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackForm
        fields = ['name', 'comments']
        widgets = {
            'comments': forms.Textarea(attrs={'rows'; 4, 'placeholder': 'Write your feedback here....'}),
        }