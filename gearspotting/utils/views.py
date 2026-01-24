from typing import Generic, TypeVar

from django.forms.models import ModelForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic.base import View

from gearspotting.utils.models import CustomModel

T = TypeVar("T", bound=CustomModel)


class AddSomethingView(Generic[T], View):
    context_obj_name = "object"
    model: type[T]
    template_name: str

    def get_form(self, obj: T) -> type[ModelForm]:
        raise NotImplementedError

    def get(self, request: HttpRequest, slug: str) -> HttpResponse:
        obj = get_object_or_404(self.model, slug=slug)
        form: ModelForm = self.get_form(obj)()
        data = dict(form=form)
        data[self.context_obj_name] = obj  # type: ignore
        return render(request, self.template_name, data)

    def post(self, request: HttpRequest, slug: str) -> HttpResponse:
        obj = get_object_or_404(self.model, slug=slug)
        form = self.get_form(obj)(request.POST, request.FILES)
        if form.is_valid():
            v = form.save(commit=False)
            v.content_object = obj
            v.save()
            return HttpResponseRedirect(obj.get_absolute_url())
        data = dict(form=form)
        data[self.context_obj_name] = obj  # type: ignore
        return render(request, self.template_name, data)


class EditSomethingView(Generic[T], View):
    model: type[T]

    def get_formset(self) -> type[ModelForm]:
        raise NotImplementedError

    def get(self, request: HttpRequest, slug: str) -> HttpResponse:
        obj = get_object_or_404(self.model, slug=slug)
        return HttpResponseRedirect(obj.get_absolute_url())

    def post(self, request: HttpRequest, slug: str) -> HttpResponse:
        obj = get_object_or_404(self.model, slug=slug)
        Formset = self.get_formset()
        formset = Formset(request.POST, request.FILES, instance=obj)
        if formset.is_valid():
            formset.save()
        return HttpResponseRedirect(obj.get_absolute_url())
