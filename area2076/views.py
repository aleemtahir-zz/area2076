from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from area2076.models import User
from api.models import Task
import json

def index(request):  
    default_user = User.objects.get(id=1)
    context = {'user': default_user}

    return render(request, 'area2076/index2.html', context)
   

def profile(request):  
    current_user = request.user
    if not current_user.is_authenticated:
        return HttpResponseRedirect('/accounts/login')

    c = current_user.get_descendants(include_self=True)
    # print(c.values('code'))    
    tasks = Task.objects.filter(user__in=c).order_by('-id')

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