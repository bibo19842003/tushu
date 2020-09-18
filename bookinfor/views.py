from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader, Context
from django.contrib.auth.decorators import login_required
from bookinfor.models import Bookinfor, Consume, Bookmember, Inoutrecord, Author, Publish
import time
import os
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import requests, re
import sys
import urllib.error
import json
from django.http import JsonResponse


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
    remain = '0'

    newmember = Bookmember(phone=phone, name=membername, account=account, mail=mail, expir=expir, card=card, handler=runuser, remark=remark, remain=remain)
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


@login_required
def book_import(request):
  if request.POST.get('booklink') == None:
      return render(request, 'bookinfor/bookinfor/book_import.html')

  booklink = request.POST.get('booklink')

  headers = {
  'User-Agent':' Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/81.0.4044.138 Chrome/81.0.4044.138 Safari/537.36',
  }

  req = urllib.request.Request(url=booklink,headers=headers)

  try:
    res = urllib.request.urlopen(req)
  except urllib.request.URLError as e:
    return render(request, 'bookinfor/bookinfor/book_import_link_error.html')

  bsObj = BeautifulSoup(res, 'html.parser')

  tags = bsObj.find_all('div', class_="name_info")

  for tag in tags:
    bookname=tag.h1['title']

  author_info = bsObj.find_all('div', class_="messbox_info")
  for zuozhe in author_info:
    for zuozhe_name in zuozhe.span.contents[1]:
      author = zuozhe_name
    publisher = zuozhe.span.next_sibling.contents[1].contents[0]
    edition = zuozhe.span.next_sibling.next_sibling.contents[0]

  prices=str(bsObj.select("div#original-price"))
  price=str(prices.split("span>")[1]).split(" ")[0]

  details=str(bsObj.select("div#detail_describe"))
  size=details.split("<li>")[1]
  paper=details.split("<li>")[2]
  hardcover=details.split("<li>")[3]
  setset=details.split("<li>")[4]

  if 'cx' in request.POST:
    return render(request, 'bookinfor/bookinfor/book_import.html', {'bookname': bookname, 'booklink': booklink, 'author': author, 'publisher':publisher, 'edition':edition, 'price':price, 'size':size, 'paper':paper, 'hardcover':hardcover, 'setset':setset,})

  if 'importdata' in request.POST:
    if request.POST.get('bookname') =="" or request.POST.get('booklink') == "":
      return render(request, 'bookinfor/bookinfor/book_import.html')

    bookname = request.POST.get('bookname')
    booklink = request.POST.get('booklink')
    author = request.POST.get('author')
    publisher = request.POST.get('publisher')
    edition = request.POST.get('edition')
    price = request.POST.get('price')
    size = request.POST.get('size')
    paper = request.POST.get('paper')
    hardcover = request.POST.get('hardcover')
    setset = request.POST.get('setset')

    authorinfo = Author.objects.filter(chn_name = author)
    if not authorinfo.exists():
      print("new author, new author, new author")
      newauthor = Author(chn_name=author)
      newauthor.save()
    authorinfoupdate = Author.objects.get(chn_name = author)

    publishinfo = Publish.objects.filter(name = publisher)
    if not publishinfo.exists():
      print("new publisher, new publisher, new publisher")
      newpublisher = Publish(name = publisher)
      newpublisher.save()
    publishinfoupdate = Publish.objects.get(name = publisher)

    if hardcover == "精装":
      hardcoverchoice = "jingz"
    else:
      hardcoverchoice = "jianz"

    if setset == "是":
      setsetchoice = "s"
    else:
      setsetchoice = "f"

    newbookinfor = Bookinfor(book_name=bookname, book_link=booklink, author_text=authorinfoupdate, publisher=publishinfoupdate, edition=edition, price=price, size=size, hardcover=hardcoverchoice, book_paper=paper, setset=setsetchoice)
    newbookinfor.save()
    return render(request, 'bookinfor/bookinfor/book_import_ok.html', {'bookname': bookname, 'booklink': booklink, 'author': author, 'publisher':publisher, 'edition':edition, 'price':price, 'size':size, 'paper':paper, 'hardcover':hardcover, 'setset':setset,})



# --- book end ---



# --- consume begin ---

@login_required
def deal_query(request):

  if request.GET.get('phone') == None:
      return render(request, 'bookinfor/consume/deal_query.html')

  phone = request.GET.get('phone')

  consume = Consume.objects.filter(phone__icontains=phone)

  return render(request, 'bookinfor/consume/deal_query.html', {'consume': consume,})


