from django.forms import ModelForm, BooleanField

from dogs.models import Dog, Parent


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class DogForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Dog
        exclude = ('view_counter', 'owner')


class ParentForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Parent
        fields = '__all__'

    # def clean_year_born(self):
    #     year_born = self.changed_data['year_born']
    #     if year_born =


class DogModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Dog
        fields = ('description', 'breed')
