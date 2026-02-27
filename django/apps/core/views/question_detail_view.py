from typing import Any

from django.contrib.auth.decorators import login_not_required
from django.forms import Form
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import FormView

from ..models import ModelML
from ..questions import QUESTIONS_MAP


def get_clfs():
    return ModelML.objects.filter(is_public=1)


def format_data(cleaned_data: dict):
    data = [value for value in cleaned_data.values()]
    # data.extend([0, 0.5, 0.6, 1])
    return data


@method_decorator(login_not_required, name="dispatch")
class QuestionDetailView(FormView):
    template_name = 'core/question/form.html'

    def get_question(self):
        return QUESTIONS_MAP.get(self.kwargs.get('id'))

    def get_form_class(self) -> type[Form]:
        return getattr(self.get_question(), 'form_class', Form)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        if (q := self.get_question()) is not None:
            context['question'] = q
        else:
            # Se question for None, então Form é inválido
            context.pop('form')

        return context

    def form_valid(self, form: Form):
        from sklearn.utils import estimator_html_repr
        # formatar dados para input do modelo
        data = format_data(form.cleaned_data)

        # Carregar modelos
        questao = self.get_question()
        assert questao is not None
        clfs = get_clfs().filter(tipo=questao.tipo_modelo).all()

        # fazer classificação
        context = self.get_context_data()
        context["resultado"] = [
            (c, *c.predict(data), *(c.predict_proba(data) * 100), estimator_html_repr(c.model))
            for c in clfs
        ]
        from pprint import pprint
        for c in clfs:
            pprint(estimator_html_repr(c.model))
            # print(c.nome)
        return render(
            request=self.request,
            template_name='core/question/answer.html',
            context=context,
        )
