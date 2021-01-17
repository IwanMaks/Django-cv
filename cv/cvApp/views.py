from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic import DetailView
from django.core.mail import send_mail
from django.contrib import messages


def index(request):
    about = About.objects.get(pk=1)
    knowledge = Knowledge.objects.all()
    skill = Skill.objects.all()
    story = Story.objects.all()
    allimg = AllImg.objects.get(pk=1)
    work = Work.objects.all()
    social = SocialLinks.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['message'], 'iwanmak71@yandex.ru', ['iwan.maksackov@yandex.ru'], fail_silently=False)
            if mail:
                messages.success(request, 'Письмо отправлено!')
                return redirect('home')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Ошибка заполнения формы')
    else:
        form = ContactForm()

    context = {
        'about': about,
        'knowledge': knowledge,
        'skill': skill,
        'story': story,
        'work': work,
        'allImg': allimg,
        'social': social,
        'form': form,
    }
    return render(request, 'index.html', context=context)


class ViewWork(DetailView):
    model = Work
    template_name = 'single-portfolio.html'
    context_object_name = 'work'
