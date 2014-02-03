from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views.generic.base import View


class AddSomethingView(View):
    context_obj_name = "object"

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug=slug)
        form = self.get_form(obj)
        f = form()
        data = dict(form=f)
        data[self.context_obj_name] = obj
        return render(
            request,
            self.template_name,
            data)

    def post(self, request, slug):
        obj = get_object_or_404(self.model, slug=slug)
        form = self.get_form(obj)
        f = form(request.POST, request.FILES)
        if f.is_valid():
            l = f.save(commit=False)
            l.content_object = obj
            l.save()
            return HttpResponseRedirect(obj.get_absolute_url())
        data = dict(form=f)
        data[self.context_obj_name] = obj
        return render(
            request, self.template_name,
            data)


class EditSomethingView(View):
    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug=slug)
        return HttpResponseRedirect(obj.get_absolute_url())

    def post(self, request, slug):
        obj = get_object_or_404(self.model, slug=slug)
        Formset = self.get_formset()
        formset = Formset(request.POST, request.FILES, instance=obj)
        if formset.is_valid():
            formset.save()
        return HttpResponseRedirect(obj.get_absolute_url())
