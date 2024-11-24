# Ex02 Django ORM Web Application
## Date:24.11.2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

![alt text](<Screenshot 2024-11-24 130817.png>)



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin
from .models import Bankloan,BankloanAdmin
admin.site.register(Bankloan,BankloanAdmin)

models.py

from django.db import models
from django.contrib import admin
class Bankloan(models.Model):
    Customer_id=models.IntegerField(primary_key=True)
    Customer_name=models.CharField(max_length=100)
    Account_no=models.IntegerField()
    Account_type=models.CharField(max_length=50)
    Age=models.IntegerField()
    Loan_type=models.CharField(max_length=50)
    Loan_amount=models.IntegerField()
 
class BankloanAdmin(admin.ModelAdmin):
    list_display=('Customer_id','Customer_name','Account_no','Account_type','Age','Loan_type','Loan_amount')

```



## OUTPUT

![alt text](<Screenshot 2024-11-24 121703.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
