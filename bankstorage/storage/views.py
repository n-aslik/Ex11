from .models import  Userlogin,Incoming,Storage,Outcoming,Branch,Branch_access
from .forms import userpageform,incomingform,outcomingform,branchform,branch_accessform,loginform,storeform,report_searchform
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404,HttpResponse,HttpResponseNotFound
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login,logout
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from django.contrib.auth.decorators import login_required,permission_required
from django.db import connection
from django.contrib import messages

#User#
def user_list (request):
    data1=Userlogin.objects.all()
    return render(request,'user_list.html',{'data1':data1})

def user_update(request,id):
    users=Userlogin.objects.all()
    user=get_object_or_404(Userlogin,id=id)
    form=userpageform(request.POST, instance=user)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            return redirect('user_list')
        
    else:
        initial_data={
            'Fio':user.Fio,
            'pos':user.pos,
            'Tel':user.Tel,
            'rol':user.rol
            }
    form=userpageform(initial=initial_data)
    context={'form': form,'users':users}
    return render(request,'user_form.html',context)

def user_delete(request,id):
    instance=get_object_or_404(Userlogin,id=id)
    instance.delete()
    return redirect('user_list')
##########################################################



def my_custom_update1():
    with connection.cursor() as cursor:
        cursor.execute('''UPDATE storage_incoming,storage_outcoming SET Counti = IF(Counti>=0,IF(Counti>=storage_outcoming.Counto,Counti-storage_outcoming.Counto,Counti),0) WHERE storage_incoming.id>=1 and storage_incoming.id = storage_outcoming.inc_id;
                          ''')
        # Если вы хотите сохранить изменения в базе данных, не забудьте вызвать метод commit()
        connection.commit()

def my_custom_update2():
    with connection.cursor() as cursor:
        cursor.execute('''UPDATE storage_outcoming,storage_incoming SET Counto = IF(Counto>=0,IF(Counto <= storage_incoming.Counti,Counto,0),0) WHERE storage_outcoming.id>=1 and storage_outcoming.inc_id=storage_incoming.id;
                          ''')
        # Если вы хотите сохранить изменения в базе данных, не забудьте вызвать метод commit()
        connection.commit()
        



#Incoming#
def incoming_list (request):
    my_custom_update1()
    if request.user.rol in [1,2] or request.user.is_superuser==1:
        if  request.user.id>1:
            data2=Incoming.objects.filter(user__gt=1)
            return render(request,'incoming_list.html',{'data2':data2})
        else:
            data2=Incoming.objects.all()
            return render(request,'incoming_list.html',{'data2':data2})
    elif request.user.rol not in [1,2]:
        data2=Incoming.objects.filter(user=request.user)
        return render(request,'incoming_list.html',{'data2':data2})


def incoming_create(request):
    if request.method=='POST':
        form=incomingform(request.POST )
        if form.is_valid():
            if form.instance.Counti<0:
                pass
            else:
                form.save()
                return redirect('incoming_list')
    else:
        form=incomingform()
        if request.user.rol  in [1, 2] or request.user.is_superuser==1 :
            if request.user.id >1:
                form.fields['user'].queryset=Userlogin.objects.filter(id__gt=1)
                form.fields['store'].queryset=Storage.objects.filter(user=request.user)
            else:
                form.fields['user'].queryset=Userlogin.objects.all()
                form.fields['store'].queryset=Storage.objects.filter(user=request.user)
        elif request.user.rol not in [1,2]:
            form.fields['user'].queryset=Userlogin.objects.filter(Fio=request.user)
            form.fields['store'].queryset=Storage.objects.filter(user=request.user) 
        else:
            form.fields['user'].queryset=Userlogin.objects.all()
            form.fields['store'].queryset=Storage.objects.all()
    return render(request,'incoming_form.html',{'form':form})

