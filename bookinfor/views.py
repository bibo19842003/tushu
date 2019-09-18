from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader, Context
from django.contrib.auth.decorators import login_required
from bookinfor.models import Bookinfor, Consume, Bookmember, Inoutrecord
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




def mermber_query(request):

  member = Bookmember.objects.all()

  return render(request, 'bookinfor/bookmember/bookmember_query.html', {'member': member,})



def inout_query(request):

  inout = Inoutrecord.objects.all()

  return render(request, 'bookinfor/inoutrecord/inout_query.html', {'inout': inout,})

