from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from .forms import ContactForm
from .utils import send_contact_email


# Create your views here.


class HomeView(FormView):
    template_name = 'home.html'
    form_class = ContactForm
    success_url = reverse_lazy('core:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = ContactForm()
        context['form'] = form
        return context

    def form_valid(self, form):
        contact = form.save()
        send_contact_email(contact)
        messages.success(self.request, 'Your message has been sent. Thank you!')
        return super().form_valid(form)


# class ContactView(FormView):
#     template_name = 'home.html'
#     form_class = ContactForm
#     success_url = reverse_lazy('core:home')
#
#     def form_valid(self, form):
#         contact = form.save()
#         send_contact_email(contact)
#         messages.success(self.request, 'Your message has been sent. Thank you!')
#         return super().form_valid(form)
