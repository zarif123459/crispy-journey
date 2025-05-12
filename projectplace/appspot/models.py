from django.db import models
from django.utils.timezone import now
# Create your models here.

class User(models.Model):
    uid = models.AutoField(primary_key=True)
    first=models.CharField(max_length=64)
    last=models.CharField(max_length=64)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    password=models.CharField(max_length=64)
    balance=models.IntegerField()
    role=models.CharField(max_length=64)
    def __str__(self):
        return self.username
    class Meta:
        db_table = "Users"
    


class Transaction(models.Model):
    tranid = models.AutoField(primary_key=True)
    amount=models.IntegerField()
    userid = models.ForeignKey(User, to_field='uid', on_delete=models.CASCADE)  # FK for UserPersonal
    category = models.ForeignKey('Category', to_field='catid', on_delete=models.CASCADE)  # FK for Category
    date=models.DateField(default=now)
    
    class Meta:
        db_table="Transactions"

class Category(models.Model):
    catid = models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    setbudget=models.IntegerField()
    totalspend=models.IntegerField()
    userid = models.ForeignKey(User, to_field='uid', on_delete=models.CASCADE)  # FK for UserPersonal

    def __str__(self):
        return self.name
    
    class Meta:
        db_table="Categories"