def incoming_update(request,id):
    incomes=Incoming.objects.all()
    income=get_object_or_404(Incoming,id=id)
    form=incomingform(request.POST, instance=income)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            return redirect('incoming_list')
    else:
        initial_data1={
            'iname':income.iname,
            'Counti':income.Counti,
            'incoming_date':income.incoming_date,
            'Recipient':income.Recipient,
            'store':income.store,
            'user':income.user

            }
    form=incomingform(initial=initial_data1)
    context={'form':form,'income':income}
    if request.user.rol  in [1, 2] or request.user.is_superuser==1 :
        if request.user.id >1:
            form.fields['user'].queryset=Userlogin.objects.filter(id__gt=1)
            form.fields['store'].queryset=Storage.objects.filter(user=request.user)
        else:
            form.fields['user'].queryset=Userlogin.objects.all()
            form.fields['store'].queryset=Storage.objects.filter(user=request.user)
    elif request.user.rol not in [1,2]:
        form.fields['user'].queryset=Userlogin.objects.filter(Fio=request.user)
        form.fields['store'].queryset=Storage.objects.filter(user=request.user) 
    else:
        form.fields['user'].queryset=Userlogin.objects.all()
        form.fields['store'].queryset=Storage.objects.all()
    return render(request,'incoming_form.html',context)

def incoming_delete(request,id):
    instance=get_object_or_404(Incoming,id=id)
    instance.delete()
    return redirect('incoming_list')
##########################################################

#Outcoming#

def outcoming_list (request):
    my_custom_update2()
    if request.user.rol in [1,2] or request.user.is_superuser==1:
        if request.user.id>1:
            data3=Outcoming.objects.filter(user__gt=1)
            return render(request,'outcoming_list.html',{'data3':data3})
        else:
            data3=Outcoming.objects.all()
            return render(request,'outcoming_list.html',{'data3':data3})
    elif request.user.rol not in [1,2]:
        data3=Outcoming.objects.filter(user=request.user)
        return render(request,'outcoming_list.html',{'data3':data3})

def outcoming_create(request):
    if request.method=='POST':
        form=outcomingform(request.POST )
        if form.is_valid():
            if form.instance.Counto<0:
                pass
            else:
                form.save()
                return redirect('outcoming_list')
    else:
        form=outcomingform()
        if request.user.rol  in [1, 2] or request.user.is_superuser==1 :
            if request.user.id >1:
                form.fields['user'].queryset=Userlogin.objects.filter(id__gt=1)
                form.fields['store'].queryset=Storage.objects.filter(user=request.user)
            else:
                form.fields['user'].queryset=Userlogin.objects.all()
                form.fields['store'].queryset=Storage.objects.filter(user=request.user)
                

        elif request.user.rol not in [1,2]:
            form.fields['user'].queryset=Userlogin.objects.filter(Fio=request.user)
            form.fields['store'].queryset=Storage.objects.filter(user=request.user)
            
        else:
            form.fields['user'].queryset=Userlogin.objects.all()
            form.fields['store'].queryset=Storage.objects.all()
            

    return render(request,'outcoming_form.html',{'form':form})

def outcoming_update(request,id):
    outcomes=Outcoming.objects.all()
    outcome=get_object_or_404(Outcoming,id=id)
    form=outcomingform(request.POST , instance=outcome)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('outcoming_list')
    else:
        initial_data2={
        'inc':outcome.inc,
        'Counto':outcome.Counto,
        'Recipient':outcome.Recipient,
        'outcoming_date':outcome.outcoming_date,
        'store':outcome.store,
        'user':outcome.user
        
            }
    form=outcomingform(initial=initial_data2)
    context={'form':form,'outcome':outcome}
    if request.user.rol  in [1, 2] or request.user.is_superuser==1 :
        if request.user.id >1:
            form.fields['user'].queryset=Userlogin.objects.filter(id__gt=1)
            form.fields['store'].queryset=Storage.objects.filter(user=request.user)
        else:
            form.fields['user'].queryset=Userlogin.objects.all()
            form.fields['store'].queryset=Storage.objects.filter(user=request.user)
                
    elif request.user.rol not in [1,2]:
        form.fields['user'].queryset=Userlogin.objects.filter(Fio=request.user)
        form.fields['store'].queryset=Storage.objects.filter(user=request.user)
            
    else:
        form.fields['user'].queryset=Userlogin.objects.all()
        form.fields['store'].queryset=Storage.objects.all()
    return render(request,'outcoming_form.html',{'form':form})

