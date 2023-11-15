from django.shortcuts import render
from django.core.paginator import Paginator

TAGS = [
        {
            'id': i,
            'title': f'Tag {i}',
        } for i in range(100)
    ]

QUESTIONS = [
        {
            'id': i,
            'title': f'Question {i}',
            'content': f'Long lorem ipsum {i}',
            'tags': TAGS[i]
        } for i in range(40)
    ]

HOT_QUESTIONS = QUESTIONS [:-5]

ANSWERS = [
        {
            'id': i,
            'content': f'Content of this answer {i}',
            #correct = true/false?
        } for i in range(10)
    ]

def paginate(objects, page, per_page=10):
    paginator = Paginator(objects, per_page)

    #page_item = paginator.page(1).object_list

    #возвращаем нужную страницу (со всей инфой)
    return paginator.page(page)


# Create your views here.
def index(request):
    page = request.GET.get('page', 1)
    return render(request, 'index.html', {'objects': paginate(QUESTIONS, page)})

def hot_questions(request):
    page = request.GET.get('page', 1)
    return render(request, 'hot_questions.html', {'objects': paginate(HOT_QUESTIONS, page)})

def question(request, question_id):
    item = QUESTIONS[question_id]
    page = request.GET.get('page', 1)
    return render(request, 'question.html', {'question': item, 'objects': paginate(ANSWERS, page, 3)})

def ask(request):
    return render(request, 'ask.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def settings(request):
    return render(request, 'settings.html')

def tag(request, tag_id):
    item = TAGS[tag_id]
    page = request.GET.get('page', 1)
    #надо будет выбирать вопросы, которые соответствуют тэгу. сейчас просто буду водить все
    return render(request, 'tag.html', {'tag': item, 'objects': paginate(QUESTIONS, page)})
