from pprint import pprint

from django.contrib.auth.decorators import login_not_required
from django.forms import Form
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import FormView

from ..forms.diabetes import DiabetesForm
from ..models import ModelML


def _get_clf2(user):
    return ModelML.objects.all()

@method_decorator(login_not_required, name="dispatch")
class DiabetesFormView(FormView):
    template_name = 'core/diabetes/form.html'
    form_class = DiabetesForm

    def form_valid(self, form: Form):
        pprint(form.cleaned_data)

        # formatar dados para input do modelo
        data = [value for value in form.cleaned_data.values()]
        data.extend([0, 0.5, 0.6, 1])

        # Carregar modelo
        clfs = _get_clf2(self.request.user)

        # fazer classificação
        context = self.get_context_data()
        context["resultado"] = [
            (c, *c.predict(data), *(c.predict_proba(data) * 100))
            for c in clfs
        ]
        pprint(context['resultado'])
        return render(
            request=self.request,
            template_name='core/predict.html',
            context=context,
        )
