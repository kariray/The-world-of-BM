from dataclasses import field
from django import forms
from . import models


class CreateBookForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = models.Book
        fields = [
            "title",
            "year",
            "rating",
            "cover_image",
            "category",
            "writer",
            "storyline",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "p-2"}),
            "year": forms.NumberInput(attrs={"class": "p-2"}),
            "rating": forms.NumberInput(attrs={"class": "p-2"}),
            "storyline": forms.Textarea(attrs={"class": "p-2"}),
        }
        required = (
            "title",
            "year",
            "rating",
            "category",
            "writer",
        )

    def clean(self):
        title = self.cleaned_data.get("title")

        if len(title) <= 0:
            self.add_error("title", forms.ValidationError(
                "title is not empty."))
        else:
            return self.cleaned_data

    # def save(self, *args, **kwargs):
    #     book = super().save(commit=False)
    #     return book
