from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.layout import Div
from app.models import ExpensesRegistry

class ExpensesForm(forms.ModelForm):
    class Meta:
        model = ExpensesRegistry
    	fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ExpensesForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
        	Div(
        		'expenses',
        		'income',
        		'income_date',
        		'expenses_concept',
        		'income_concept',
        		'category',
        	)
        )
