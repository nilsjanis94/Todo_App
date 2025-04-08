from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Aufgabentitel eingeben'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Beschreibung der Aufgabe'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'title': 'Titel',
            'description': 'Beschreibung',
            'completed': 'Erledigt',
        }
        help_texts = {
            'title': 'Gib deiner Aufgabe einen prägnanten Titel.',
            'description': 'Beschreibe die Aufgabe ausführlich.',
        } 