import os 
import django 

#this file generating fake records
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fourthprodatabase.settings')
django.setup()

from testapp.models import * 
from faker import Faker 
from random import * 

fake = Faker() 
def populate(n):
    for i in range(n):
        feno = randint(1001,9999)
        fename = fake.name()
        fesal = randint(30000,40000)
        feaddress = fake.city()
        emp_record = Employee.objects.get_or_create(e_no=feno,e_name=fename,e_sal=fesal,e_address=feaddress)
populate(30)

def populate1(n):
    for i in range(n):
        pname = fake.name()
        pdate = fake.date()
        psal = randint(30000,40000)
        ploc = fake.city()
        pqualif = fake.random_element(elements=('B.Tech','Deplomo','B.Sc','Post Graduation'))
        emp_record = Job.objects.get_or_create(posting_date=pdate,post_name=pname, salary=psal,location=ploc,qualification=pqualif)
populate1(30)

def phoneNumberGeneration():
    d1 = randint(7,9)
    num = ''+ str(d1)
    for i in range(9):
        num += str(randint(0,9))
    return int(num)
#after writing this code we have to run this file in terminal to add fake records in admin and our results.html
# python populate.py 
#next we have to run the server
# python manage.py runserver 
# now we see the fake data in admin and results.html page also