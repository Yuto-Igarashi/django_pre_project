from django.shortcuts import render
from django.views import generic
from .models import Diary
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class IndexView(LoginRequiredMixin, generic.ListView):
    model = Diary
    template_name = 'diary/index.html'

    def get_queryset(self):
        dirares = Diary.objects.filter(user=self.request.user).order_by('-create_date')
        return dirares