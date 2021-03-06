from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit
from django.forms import ModelForm
from parsley.decorators import parsleyfy

from attendance.models import Attendance


@parsleyfy
class AttendanceForm(ModelForm):
    class Meta:
        model = Attendance
        exclude = []

    def __init__(self, *args, **kwargs):
        super(AttendanceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.attrs = {"data-parsley-validate": "data-parsley-validate"}
        self.helper.layout = Layout(
            Div(
                Div('user', css_class="col-md-6"),
                Div('check_in', css_class="col-md-6"),
                css_class="row"),
            Div(
                Div('check_out', css_class="col-md-6"),
                Div('duration', css_class="col-md-6"),
                css_class="row"),
            Div(
                Div(Div(Submit('save', _('Save Changes'), css_class='btn btn-success btn-block'),
                        css_class="col-md-6 col-md-offset-3"),
                    css_class="row")
            )
        )
