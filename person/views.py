from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from cpf.cpf import CpfMixin
from person.models import Person


class ListPersonView(LoginRequiredMixin, CpfMixin, ListView):
    model = Person

    def get_context_data(self, *, object_list=None, **kwargs):
        cx = super(ListPersonView, self).get_context_data(**kwargs)
        cx.update({"response": self.get_token()})
        return cx
