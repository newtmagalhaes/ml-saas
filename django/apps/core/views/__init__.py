import pickle
from typing import Any

from django.contrib.auth.decorators import login_not_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

# register Your views here
from .diabetes_form_view import DiabetesFormView, _get_clf2


# Create your views here.
@method_decorator(login_not_required, name="dispatch")
class PredictView(TemplateView):
    template_name = 'core/predict.html'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        clfs = _get_clf2(self.request.user)
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
        data = [v for v in fields.values()]
        context["resultado"] = [
            (c, *c.predict(data), *(c.predict_proba(data) * 100))
            for c in clfs
        ]
        print(context['resultado'])
        return context
