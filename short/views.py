from django.shortcuts import render, get_object_or_404
from django.views.generic.base import RedirectView
from django.views.generic.edit import CreateView
from django.views.generic import DetailView


from .models import Link


class LinkCreateView(CreateView):
    model = Link
    fields = ['long_url']


class LinkDetailView(DetailView):
    model = Link


class RedirectToLongURLView(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        short_url_code = self.kwargs.get('short_url_code')
        decoded_hash = Link.decode_url(short_url_code)
        link_obj = get_object_or_404(Link, pk=decoded_hash)
        return ("" + link_obj.long_url)