def outcoming_delete(request,id):
    instance=get_object_or_404(Outcoming,id=id)
    instance.delete()
    return redirect('outcoming_list')
##########################################################

    
#Storage#
def storage_list (request):
    if request.user.rol in [1,2] or request.user.is_superuser==1:
        if  request.user.id>1:
            data6=Storage.objects.filter(user__gt=1)
            return render(request,'storage_list.html',{'data6':data6})
        else:
            data6=Storage.objects.all()
            return render(request,'storage_list.html',{'data6':data6})
    elif request.user.rol not in [1,2]:
        data6=Storage.objects.filter(user=request.user)
        b_a=Branch_access.objects.get(user=3)
        new_s=Storage.objects.filter(user=3)
        for s in new_s:
            s.sname=b_a.store.sname
            s.branch=b_a.store.branch
            s.save()
        data6=new_s
        return render(request,'storage_list.html',{'data6':data6})
    
    

def storage_create(request):
    form=storeform(request.POST)
    if form.is_valid():
        form.save()
        return redirect('storage_list')
    else:
        form=storeform()
        if request.user.rol  in [1, 2] or request.user.is_superuser==1 :
            if request.user.id >1:
                form.fields['user'].queryset=Userlogin.objects.filter(id__gt=1)
                form.fields['sname'].queryset=Storage.objects.filter(user=request.user)
                form.fields['branch'].queryset=Branch.objects.filter(user=request.user)
            else:
                form.fields['user'].queryset=Userlogin.objects.all()
                form.fields['sname'].queryset=Storage.objects.filter(user=request.user)
                form.fields['branch'].queryset=Branch.objects.filter(user=request.user)

        elif request.user.rol not in [1,2]:
            form.fields['user'].queryset=Userlogin.objects.filter(Fio=request.user)
            form.fields['sname'].queryset=Storage.objects.filter(user=request.user)
            form.fields['branch'].queryset=Branch.objects.filter(user=request.user)
        else:
            form.fields['user'].queryset=Userlogin.objects.all()
            form.fields['sname'].queryset=Storage.objects.all()
            form.fields['branch'].queryset=Branch.objects.all()

    return render(request,'storage_form.html',{'form':form})

def storage_update(request,id):
    stors=Storage.objects.all()
    stor=get_object_or_404(Storage,id=id)
    form=storeform(request.POST , instance=stor)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('storage_list')
    else:
        initial_data3={
            'sname':stor.sname,
            'user':stor.user
            }
    form=storeform(initial=initial_data3)
    context={'form':form,'stor':stor}
    if request.user.rol  in [1, 2] or request.user.is_superuser==1 :
        if request.user.id >1:
            form.fields['user'].queryset=Userlogin.objects.filter(id__gt=1)
            form.fields['sname'].queryset=Storage.objects.filter(user=request.user)
            form.fields['branch'].queryset=Branch.objects.filter(user=request.user)
        else:
            form.fields['user'].queryset=Userlogin.objects.all()
            form.fields['sname'].queryset=Storage.objects.filter(user=request.user)
            form.fields['branch'].queryset=Branch.objects.filter(user=request.user)

    elif request.user.rol not in [1,2]:
        form.fields['user'].queryset=Userlogin.objects.filter(Fio=request.user)
        form.fields['sname'].queryset=Storage.objects.filter(user=request.user)
        form.fields['branch'].queryset=Branch.objects.filter(user=request.user)
    else:
        form.fields['user'].queryset=Userlogin.objects.all()
        form.fields['sname'].queryset=Storage.objects.all()
        form.fields['branch'].queryset=Branch.objects.all()

    return render(request,'storage_form.html',context)

