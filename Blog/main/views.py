from django.shortcuts import render, redirect
from . import forms, models
from django.contrib.auth.models import User

# Create your views here.


def home_page(request):
    search_bar = forms.SearchForm()
    context = {'form': search_bar}
    return render(request, 'home-page.html', context)


def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = forms.RegisterForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def search_profile(request):
    if request.method == 'POST':
        get_user_id = request.POST.get('search_profile')
        try:
            exact_profile = User.objects.get(username__icontains=get_user_id)
            return redirect(f'profiles/{exact_profile.id}')
        except:
            return redirect('/')


def exact_profile_html(request, pk):
    user_content = models.Content.objects.filter(user_id=pk)
    context = {'content': user_content}
    return render(request, 'exact_profile.html', context)


def add_like(request, pk):
    if request.method == 'POST':
            amount_like = models.Content.objects.get(id=pk)
            amount_like.content_likes += 1
            amount_like.save(update_fields=["content_likes"])
            user_content = models.User.objects.get(username=amount_like.user_id)
            return redirect(f'/profiles/{user_content.id}')


def add_dislike(request, pk):
    if request.method == 'POST':
            amount_dislike = models.Content.objects.get(id=pk)
            amount_dislike.content_dislikes += 1
            amount_dislike.save(update_fields=["content_dislikes"])
            user_content = models.User.objects.get(username=amount_dislike.user_id)
            return redirect(f'/profiles/{user_content.id}')


def write_article(request):
    if request.method == 'post':
        pass
