from django.db import models





class Book(models.Model):

    Title = models.CharField("Title",max_length= 200)
    Author = models.CharField("Author",max_length= 200)
    ISBN = models.CharField("ISBN",max_length= 200)
    Published_Date = models.DateField("Published Date")
    number_of_copies = models.PositiveIntegerField("Number Of Copies")

class User(models.Model):
    username = models.CharField( max_length= 50)
    Email = models.EmailField( max_length= 50)
    password = models.CharField(max_length= 50)
    confirm_password = models.CharField(max_length= 50)
    Membership_Date = models.DateField(auto_now= True)
    Active_Status = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Transactions(models.Model):
    book = models.ForeignKey(Book, default=None, on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    Check_out = models.BooleanField(default=False)
    Returned = models.BooleanField(default=False)
    Check_out_date = models.DateTimeField()
    Returned_Date = models.DateTimeField()
    return_status=models.CharField(max_length=50,default=None)
    Fine = models.IntegerField(default = 0)

  
class History(models.Model):
    borrowed_Book =models.CharField(max_length=100)
    borrow_date = models.DateTimeField(auto_now_add = True)
    return_date = models.DateTimeField(auto_now = True)
    return_status=models.CharField(max_length=50,default=None)
    Fine =models.IntegerField(default = 0)