def storage_delete(request,id):
    instance=get_object_or_404(Storage,id=id)
    instance.delete()
    return redirect('storage_list')

#########################################################################################
#Branch#
def branch_list (request):
    if request.user.rol in [1,2] or request.user.is_superuser==1:
        if  request.user.id>1:
            data4=Branch.objects.filter(user__gt=1)
            return render(request,'branch_list.html',{'data4':data4})
        else:
            data4=Branch.objects.all()
            return render(request,'branch_list.html',{'data4':data4})
    elif request.user.rol not in [1,2]:
        data4=Branch.objects.filter(user=request.user)
        b_a=Branch_access.objects.get(user=3)
        new_b=Branch.objects.filter(user=3)
        for b in new_b:
            b.bname=b_a.branch.bname
            b.Address=b_a.branch.Address
            b.save()
        data4=new_b
        return render(request,'branch_list.html',{'data4':data4})

def branch_create(request):
    form=branchform(request.POST)
    if form.is_valid():
        form.save()
        return redirect('branch_list')
    else:
        form=branchform()    
        if request.user.rol  in [1, 2] or request.user.is_superuser==1 :
            if request.user.id >1:
                form.fields['user'].queryset=Userlogin.objects.filter(id__gt=1)
                form.fields['bname'].queryset=Branch.objects.filter(user=request.user)
            else:
                form.fields['user'].queryset=Userlogin.objects.all()
                form.fields['bname'].queryset=Branch.objects.filter(user=request.user)
        elif request.user.rol not in [1,2] :
            form.fields['user'].queryset=Userlogin.objects.filter(Fio=request.user)
            form.fields['bname'].queryset=Branch.objects.filter(user=request.user)
        else:
            form.fields['user'].queryset=Userlogin.objects.all()
            form.fields['bname'].queryset=Branch.objects.all()

    return render(request,'branch_form.html',{'form':form})

def branch_update(request,id):
    brancs=Branch.objects.all()
    branc=get_object_or_404(Branch,id=id)
    form=branchform(request.POST , instance=branc)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('branch_list')
    else:
        initial_data4={
            'Address':branc.Address,
            'bname':branc.bname,
            'user':branc.user
            }
    form=branchform(initial=initial_data4)
    context={'form':form,'branc':branc}
    if request.user.rol  in [1, 2] or request.user.is_superuser==1 :
        if request.user.id >1:
            form.fields['user'].queryset=Userlogin.objects.filter(id__gt=1)
            form.fields['bname'].queryset=Branch.objects.filter(user=request.user)
        else:
            form.fields['user'].queryset=Userlogin.objects.all()
            form.fields['bname'].queryset=Branch.objects.filter(user=request.user)
    elif request.user.rol not in [1,2] :
        form.fields['user'].queryset=Userlogin.objects.filter(Fio=request.user)
        form.fields['bname'].queryset=Branch.objects.filter(user=request.user)
    else:
        form.fields['user'].queryset=Userlogin.objects.all()
        form.fields['bname'].queryset=Branch.objects.all()

    return render(request,'branch_form.html',context)

def branch_delete(request,id):
    instance=get_object_or_404(Branch,id=id)
    instance.delete()
    return redirect('branch_list')

##########################################################
#Branch_access#
def branch_access_list (request):
    if request.user.rol in [1,2] or request.user.is_superuser==1:
        if  request.user.id > 1:
            data5=Branch_access.objects.filter(user__gt=1)
            return render(request,'branch_access_list.html',{'data5':data5})
        else:
            data5=Branch_access.objects.all()
            return render(request,'branch_access_list.html',{'data5':data5})
    elif request.user.rol not in [1,2]:
        data5=Branch_access.objects.filter(user=request.user)
        return render(request,'branch_access_list.html',{'data5':data5})
    
