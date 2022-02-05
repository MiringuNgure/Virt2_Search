from django import forms

class AirportSearchForm(forms.Form):
    q = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['q'].label = "Search For"
        self.fields["q"].widget.attrs.update(
            {'class': 'for-control'}
        )