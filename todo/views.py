from django.shortcuts import render
from .models import Todo,Tag
from django.http import JsonResponse

def read_todo(request):
    db_todo=Todo.objects.all()

    res=[]
    for todo in db_todo:
        db_tag=Tag.objects.filter(todo__pk=todo.pk)
        t=[]
        for i in db_tag:
            t.append(i.name)
        res.append(
            {
                "Title":todo.title,
                "Completed":todo.completed,
                "user":{
                    "UserName":todo.user.user_name,
                    "Name":todo.user.first_name+""+todo.user.last_name,
                    "Age":todo.user.age
                },
                "Tags":t,
            }
        )
        
    return JsonResponse(res,safe=False)
        