# @permission_required('storage.can_view_page')
def branch_access_create(request):
    if request.method=='POST':
        form=branch_accessform(request.POST)
        if form.is_valid:
            form.save()
            return redirect('branch_access_list')
    else:
        form=branch_accessform()
        if request.user.rol  in [1,2] or request.user.is_superuser==1:
            if request.user.id > 1:
                form.fields['user'].queryset=Userlogin.objects.filter(id__gt=1)
                form.fields['store'].queryset=Storage.objects.filter(user=request.user)
                form.fields['branch'].queryset=Branch.objects.filter(user=request.user)
            else:
                form.fields['user'].queryset=Userlogin.objects.all()
                form.fields['store'].queryset=Storage.objects.filter(user=request.user)
                form.fields['branch'].queryset=Branch.objects.filter(user=request.user)

        elif request.user.rol not in [1,2] :
            form.fields['user'].queryset=Userlogin.objects.filter(Fio=request.user)
            form.fields['store'].queryset=Storage.objects.filter(user=request.user)
            form.fields['branch'].queryset=Branch.objects.filter(user=request.user)
        else:
            form.fields['user'].queryset=Userlogin.objects.all()
            form.fields['store'].queryset=Storage.objects.filter(user=request.user)
            form.fields['branch'].queryset=Branch.objects.all()
    context={'form':form}
    return render(request,'branch_access_form.html',context)

def branch_access_update(request,id):
    bran_a=Branch_access.objects.all()
    bran=get_object_or_404(Branch_access,id=id)
    form=branch_accessform(request.POST , instance=bran)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('branch_access_list')
    else:
        initial_data5={
            'branch':bran.branch,
            'user':bran.user,
            'store':bran.store
            }
    form=branch_accessform(initial=initial_data5)
    context={'form':form,'bran':bran}
    if request.user.rol  in [1, 2] or request.user.is_superuser==1 :
        if request.user.id >1 :
            form.fields['user'].queryset=Userlogin.objects.filter(id__gt=1)
            form.fields['store'].queryset=Storage.objects.filter(user=request.user)
            form.fields['branch'].queryset=Branch.objects.filter(user=request.user)
        else:
            form.fields['user'].queryset=Userlogin.objects.all()
            form.fields['store'].queryset=Storage.objects.filter(user=request.user)
            form.fields['branch'].queryset=Branch.objects.filter(user=request.user)

    elif request.user.rol not in [1,2] :
        form.fields['user'].queryset=Userlogin.objects.filter(Fio=request.user)
        form.fields['store'].queryset=Storage.objects.filter(user=request.user)
        form.fields['branch'].queryset=Branch.objects.filter(user=request.user)
    else:
        form.fields['user'].queryset=Userlogin.objects.all()
        form.fields['store'].queryset=Storage.objects.all()
        form.fields['branch'].queryset=Branch.objects.all()
    
    return render(request,'branch_access_form.html',context)

def branch_access_delete(request,id):
    instance=get_object_or_404(Branch_access,id=id)
    instance.delete()
    return redirect('branch_access_list')
##############################################################
#HOME#
@login_required(login_url='')
def home (request):
    user = request.user
    return render(request, 'home.html', {'user': user})



def logout_view(request):
    logout(request)
    return redirect('/')



