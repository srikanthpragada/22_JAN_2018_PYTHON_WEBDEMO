import django.forms as forms
# from django.forms import ModelForm
import django.core.validators as v
from demo.models import Account, Transaction


class AddAccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['customer', 'email', 'mobile', 'balance']


class AddTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['trans_date', 'trans_amount',
                  'trans_type', 'trans_remarks' , 'account']



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
                              widget=forms.RadioSelect,
                              choices=[('k', 'Kindle Edition'),
                                       ('p', "PaperBack"),
                                       ('h', 'Hardbound')])
