from django.shortcuts import render, get_object_or_404
from info.models import Faq
from info.models import Question


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def faq(request):

    subjects = Faq.objects.all()
    questions = Question.objects.all()

    return render(request, 'faq.html', {'subjects':subjects, 'questions':questions})
