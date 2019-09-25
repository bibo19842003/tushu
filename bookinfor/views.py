from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader, Context
from django.contrib.auth.decorators import login_required
from bookinfor.models import Bookinfor, Consume, Bookmember, Inoutrecord
import time
import os


# --- index begin ---

def index(request):
  return render(request, 'index.html')
#  return HttpResponse("xxxxxxxxxxxxxxxxxxxxxxxxx")

# --- index end ---



# --- member begin ---

def memberlogfile(runuser, phone, membername, account, mail, expir, card, remark):
  t = time.strftime("%Y-%m-%d-%H-%M-%S")
  filename = "member-" + t + "-" + runuser + "-" + phone + ".txt"
  BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  memberlog = os.path.join(BASE_DIR, 'static/log/member', filename)
  with open(memberlog, 'a+') as f:
    f.write(time.strftime("%Y-%m-%d %H:%M:%S"))
    f.write('\n')
    f.write(' runuser: %s \n phone: %s \n membername: %s \n account: %s \n mail: %s \n expir: %s \n card: %s \n remark: %s \n' %(runuser, phone, membername, account, mail, expir, card, remark))



@login_required
def member_query(request):

  if request.GET.get('phone') == None:
      return render(request, 'bookinfor/bookmember/bookmember_query.html')

  phone = request.GET.get('phone')

  member = Bookmember.objects.filter(phone__icontains=phone)

  return render(request, 'bookinfor/bookmember/bookmember_query.html', {'member': member,})



@login_required
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

    member = Bookmember.objects.filter(phone=phone)

    memberlogfile(runuser, phone, membername, account, mail, expir, card, remark)

    return render(request, 'bookinfor/bookmember/member_modify_ok.html', {'member': member,})



def member_log(request):

  BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  memberlogdir = os.path.join(BASE_DIR, 'static/log/member')
  filename = os.listdir(memberlogdir)
  filename.sort(reverse=True)

  return render(request, 'bookinfor/bookmember/member_log.html', {'filename': filename,})


# --- member end ---



# --- book begin ---

def book_query(request):

  if request.GET.get('bookname') == None:
      return render(request, 'bookinfor/bookinfor/book_query.html')

  bookname = request.GET.get('bookname')

  bookinfor = Bookinfor.objects.filter(book_name__icontains=bookname)

  return render(request, 'bookinfor/bookinfor/book_query.html', {'bookinfor': bookinfor,})


# --- book end ---




# --- consume begin ---

@login_required
def deal_query(request):

  consume = Consume.objects.all()

  return render(request, 'bookinfor/consume/deal_query.html', {'consume': consume,})











# --- consume end ---





# --- in out begin ---

def inout_query(request):

  inout = Inoutrecord.objects.all()

  return render(request, 'bookinfor/inoutrecord/inout_query.html', {'inout': inout,})












# --- in out end ---


