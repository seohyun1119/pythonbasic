from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question
from django.http import HttpResponseNotAllowed
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator 
# from django.http import HttpResponse

def index(request):
    # return HttpResponse("안녕하세요. board의 index 페이지입니다.")
    page = request.GET.get('page', '1')  # 페이지
    question_list = Question.objects.order_by('-created_at')
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기 
    page_obj = paginator.get_page(page) 
    context = {'question_list':page_obj}
    return render(request, 'board/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id) # Question.objects.get(id=question_id)
    context = {'question':question}
    return render(request, 'board/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # question.answer_set.create(content=request.POST.get('content'), created_at=timezone.now())
    # answer = Answer(question=question, content=request.POST.get('content'), created_at=timezone.now())
    # answer.save()
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.created_at = timezone.now()
            answer.question = question
            answer.save()
            return redirect('board:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question':question, 'form':form}
    return render(request, 'board/question_detail.html', context)

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.created_at = timezone.now()
            question.save()
            return redirect('board:index')
    else:
        form = QuestionForm()
    context = {'form':form}
    return render(request, 'board/question_form.html', context)