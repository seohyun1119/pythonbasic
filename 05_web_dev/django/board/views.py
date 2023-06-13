from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer
# from django.http import HttpResponse

def index(request):
    # return HttpResponse("안녕하세요. board의 index 페이지입니다.")
    question_list = Question.objects.order_by('-created_at')
    context = {'question_list':question_list}
    return render(request, 'board/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id) # Question.objects.get(id=question_id)
    context = {'question':question}
    return render(request, 'board/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # question.answer_set.create(content=request.POST.get('content'), created_at=timezone.now())
    answer = Answer(question=question, content=request.POST.get('content'), created_at=timezone.now())
    answer.save()
    return redirect('board:detail', question_id=question.id)