from django.shortcuts import render
from testapp.models import Employee

# Create your views here.
def employee_info_view(request):
    all_data = Employee.objects.all()
    return render(request,'testapp/results.html',{'all_data':all_data})

def job_info_view(request):
    all_data = Job.objects.all()
    return render(request,'testapp/jobs.html',{'all_data':all_data})