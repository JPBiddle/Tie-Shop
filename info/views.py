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

def delete_faq(request, question_id):
    subject = get_object_or_404(Question, pk=question_id)
    subject.delete()
    messages.success(request, 'Q&A has been deleted.')
    return redirect(reverse('faq'))

def edit_faq(request, question_id):
    """ Edit FAQ question and answer"""
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES, instance=question)
        if form.is_valid():
            question = form.save()
            messages.success(request, 'FAQ successfully updated!')
            return redirect(reverse('faq'))
        else:
            messages.error(request, 'FAQ edit failed. Please ensure the form is valid.')
    else:
        form = QuestionForm(instance=question)
        messages.info(request, f'You are editing {question.question}')

    template = 'edit_faq.html'
    context = {
        'form': form,
        'question': question,
    }

    return render(request, template, context)
