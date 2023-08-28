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
    if str(models.Content.objects.filter(user_id=pk)) != '<QuerySet []>':
        comments = []
        contents = models.Content.objects.filter(user_id=pk)
        for i in range(len(contents)):
            comments.append(models.Comment.objects.filter(comment_content_id=contents[i]))
        username = User.objects.get(id=pk)
        context = {'content': contents,
                   'comment': comments,
                   'user_id': username}
        return render(request, 'exact_profile.html', context)
    else:
        username = User.objects.get(id=pk)
        context = {'user_id': username}
        return render(request, 'empty_profile.html', context)


def add_like(request, pk):
        amount_like = models.Content.objects.get(id=pk)
        amount_like.content_likes += 1
        amount_like.save(update_fields=["content_likes"])
        user_content = models.User.objects.get(username=amount_like.user_id)
        return redirect(f'/profiles/{user_content.id}')


def add_dislike(request, pk):
        amount_dislike = models.Content.objects.get(id=pk)
        amount_dislike.content_dislikes += 1
        amount_dislike.save(update_fields=["content_dislikes"])
        user_content = models.User.objects.get(username=amount_dislike.user_id)
        return redirect(f'/profiles/{user_content.id}')


def write_article(request):
    article_bar = forms.ArticleForm()
    context = {'form': article_bar}
    return render(request, 'write_article.html', context)


def post_article(request, pk):
    us_id = models.User.objects.filter(id=pk)
    new_article = models.Content(user_id_id=us_id.values('pk'),
                                 content_name=request.POST.get('name'),
                                 content_info=request.POST.get('info'))
    new_article.save()
    return redirect(f'/profiles/{pk}')


def write_comment(request, pr_id, ct_id):
    comment_bar = forms.CommentForm()
    context = {'pr_id': pr_id, 'ct_id': ct_id, 'form': comment_bar}
    return render(request, 'write_comment.html', context)


def post_comment(request, pr_id, ct_id, us_id):
    com_cont = models.Content.objects.filter(id=ct_id)
    print(com_cont.values('pk'))
    to_whom = User.objects.filter(id=pr_id)
    who_post = User.objects.filter(id=us_id)
    new_comment = models.Comment(comment_content_id=com_cont.values('pk'),
                                 who_post_id=who_post.values('pk'),
                                 to_whom_id=to_whom.values('pk'),
                                 comment_info=request.POST.get('info'))
    new_comment.save()
    return redirect(f'/profiles/{pr_id}')