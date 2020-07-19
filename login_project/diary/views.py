from django.shortcuts import render
from django.views import generic
from .models import Diary
from django.contrib.auth.mixins import LoginRequiredMixin
from .froms import DiaryForm

# Create your views here.

class IndexView(LoginRequiredMixin, generic.ListView):
    model = Diary
    template_name = 'diary/index.html'

    def get_queryset(self):
        diaries = Diary.objects.filter(user=self.request.user).order_by('-create_date')
        return diaries

class detailView(LoginRequiredMixin,generic.DetailView):
    model = Diary
    template_name = 'diary/detail.html'

class createView(LoginRequiredMixin,generic.CreateView):
    model = Diary
    form_class = DiaryForm
    template_name = 'diary/create.html'
    success_url = '/diary/'