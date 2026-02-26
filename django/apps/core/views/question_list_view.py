from typing import Any

from django.views.generic import TemplateView
from .. import questions

_data = [
    questions.DIABETES,
].sort(key=lambda q: q.id)


class QuestionListView(TemplateView):
    template_name = 'core/question_list_view.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['questions'] = _data
        return context
