from __future__ import unicode_literals
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Field
from authtools import forms as authtoolsforms
from django.contrib.auth import forms as authforms
from django.urls import reverse


class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, initial=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["username"].widget.input_type = "email"  # ugly hack

        self.helper.layout = Layout(
            Field("username", placeholder="Enter Email",autofocus="", css_class="form-control"),
            Field("password", placeholder="Enter Password",css_class="form-control"),
            HTML(
                '<a href="{}">Forgot Password?</a>'.format(
                    reverse("accounts:password-reset")
                )
            ),
            Field("remember_me"),
            Submit("sign_in", "Sign In", css_class="btn_1 full-width mb_5"),
        )


class SignupForm(authtoolsforms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["email"].widget.input_type = "email"  # ugly hack

        self.helper.layout = Layout(
            Field("email", placeholder="Enter Email", autofocus="", css_class="form-control"),
            Field("name", placeholder="Enter Full Name", css_class="form-control"),
            Field("password1", placeholder="Enter Password", css_class="form-control"),
            Field("password2", placeholder="Re-enter Password", css_class="form-control"),
            Submit("sign_up", "Sign up Now", css_class="btn_1 full-width mb_5"),
        )


class PasswordChangeForm(authforms.PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Field("old_password", placeholder="Enter old password", autofocus=""),
            Field("new_password1", placeholder="Enter new password"),
            Field("new_password2", placeholder="Enter new password (again)"),
            Submit("pass_change", "Change Password", css_class="btn-warning"),
        )


class PasswordResetForm(authtoolsforms.FriendlyPasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Field("email", placeholder="Enter email", autofocus=""),
            Submit("pass_reset", "Reset Password", css_class="btn-warning"),
        )


class SetPasswordForm(authforms.SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Field("new_password1", placeholder="Enter new password", autofocus=""),
            Field("new_password2", placeholder="Enter new password (again)"),
            Submit("pass_change", "Change Password", css_class="btn-warning"),
        )
