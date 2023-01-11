from django import forms
from django.core.validators import validate_email
#gettext_lazy is useful for language translation
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm

User=get_user_model()


class RegistrationForm(forms.Form):
    
    first_name = forms.CharField(required=True,)
    last_name = forms.CharField(required=True,)
    email = forms.EmailField(required=True,)
    username = forms.CharField(required=True,help_text=None)
    password = forms.CharField(required=True,min_length=8,widget=forms.PasswordInput())
    confirm_password = forms.CharField(required=True,min_length=8,widget=forms.PasswordInput())

    # check if email has been registered
    def clean_email(self,*args,**kwargs):
        email=self.cleaned_data.get('email')
        email_qs=User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError(_("A user with this email already exists."),code='email_already_used',)
        else:
            return email
    
    #check if username has been registered
    def clean_username(self,*args,**kwargs):
        username=self.cleaned_data.get('username')
        username_qs=User.objects.filter(username=username)
        if username_qs.exists():
            raise forms.ValidationError(_("A user with this username already exists."),code='username_already_used',)
        else:
            return username

    #check if the two passwords provided match
    def clean(self,*args,**kwargs):
        password=self.cleaned_data.get('password')
        confirm_password=self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            self.add_error(field="confirm_password",error="The passwords provided did not match.")
        else:
            #important!! call parent clean() so as to return the object 'cleaned data'
            return super().clean()


class LogInForm(forms.Form):

    username_or_email = forms.CharField(required=True,)
    password = forms.CharField(required=True,widget=forms.PasswordInput())

    def clean_username_or_email(self,*args,**kwargs):
        username_or_email=self.cleaned_data.get('username_or_email')

        # check if provided is a valid email
        try:
            #import validate_email from django.core.validators to check if a value is a valid email
            validate_email(username_or_email)
            #if no exception is raised then value is an email
            is_email = True

        except forms.ValidationError as err:
            #if exception is raised value is not a valid email
            is_email = False

        if is_email:
            email = username_or_email
            #if the value is a valid email
            #check if email is registered
            email_qs=User.objects.filter(email=email)
            if email_qs.exists():
                #if email is registered get the user
                user=User.objects.get(email=email)
                #check if user is active
                if user.is_active:
                    #if active return username
                    return user.username
                else:
                    #if inactive raise validation error
                    raise forms.ValidationError(_("This account is inactive."),code='inactive',)
            else:
                # else raise email validation error
                raise forms.ValidationError(_("There is no user with that email."),code='invalid',)
        else:
            #if email validation failed probably value provided is a username
            #check if there is a username matching that value
            username = username_or_email
            username_qs=User.objects.filter(username=username)
            if username_qs.exists():
                #if username exists return username
                return username
            else:
                #if username doesnt exist raise exception
                raise forms.ValidationError(_("There is no user with that username."),code='invalid',)

class UserDetailsForm(forms.Form):
    first_name = forms.CharField(required=True,)
    last_name = forms.CharField(required=True,)
    email = forms.EmailField(required=True,)
    username = forms.CharField(required=True)
    
class StaffCreationForm(RegistrationForm):
    DESIGNATION = [
    ('admin', 'Admin'),
    ('writer', 'Writer'),
    ]
    designation = forms.ChoiceField(choices=DESIGNATION,required=True)

class StaffDetailsForm(forms.Form):
    DESIGNATION = [
    ('admin', 'Admin'),
    ('writer', 'Writer'),
    ]
    first_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'readOnly':True}))
    last_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'readOnly':True}))
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'readOnly':True}))
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'readOnly':True}))
    designation = forms.ChoiceField(choices=DESIGNATION,required=True)
