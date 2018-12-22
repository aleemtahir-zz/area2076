from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse
from area2076.models import User
from api.models import Task
import json

def index(request):  
    default_user = User.objects.get(id=2)
    context = {'user': default_user}

    return render(request, 'area2076/index.html', context)
   

def profile(request):  
    current_user = request.user
    tasks = Task.objects.filter(user=current_user.id)#.order_by('-id')[:5]

    page = request.GET.get('page', 1)
    paginator = Paginator(tasks, 5)
    
    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(paginator.num_pages)
    context = {'user': current_user, 'tasks': tasks}
    # return HttpResponse(json.dumps(current_user.role), content_type='application/json')
    # if current_user.role == 'SR':
    #     url = ''
    # elif current_user.role == 'SO':
    #     url = ''
    # elif current_user.role == 'AM':
    #     url = ''

    return render(request, 'area2076/profile.html', context)