from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm

from core.models import Registration, Mail


class RegisterForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        self.helper.layout.append(Submit('submit', 'Submit', css_class='btn-primary'))

    class Meta:
        model = Registration
        # error_messages = {
        #     NON_FIELD_ERRORS: {
        #         'unique': "This URL is taken",
        #     }
        # }
        fields = ['first_name', 'last_name','zip','email','phone','can_text']


class MailForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(MailForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        self.helper.layout.append(Submit('submit', 'Submit', css_class='btn-primary'))

    class Meta:
        model = Mail
        # error_messages = {
        #     NON_FIELD_ERRORS: {
        #         'unique': "This URL is taken",
        #     }
        # }
        fields = ['street','city','state','zip']