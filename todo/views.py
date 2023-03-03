from ast import If
from django.shortcuts import render,redirect,get_object_or_404

from todo.forms import TodoForm
from todo.models import Todo

# Create your views here.
def home(req):
    if not req.user.is_authenticated: 
        return redirect('userlogin')
    if req.method == "GET":
        return render(req,'home.html',{'form':TodoForm,'Todos':Todo.objects.filter(user=req.user)})
    else:
        form = TodoForm(req.POST)
        mytodo = form.save(commit = False)
        mytodo.user= req.user
        mytodo.save()
        return redirect('home')
    
def delete(req,id):
    todo = get_object_or_404(Todo,pk=id,user=req.user)
    todo.delete()
    return redirect('home')

