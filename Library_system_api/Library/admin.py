from django.contrib import admin
from . models import Book,User,Transactions



class UserAdmin(admin.ModelAdmin):
    list_display =["username","Email","Membership_Date","Active_Status"]

class BookAdmin(admin.ModelAdmin):
    list_display =["Title","Author","ISBN","Published_Date","number_of_copies",]

class TransactionsAdmin(admin.ModelAdmin):
    list_display =["book","user","Check_out","Returned","Check_out_date","Returned_Date","Fine",]


admin.site.register(User, UserAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Transactions, TransactionsAdmin)
