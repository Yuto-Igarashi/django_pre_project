from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import SignUpForm



def index(request):
    return render(request,'myapp/index.html')

@login_required
#login_requiredデコレータがあるとログイン状態出ない場合に訪れると任意のページにリダイレクトする
#リダイレクト先は,settigs.pyのLOGIN_URLで指定する
def home(request):
    return render(request,'myapp/home.html')
    
class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'myapp/signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)        
        self.object = user
        return HttpResponseRedirect(self.get_success_url())

