import django.forms as forms
import django.core.validators as v


class AddCourseForm(forms.Form):
    title = forms.CharField(max_length=30, label="Course Title")
    duration = forms.IntegerField(initial=30, label="Course Duration (Hours)",
                                  validators=[v.MinValueValidator(10), v.MaxValueValidator(100)])
    fee = forms.IntegerField(label="Course Fee")


class AddBookForm(forms.Form):
    title = forms.CharField(max_length=30, min_length=5, label="Book Title")
    author = forms.CharField(max_length=30, label="Author Name")
    price = forms.IntegerField(label="Book Price", min_value=100)
    btype = forms.ChoiceField(label="Book Type", required=True,
                              widget= forms.RadioSelect,
                              choices=[('k', 'Kindle Edition'),
                                       ('p', "PaperBack"),
                                       ('h', 'Hardbound')])
