from django import forms
from .models import EventModel

# ajusting the text area
class ResponsiveSizeTextarea(forms.widgets.Textarea):
    def __init__(self, attrs=None, size_percentage=100):
        if attrs is None:
            attrs = {}
        attrs['style'] = f'width: {size_percentage}%;'
        super().__init__(attrs)

# ajusting the image size area
class ResponsiveSizeFileInput(forms.widgets.FileInput):
    def __init__(self, attrs=None, width_percentage=100):
        if attrs is None:
            attrs = {}
        attrs['style'] = f'width: {width_percentage}%;'
        super().__init__(attrs)


class EventForm(forms.ModelForm):
    class Meta:
        model = EventModel  
        fields = ["author",
                  "title",
                  "event",
                  "type",
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
        
        widgets = {
            'event': ResponsiveSizeTextarea(size_percentage=100),
            'pic': ResponsiveSizeFileInput(width_percentage=100),
        }

        def __init__(self, *args, **kwargs):
            super(EventForm, self).__init__(*args, **kwargs)
            
            # If there is a logged-in user, restrict 'author' to that user
            if self.instance and self.instance.author:
                self.fields['author'].queryset = EventModel.objects.filter(author=self.instance.author)
            else:
                # If no user is logged in, provide an empty queryset and hide the field
                self.fields['author'].queryset = EventModel.objects.none()
                self.fields['author'].widget = forms.HiddenInput()