@login_required
def deal_new(request):
    if request.POST.get('phone') == None:
      return render(request, 'bookinfor/consume/deal_new.html')

    if request.POST.get('phone') =="" or request.GET.get('name') == "" or request.GET.get('outtime') == "":
      return render(request, 'bookinfor/consume/deal_new.html')

    phone = request.POST.get('phone')
    money = request.POST.get('money')
    sort = request.POST.get('sort')
    over = request.POST.get('over')
    handler =str(request.user)
    deposit = request.POST.get('deposit')
    remark = request.POST.get('remark')

    member = Bookmember.objects.values("remain").filter(phone=phone)
    if sort == "cz":
      remiannow = int(member[0]['remain']) + int(money)
      sort = "临时充值"

    if sort == "xf":
      remiannow = int(member[0]['remain']) - int(money)
      sort = "消费"

    if sort == "hy":
      remiannow = int(member[0]['remain'])
      sort = "会员"

    Bookmember.objects.filter(phone=phone).update(remain=str(remiannow))
    consume = Consume(phone=phone, money=money, sort=sort, over=str(remiannow), handler=handler, deposit=deposit, remark=remark)
    consume.save()

    return render(request, 'bookinfor/consume/deal_new_ok.html')


@login_required
def deal_manage(request):

    if request.GET.get('phone') == None:
      return render(request, 'bookinfor/consume/deal_manage.html')

    phone = request.GET.get('phone')
    consume = Consume.objects.filter(phone__icontains=phone)

    return render(request, 'bookinfor/consume/deal_manage.html', {'consume': consume,})



# --- consume end ---



# --- in out begin ---

@login_required
def inout_query(request):

  if request.GET.get('phone') == None:
      return render(request, 'bookinfor/inoutrecord/inout_query.html')

  phone = request.GET.get('phone')

  inout = Inoutrecord.objects.filter(phone__icontains=phone)

  return render(request, 'bookinfor/inoutrecord/inout_query.html', {'inout': inout,})



def inoutlogfile(runuser, phone, name, intime, remark):
  t = time.strftime("%Y-%m-%d-%H-%M-%S")
  filename = "inout-" + t + "-" + runuser + "-" + phone + ".txt"
  BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  inoutlog = os.path.join(BASE_DIR, 'static/log/inout', filename)
  with open(inoutlog, 'a+') as f:
    f.write(time.strftime("%Y-%m-%d %H:%M:%S"))
    f.write('\n')
    f.write(' runuser: %s \n phone: %s \n name: %s \n intime: %s \n remark: %s \n' %(runuser, phone, name, intime, remark))



@login_required
def inout_manage(request):

    if request.GET.get('phone') == None:
      return render(request, 'bookinfor/inoutrecord/inout_manage.html')

    phone = request.GET.get('phone')
    name = request.GET.get('name')
    inout = Inoutrecord.objects.filter(phone__icontains=phone).filter(name__icontains=name).order_by('intime')

    return render(request, 'bookinfor/inoutrecord/inout_manage.html', {'inout': inout,})



@login_required
def inout_out_new(request):
    if request.POST.get('phone') == None:
      return render(request, 'bookinfor/inoutrecord/inout_out_new.html')

    if request.POST.get('phone') =="" or request.GET.get('name') == "" or request.GET.get('outtime') == "":
      return render(request, 'bookinfor/inoutrecord/inout_out_new.html')

    phone = request.POST.get('phone')
    name = request.POST.get('name')
    zcbm = request.POST.get('zcbm')
    outtime = request.POST.get('outtime')
    handlerout =str(request.user)
    remark = request.POST.get('remark')

    inout = Inoutrecord(phone=phone, name=name, zcbm=zcbm, outtime=outtime, handlerout=handlerout, remark=remark)
    inout.save()

    return render(request, 'bookinfor/inoutrecord/inout_out_new_ok.html')



@login_required
def inout_modify(request):

  if request.GET.get('phone') == None:
      return render(request, 'bookinfor/inoutrecord/inout_manage.html')

  if "cx" in request.GET:
    phone = request.GET.get('phone')
    name = request.GET.get('name')
    inout = Inoutrecord.objects.filter(phone__icontains=phone).filter(name__icontains=name)

    return render(request, 'bookinfor/inoutrecord/inout_modify.html', {'inout': inout,})

  if "gx" in request.GET:
    handlerin =str(request.user)
    intime = request.GET.get('intime')
    remark = request.GET.get('remark')
    phone = request.GET.get('phone')
    name = request.GET.get('name')

    Inoutrecord.objects.filter(phone=phone).filter(name=name).update(handlerin=handlerin, intime=intime, remark=remark)

    inout = Inoutrecord.objects.filter(phone=phone).filter(name=name)

    inoutlogfile(handlerin, phone, name, intime, remark)

    return render(request, 'bookinfor/inoutrecord/inout_modify_ok.html', {'inout': inout,})



def inout_log(request):

  BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  inoutlogdir = os.path.join(BASE_DIR, 'static/log/inout')
  filename = os.listdir(inoutlogdir)
  filename.sort(reverse=True)

  return render(request, 'bookinfor/inoutrecord/inout_log.html', {'filename': filename,})



# --- in out end ---



# --- ajax begin ---

# phone list
def ajax_get_phone_list(request):
    search = request.GET.get('search')
    val_list = []

    if search == None or '':
        return JsonResponse(val_list, safe=False)
    else:
        orgs = Bookmember.objects.filter(phone__icontains=search)

        for org in orgs.values('phone'):
          val_list.append(org['phone'])
        return JsonResponse(val_list, safe=False)



# --- ajax end ---


