from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    data = { 'latest_question_list': latest_question_list  }
    return render(request, 'polls/index.html', data)

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    data = { 'question': question }
    return render(request, 'polls/detail.html', data)

def results(request, question_id):
    return HttpResponse(f'Results page for question {question_id}')

def vote(request, question_id):
    return HttpResponse(f'Vote page for question {question_id}')