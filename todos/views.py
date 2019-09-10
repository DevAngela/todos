from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todos/index.html', context)

def new(request):
    return render(request, 'todos/new.html')

def create(request):
    # 대문자 POST로 써서 POST방식으로 얻은 데이터 가져오기
    # 이 데이터는 Query Dict로 되어 있으니 dictionary.get으로 딕셔너리 정보 가져오기
    title = request.POST.get('title')
    due_date = request.POST.get('due-date') # -와 _ 구분 잘 하기
    
    Todo.objects.create(title=title, due_date=due_date)

    return redirect('todos:index')
    
def edit(request, pk):
    todo = Todo.objects.get(id=pk)
    context = {
        'todo': todo
    }
    return render(request, 'todos/edit.html', context)

def update(request, pk):
    # 새로 수정된 정보 가져오기
    title = request.POST.get('title')
    due_date = request.POST.get('due-date')
    
    # 기존 정보 가져오고 새 정보로 바꿔주기
    todo = Todo.objects.get(id=pk)
    todo.title = title
    todo.due_date = due_date
    todo.save()
    return redirect('todos:index')

def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()

    return redirect('todos:index')