from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from app.models import TaskManage
from app.models import Notes
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

class TaskView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(TaskView, self).dispatch(*args, **kwargs)

    def get(self, request):
        # data = serializers.serialize("json",, cls=LazyEncoder)
        print(request.GET)
        by = request.GET['by']
        data = []
        for row in TaskManage.objects.filter(assign_to=by):
            data.append({'taskname': row.task_name,'assign_by':row.assign_by,'assign_to':row.assign_to,'description':row.description})
        return JsonResponse( {'data':data})

    def post(self, request):
        print(request.body)
        data = json.loads(request.body)
        task_name = data['taskname']
        assign_by = data['assignby']
        assign_to = data['assignto']
        description = data['description']
        t=TaskManage(task_name=task_name,assign_by=assign_by,assign_to=assign_to,description=description)
        t.save()

        return HttpResponse(status=200)

class NotesView(View):   
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(NotesView, self).dispatch(*args, **kwargs)

    def get(self, request):
        print(request.GET)
        notesdata = []
        for row in Notes.objects.all():
            notesdata.append({'notes_title':row.title,'notes_content':row.content,'notes_todo':row.todo})
        return JsonResponse({'notesdata': notesdata})
      

    def post(self, request):
        print(request.body)
        data = json.loads(request.body)
        notes_title=data['title']
        notes_content=data['content']
        notes_todo=data['todo']
        n=Notes(title=notes_title,content=notes_content,todo=notes_todo)
        n.save()
        return HttpResponse(status=200)