from django.shortcuts import render
from .models import User
from django.http import JsonResponse
# Create your views here.

def home(request):
 stud = User.objects.all()
 return render(request, 'enroll/home.html', {'stu':stud})

# @csrf_exempt
def save_data(request):
  if request.method == "POST":
    sid = request.POST.get(request.POST['stuid'])
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    if(sid == ''):
      usr = User.objects.create(name = name, email = email, password = password)
    else:
      usr = User.objects.create(id=sid, name = name, email = email, password = password)
    usr.save()
    stud = User.objects.values()
    # print(stud)
    student_data = list(stud)
    return JsonResponse({'status':'Save', 'student_data':student_data})
  else:
    return JsonResponse({'status':0})

# Delete Data
def delete_data(request):
 if request.method == "POST":
  id = request.POST.get('sid')
  # print(id)
  pi = User.objects.get(pk=id)
  pi.delete()
  return JsonResponse({'status':1})
 else:
  return JsonResponse({'status':0})

# Edit Data
def edit_data(request):
 if request.method == "POST":
  id = request.POST.get('sid')
  # print(id)
  student = User.objects.get(pk=id)
  student_data = {"id":student.id, "name":student.name, "email":student.email, "password":student.password}
  return JsonResponse(student_data)