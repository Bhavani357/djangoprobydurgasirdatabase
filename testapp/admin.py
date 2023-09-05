from django.contrib import admin
from testapp.models import Employee,Job,Book,Customer

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['e_no','e_name','e_sal','e_address']

class JobAdmin(admin.ModelAdmin):
    list_display = ['post_name','posting_date','location','salary','qualification']

class BookAdmin(admin.ModelAdmin):
    list_display = ['number','title','author','published_date']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['phoneNumber','name','age','mailId']



admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Job,JobAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Customer,CustomerAdmin)
