from django.shortcuts import render
from django.shortcuts import redirect
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required 
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login, authenticate
from .forms import (
    CustomUserCreationForm,
    UserUpdateForm,
)
from django.contrib.auth import get_user_model
from django.views.generic import (
    DetailView,
    UpdateView,
    DeleteView,
)    # cambiar
from django.urls import reverse
from django.contrib.auth.views import (
    PasswordChangeView, PasswordChangeDoneView
)

from django.views.generic import DetailView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import login_required

User = get_user_model()

class OnlyYouMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser

class UserDetail(OnlyYouMixin, DetailView): 
    model = User
    template_name = 'tasks/user_detail.html'
    context_object_name = 'user'

class UserUpdate(OnlyYouMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'tasks/user_edit.html'

    def get_success_url(self):
        return reverse('user_detail', kwargs={'pk': self.kwargs['pk']})
    
    
    
class PasswordChange(PasswordChangeView):
    template_name = 'tasks/password_change.html'


class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'tasks/user_detail.html'
    
class UserDelete(OnlyYouMixin, DeleteView): 
    model = User
    template_name = 'tasks/user_delete.html'
    success_url = reverse_lazy('login')
    

@login_required    # Apéndice
def create(request):
    if (request.method == 'POST'):
        title = request.POST['title']
        content = request.POST['content']
        article = Article(title=title, content=content)
        article.save()
        return redirect('blog:index')
    else:
        params = {
            'form': ArticleForm(),
        }
        return render(request, 'blog/create.html', params)