def login_view(request):
    if request.method=="POST":
        form=loginform(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('home')
        else:
            messages.warning(request,"Такого пользователя несуществует!")
            return render (request,'login.html',{'message':"Такого пользователя несуществует!"})
    else:
        form=loginform(request)
        return render(request,'login.html',{'form':form})
    

def reestr(request):
    results_i=[]
    results_o=[]
    if request.method=='GET':
        form=report_searchform(request.GET)
        if form.is_valid():
            query_b=form.cleaned_data.get('query_b')
            query_ds=form.cleaned_data.get('query_ds')
            query_de=form.cleaned_data.get('query_de')
            if request.user.rol  in [1, 2] or request.user.is_superuser==1 :
                if request.user.id >1 :
                    results_i=Incoming.objects.filter(Q(store__branch__bname__contains=query_b) & Q(incoming_date__range=(query_ds,query_de)) & Q(user__in=[2,3])).order_by('incoming_date')
                    results_o=Outcoming.objects.filter(Q(store__branch__bname__contains=query_b) & Q(inc__incoming_date__range=(query_ds,query_de)) & Q(user__in=[2,3])).order_by('incoming_date')
                    return render(request,'reestr_list.html',{'form':form,'results_i': results_i,'results_o': results_o})
                else:
                    results_i=Incoming.objects.filter(Q(store__branch__bname__contains=query_b) & Q(incoming_date__range=(query_ds,query_de))& Q(user__in=[1,3])).order_by('incoming_date')
                    results_o=Outcoming.objects.filter(Q(store__branch__bname__contains=query_b) & Q(inc__incoming_date__range=(query_ds,query_de))& Q(user__in=[1,3])).order_by('inc__incoming_date')
                    return render(request,'reestr_list.html',{'form':form,'results_i': results_i,'results_o': results_o})
            elif request.user.rol not in [1,2] :
                results_i=Incoming.objects.filter(Q(store__branch__bname__contains=query_b) & Q(incoming_date__range=(query_ds,query_de))& Q(user=3)).order_by('incoming_date')
                results_o=Outcoming.objects.filter(Q(store__branch__bname__contains=query_b) & Q(inc__incoming_date__range=(query_ds,query_de))& Q(user=3)).order_by('inc__incoming_date')
                return render(request,'reestr_list.html',{'form':form,'results_i': results_i,'results_o': results_o})
            else:
                results_i=Incoming.objects.filter(Q(store__branch__bname__contains=query_b) & Q(incoming_date__range=(query_ds,query_de))& Q(user__in=[1,3])).order_by('incoming_date')
                results_o=Outcoming.objects.filter(Q(store__branch__bname__contains=query_b) & Q(inc__incoming_date__range=(query_ds,query_de))& Q(user__in=[1,3])).order_by('inc__incoming_date')
            return render(request,'reestr_list.html',{'form':form,'results_i': results_i,'results_o': results_o})
    else:
        form=report_searchform()
    return render(request,'reestr_list.html',{'form':form,'results_i': results_i,'results_o': results_o})
    


    

        
##########################################################################################################################################################################
#SEARCH_DATA#
class UserSearchResultsView(ListView):
    model = Userlogin
    template_name = 'user_search.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Userlogin.objects.all().filter(Q(Fio__icontains=query) | Q(pos__pname__icontains=query) | Q(Tel__icontains=query) | Q(rol__rname__icontains=query) | Q(username__icontains=query))
        return object_list
class IncomingSearchResultsView(ListView):
    model = Incoming
    template_name = 'incoming_search.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Incoming.objects.all().filter(Q(iname__icontains=query) | Q(Counti__icontains=query) | Q(incoming_date__icontains=query)  | Q(store__sname__icontains=query))
        return object_list

class OutcomingSearchResultsView(ListView):
    model = Outcoming
    template_name = 'outcoming_search.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Outcoming.objects.all().filter(Q(inc__iname__icontains=query) | Q(Counto__icontains=query)  | Q(Recipient__icontains=query) | Q(outcoming_date__icontains=query)| Q(store__sname__icontains=query))
        return object_list

class BranchSearchResultsView(ListView):
    model = Branch
    template_name = 'branch_search.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Branch.objects.all().filter(Q(Address__icontains=query) | Q(bname__icontains=query))
        return object_list

class BranchAccessSearchResultsView(ListView):
    model = Branch_access
    template_name = 'branch_access_search.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Branch_access.objects.all().filter(Q(user__Fio__icontains=query) | Q(branch__bname__icontains=query)|Q(store__sname__icontains=query))
        return object_list

class StorageSearchResultsView(ListView):
    model = Storage
    template_name = 'storage_search.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Storage.objects.all().filter(Q(sname__icontains=query))
        return object_list


       

    


