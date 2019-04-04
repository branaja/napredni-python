from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.utils.timezone import now
from django.http import Http404

from tasks.models import Task
from tasks.forms import TaskForm, TaskModelForm

class IndexView(View):

    def get(self, request, *args, **kwargs):
        context = {
            'current_time': now(),
        }
        return render(request, 'tasks/index.html', context=context)


class TaskListView(View):

    def get(self, request, *args, **kwargs):
        context = {
            'task_list': Task.objects.all()
        }
        return render(request, 'tasks/task_list.html', context=context)


class TaskDetailsView(View):

    def get(self, request, task_id):
        try:
            context = {
                'task_id': task_id,
                'task': Task.objects.get(id=task_id)
            }
            return render(request, 'tasks/task_details.html', context=context)
        except Task.DoesNotExist:
            raise Http404('Task does not exist')




class TaskEditView(View):

    def get(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            raise Http404('Task does not exist')

        form = TaskModelForm(instance=task)
        context = {
            'task': task,
            'form': form
        }
        return render(request, 'tasks/task_edit.html', context=context)

    def post(self, request, task_id):

        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            raise Http404('Task does not exist')

        form = TaskModelForm(request.POST, instance=task)
        if form.is_valid():

            form.save()
            return HttpResponseRedirect(reverse('list'))

        context = {
            'form': form,
            'task': task
        }
        return render(request, 'tasks/task_edit.html', context=context)


class TaskDeleteView(View):

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'tasks/task_delete.html', context=context)


class TaskAddView(View):
    def get(self, request):
        form = TaskModelForm()
        context = {
            'form': form
        }
        return render(request, 'tasks/task_add.html', context=context)

    def post(self, request):
        form = TaskModelForm(request.POST)
        if form.is_valid():

            form.save()
            return HttpResponseRedirect(reverse('list'))

        context = {
            'form': form,
        }
        return render(request, 'tasks/task_edit.html', context=context)