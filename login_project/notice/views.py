from django.shortcuts import render

from django.views import generic
from .models import Article

class listTemplate(generic.ListView):
    template_name = 'notice/list.html'
    context_object_name = 'latest_list'

    def get_queryset(self):
        #return Article.objects.all()
        return Article.objects.order_by('-create_date')[:5]

class detailTemplate(generic.DetailView):
    model = Article
    template_name = 'notice/detail.html'