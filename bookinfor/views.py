from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader, Context
from django.contrib.auth.decorators import login_required
from bookinfor.models import Bookinfor, Consume, Bookmember, Inoutrecord
import time


# Create your views here.

def index(request):
  return render(request, 'index.html')
#  return HttpResponse("xxxxxxxxxxxxxxxxxxxxxxxxx")

# @login_required
def book_query(request):

  bookinfor = Bookinfor.objects.all()

  return render(request, 'bookinfor/bookinfor/book_query.html', {'bookinfor': bookinfor,})




def deal_query(request):

  consume = Consume.objects.all()

  return render(request, 'bookinfor/consume/deal_query.html', {'consume': consume,})




def member_query(request):

  if request.GET.get('phone') == None:
      return render(request, 'bookinfor/bookmember/bookmember_query.html')

  phone = request.GET.get('phone')

  member = Bookmember.objects.filter(phone__icontains=phone)

  return render(request, 'bookinfor/bookmember/bookmember_query.html', {'member': member,})



def inout_query(request):

  inout = Inoutrecord.objects.all()

  return render(request, 'bookinfor/inoutrecord/inout_query.html', {'inout': inout,})


def member_manage(request):

    if request.GET.get('phone') == None:
      return render(request, 'bookinfor/bookmember/member_manage.html')

    phone = request.GET.get('phone')
    member = Bookmember.objects.filter(phone__icontains=phone)
    print('888888888888')

    return render(request, 'bookinfor/bookmember/member_manage.html', {'member': member,})



@login_required
def member_new(request):
    if request.POST.get('phone') == None:
      return render(request, 'bookinfor/bookmember/member_new.html')

    if request.POST.get('phone') =="" or request.GET.get('expir') == "":
      return render(request, 'bookinfor/bookmember/member_new.html')

    runuser =str(request.user)
    phone = request.POST.get('phone')
    membername = request.POST.get('membername')
    account = request.POST.get('account')
    mail = request.POST.get('mail')
    expir = request.POST.get('expir')
    card = request.POST.get('card')
    remark = request.POST.get('remark')

    print('1111110', request.POST.get('expir'), '22222')

    newmember = Bookmember(phone=phone, name=membername, account=account, mail=mail, expir=expir, card=card, handler=runuser, remark=remark)
    newmember.save()

    return render(request, 'bookinfor/bookmember/member_new_ok.html')



@login_required
def member_modify(request):

  if request.GET.get('phone') == None:
      return render(request, 'bookinfor/bookmember/member_manage.html')

  if "cx" in request.GET:
    phone = request.GET.get('phone')
    member = Bookmember.objects.filter(phone__icontains=phone)
    return render(request, 'bookinfor/bookmember/member_modify.html', {'member': member,})

  if "gx" in request.GET:
    runuser =str(request.user)
    phone = request.GET.get('phone')
    membername = request.GET.get('membername')
    account = request.GET.get('account')
    mail = request.GET.get('mail')
    expir = request.GET.get('expir')
    card = request.GET.get('card')
    remark = request.GET.get('remark')

    Bookmember.objects.filter(phone=phone).update(name=membername, account=account, mail=mail, expir=expir, card=card, handler=runuser, remark=remark)

    member = Bookmember.objects.filter(phone__icontains=phone)

    return render(request, 'bookinfor/bookmember/member_modify_ok.html', {'member': member,})




def filldata(request):    
    if request.is_ajax():  # filldata        
        onlineproblem_id= int(request.POST['IIID'])        
        content = OnlineProblem.objects.filter(id=onlineproblem_id)  
        #链接onlineproblem数据库，且以id=onlineproblem_id的值进行过滤      
        result = serializers.serialize("json", content)
        #获取所有的数据库数据
        #返回        
        return JsonResponse(result, safe=False)



