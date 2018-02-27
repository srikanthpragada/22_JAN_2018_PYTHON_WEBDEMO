import django.forms as forms
import django.core.validators as v


class AddCourseForm(forms.Form):
    title = forms.CharField(max_length=30, label="Course Title")
    duration = forms.IntegerField(initial=30, label="Course Duration (Hours)",
                validators=[v.MinValueValidator(10), v.MaxValueValidator(100)])
    fee = forms.IntegerField(label="Course Fee")
