from django.shortcuts import redirect, render, reverse, get_object_or_404
from info.models import Subject, Question
from django.contrib import messages

from .forms import QuestionForm


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def subject(request):

    subjects = Subject.objects.all()
    questions = Question.objects.all()

    return render(request, 'faq.html', {'subjects':subjects, 'questions':questions})

def add_faq(request):
    """ Add new faq question and answer """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New FAQ added!')
            return redirect(reverse(add_faq))
        else:
            messages.error(request, 'Failed to add new FAQ, please check form is valid.')
    else:
        form = QuestionForm()
    template = 'add_faq.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
