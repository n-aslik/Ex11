from .models import worker
from .forms import workerform,loginform
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404 
from django.views.generic import  ListView
from django.db.models import Q as q
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def worker_list (request):
    data=worker.objects.all()
    return render(request,'worker_list.html',{'data':data})


def worker_create(request):
    form=workerform(request.POST)
    if form.is_valid():
        form.save()
        return redirect('worker_list')
    return render(request,'worker_form.html',{'form':form})

def worker_update(request,id):
    works=worker.objects.all()
    work=get_object_or_404(worker,id=id)
    form=workerform(request.POST , instance=work)
    if form.is_valid():
        form.save()
        return redirect('worker_list')
    else:
        initial_data={
            'FIO':work.FIO,
            'work_number':work.work_number,
            'mobi_number':work.mobi_number,
            'email':work.email,
            'gen':work.gen,
            'struct':work.struct,
            'user':work.user
            }
        form=workerform(initial=initial_data)
        context={'work':work,'form':form}
    return render(request,'worker_form.html',context)

def worker_delete(request,id):
    instance=get_object_or_404(worker,id=id)
    instance.delete()
    return redirect('worker_list') 


def logout_v(request):
    logout(request)
    return redirect('login')

def login_v(request):
    if request.method=="POST":
        form=loginform(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('worker_list')
        else:
            messages.warning(request,"Такого пользователя несуществует")
            return render(request,'login.html',{'message':"Такого пользователя несуществует"})
    else:
        form=loginform()
        return render(request,'login.html',{'form':form})



 
class SearchResultsView(ListView):
    model = worker
    template_name = 'search.html'
    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = worker.objects.all().filter(q(FIO__icontains=query)| q(gen__polcnom__icontains=query)| q(work_number__icontains=query)| q(mobi_number__icontains=query)|q(email__icontains=query)| q(struct__structcnom__icontains=query))
        return object_list
    
         







  
    
    


   
