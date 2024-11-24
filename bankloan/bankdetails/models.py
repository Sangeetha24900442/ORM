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

