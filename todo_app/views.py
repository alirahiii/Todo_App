import json
from django.db import models

from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import *




# Create your views here.





@csrf_exempt
def todo_list(request):
    if request.method == "GET":
        query_set = Todo.objects.all()
        result = []
        for data in query_set:
            result.append({
                "title": data.title,
                "due_date": data.due_date
            })

        return JsonResponse({"status": "successful", "data": result})
    else:
        return JsonResponse({"status": "error", "msg": "faghat get mojazeh"}, status=403)



def todo_detail(request, id):
    if request.method == "GET":
        todo_object = get_object_or_404(Todo, pk=id)
        result = {
            "title": todo_object.title,
            "due_date": todo_object.due_date,
            "created_date": todo_object.created_date
        }
        return JsonResponse({"status": "successful", "data": result})
    else:
        return JsonResponse({"status": "error", "msg": "faghat get mojazeh"}, status=403)

@csrf_exempt
def todo_create(request):
    if request.method == "POST":
        data = json.loads(request.body)
        if "title" not in data or "due_date" not in data:
            return JsonResponse({"status": "error", "msg": "shalgham sholagh title va due_date ro bede"}, status=403)
        title = data.get("title", "")
        due_date = data.get("due_date", "")
        Todo.objects.create(title=title, due_date=due_date)
        return JsonResponse({"status": "successful", "msg": "ba khubio khshi task crate shod"}, status=201)
        
    else:
        return JsonResponse({"status": "error", "msg": "faghat post mojazeh"}, status=403)


    
