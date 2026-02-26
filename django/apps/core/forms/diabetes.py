from django import forms

fields: dict[str, int | float] = {
    'Pregnancies': 6,
    'Glucose': 148,
    'BloodPressure': 72,

    'SkinThickness': 35,
    'Insulin': 0,
    'BMI': 33.6,
    'DiabetesPedigreeFunction': 0.627,

    'Age': 50,
}
class DiabetesForm(forms.Form):
    num_pregnancies = forms.IntegerField(
        label='quantidade de gravidez',
        min_value=0, required=True,
        help_text='Quantidade de gravidez que teve',
    )
    num_glucose = forms.IntegerField(
        label='Glicose',
        label_suffix='mg',
        min_value=0, required=True,
        help_text='Quantidade de Glicose no sangue',
    )
    blood_pressure = forms.IntegerField(
        label='Pressão sanguinea',
        min_value=0, required=True,
        help_text='Pressão sanguinea'
    )
    idade = forms.IntegerField(
        label='idade',
        max_value=150, min_value=0, required=True,
    )