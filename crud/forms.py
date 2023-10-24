from django import forms
from .models import EventModel

class EventForm(forms.ModelForm):
    class Meta:
        model = EventModel  
        fields = ["author",
                  "title",
                  "event",
                  "neighborhood",
                  "eyesColor",
                  "furColor",
                  "gender",
                  "age",
                  "pic",
                  "lost",
                  "found",
                  "contact"
                  ]

        def __init__(self, *args, **kwargs):
            super(EventForm, self).__init__(*args, **kwargs)
            
            # If there is a logged-in user, restrict 'author' to that user
            if self.instance and self.instance.author:
                self.fields['author'].queryset = EventModel.objects.filter(author=self.instance.author)
            else:
                # If no user is logged in, provide an empty queryset and hide the field
                self.fields['author'].queryset = EventModel.objects.none()
                self.fields['author'].widget = forms.HiddenInput()