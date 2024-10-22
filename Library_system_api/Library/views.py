from django.shortcuts import render, redirect
from .forms import CreateuserForm, loginForm, BookForm
from .models import User, Book, Transactions
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required




def Homepage(request):
    return render(request,'Library/index.html')

def CreateUser(request):

    user = CreateuserForm()

    if request.method == "POST" :

        user = CreateuserForm(request.POST)

        if user.is_valid():
            user.save()
            return redirect("login")

    context = {'user':user}
    return render(request,'Library/register.html' , context=context)

def login(request):

    form = loginForm()

    if request.method == "POST":

        form = loginForm(request, data = request.POST)

        if form.is_valid():
            
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)

            if user is not None:

                auth.login(request,user)
                return HttpResponse('youhave logged in') #redirect("ViewBooks")
            
    context = {'form':form}
    return render(request,'Library/login.html', context = context)

def signout(request):
    pass

def Addbook(request):
    book = BookForm()

    if request.method == 'POST':
        book = BookForm(request.POST)
        
        if book.is_valid():
            book.save()
        return redirect("ViewBooks")
    
    context = {'book':book}
    return render(request,'Library/addbook.html', context = context) 
    
def View_Books(request):
    all_books = Book.objects.all()
    context = {'all_books': all_books}
    return render (request, 'Library/Viewbook.html', context = context)

#@login_required(login_url='login')
def Check_out(request):

    if request.method == 'POST':
        book_id = request.POST.get('book')
        user_id = request.POST.get('user')

        try:
            book = Book.objects.get(id = book_id)
            user = Book.objects.get(id = user_id)
        except (Book.DoesNotExist, User.DoesNotExist):
            return HttpResponse('Book or user does not exist')
        
        borrowed_book = Transactions.objects.create(
            book_id = book,
            user_id = user,
        )
        borrowed_book.save()
        current_book = Book.objects.filter(book_id)
        current_book.update(number_of_copies = current_book[0].number_of_copies - 1)

        return redirect('Transactions')
    else :
        return HttpResponse('Unable to borrow the Book')
    
def Trans_Hist(request):
        my_items = Transactions.objects.all
        context = {'my_items':my_items}
        return render(request, 'Library/transaction.html', context = context)
