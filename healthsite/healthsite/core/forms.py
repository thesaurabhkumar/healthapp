from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from healthsite.core.models import ExerciseData
from crispy_forms.helper import FormHelper
from django.core.urlresolvers import reverse
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab, Accordion, AccordionGroup
from crispy_forms.layout import Submit, Layout, Div, Fieldset, MultiField
from crispy_forms.layout import Submit, Reset, HTML
from crispy_forms.layout import Button
from django.core import validators
from django.core.exceptions import ValidationError
from django.forms.formsets import BaseFormSet

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ("username", 'first_name', 'last_name', 'email', 'password1', 'password2',)



class AddExerciseForm(forms.ModelForm):
    Exercise_name = forms.CharField(label='Exercise Name',
                                 max_length=100,
                                 required=True,
                                 help_text='Required.',
                                 widget=forms.TextInput(attrs={'autofocus': 'autofocus',
                                                               'autocomplete': 'off',
                                                               'size': '100',
                                                               'style': 'font-size: small',
                                                               })
                                 )

    Exercise_muscles = forms.CharField(label='Muscles Impacted',
                                      max_length=500,
                                      required=True,
                                      help_text='Required.',
                                      widget=forms.TextInput(attrs={'autofocus': 'autofocus',
                                                                    'autocomplete': 'off',
                                                                    'size': '100',
                                                                    'style': 'font-size: small',
                                                                    })
                                      )

    Exercise_taker_level = forms.CharField(label='Exercise Level',
                                          max_length=100,
                                          required=True,
                                          help_text='Required.',
                                          widget=forms.TextInput(attrs={'autofocus': 'autofocus',
                                                                        'autocomplete': 'off',
                                                                        'size': '100',
                                                                        'style': 'font-size: small',
                                                                        })
                                          )

    Exercise_sets = forms.CharField(label='Number of Sets Recommended',
                                              max_length=30,
                                              required=False,
                                              help_text='Required.',
                                              widget=forms.TextInput(attrs={'autofocus': 'autofocus',
                                                                            'autocomplete': 'off',
                                                                            'size': '100',
                                                                            'style': 'font-size: small',
                                                                            })
                                              )

    Exercise_reps = forms.CharField(label='Number of reps Per Sets Recommended',
                                   max_length=30,
                                   required=False,
                                   help_text='Optional.',
                                   widget=forms.TextInput(attrs={'autofocus': 'autofocus',
                                                                 'autocomplete': 'off',
                                                                 'size': '100',
                                                                 'style': 'font-size: small',
                                                                 })
                                   )

    Exercise_description = forms.CharField(label='Description',
                                         max_length=5000,
                                         required=True,
                                         help_text='Required.',
                                         widget=forms.TextInput(attrs={'autofocus': 'autofocus',
                                                                       'autocomplete': 'off',
                                                                       'size': '100',
                                                                       'style': 'font-size: small',
                                                                       })
                                         )




    class Meta:
        model = ExerciseData
        fields = ('Exercise_name', 'Exercise_muscles',
                  'Exercise_taker_level', 'Exercise_sets',
                  'Exercise_reps', 'Exercise_description'
                  )


    helper = FormHelper()
    helper.form_method = 'post'
    helper.form_class = 'form-horizontal'
    helper.add_input(Submit('submit', 'Submit', css_class='btn-success'))
    helper.add_input(Reset('cancel', 'Clear', css_class='btn-warning'))
    helper.layout = Layout(
        Div('Exercise_name', 'Exercise_muscles',
                  'Exercise_taker_level', 'Exercise_sets',
                  'Exercise_reps', 'Exercise_description')
    )
