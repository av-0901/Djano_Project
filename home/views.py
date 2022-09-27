from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader

from home.models import Employee
# Create your views here.
def index(request):
    emp=Employee.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'emp': emp,
    }
    return HttpResponse(template.render(context,request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
  a = request.POST['name']
  b = request.POST['dept']
  c = request.POST['desig']
  d = request.POST['salary']
  member = Employee(name=a, dept=b, desig=c, salary=d)
  member.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  member = Employee.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  mymember = Employee.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
def updaterecord(request, id):
  a = request.POST['name']
  b = request.POST['dept']
  c = request.POST['desig']
  d = request.POST['salary']
  member = Employee.objects.get(id=id)
  member.name = a
  member.dept = b
  member.desig = c
  member.salary = d
  member.save()
  return HttpResponseRedirect(reverse('index'))