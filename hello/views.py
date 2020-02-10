from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import FriendForm
from .models import Friend
from django.db.models import QuerySet
from .forms import FindForm
from django.db.models import Count,Sum,Avg,Min,Max

def index(request):
    data = Friend.objects.all().order_by('age').reverse()
    re1 = Friend.objects.aggregate(Count('age'))
    msg = 'count:' + str(re1['age__count'])
    params = {
        'title':'Hello',
        'msg' : msg,
        'data': data,
        }
    return render(request,'hello/index.html',params)
    
def create(request):
    if (request.method == 'POST'):
        ojt = Friend()
        friend = FriendForm(request.POST,instance=ojt)
        friend.save()
        return redirect(to='/hello')
    params = {
            'title' : 'Hello',
            'form' :FriendForm(),
            }
    return render(request,'hello/create.html',params)

def edit(request,num):
    obj = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend = FriendForm(request.POST,instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
            'title': 'Hello',
            'id': num,
            'form':FriendForm(instance=obj),
            }
    return render(request,'hello/edit.html',params)

def delete(request,num):
    friend = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend.delete()
        return redirect(to='/hello')
    params = {
            'title': 'Hello',
            'id': num,
            'obj': friend,
            }
    return render(request,'hello/delete.html',params)
    
def find(request):
    if (request.method == 'POST'):
        msg = 'search result:'
        form = FindForm(request.POST)
        str = request.POST['find']
        list = str.split()
        data = Friend.objects.all()[int(list[0]):int(list[1])]
    else:
        msg = 'search words...'
        form = FindForm()
        data = Friend.objects.all()
    params = {
            'title': 'Hello',
            'message': msg,
            'form': form,
            'data': data,
            }
    return render(request,'hello/find.html',params)

