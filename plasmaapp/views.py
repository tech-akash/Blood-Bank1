from django.shortcuts import redirect, render
from .forms import AcceptorForm,DonatorForm,CustomerForm,SignUpform
from .models import Accept,Donate,Customer
# Create your views here.
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import un_authenticated,allowed_user
from django.contrib.auth.models import Group
from django.contrib import messages
import datetime
from django.core.mail import BadHeaderError, send_mail

# @un_authenticated
# def signuppage(request):
    
#     form=UserCreationForm()
#     if request.method=='POST':
#         form=UserCreationForm(request.POST)
#         if form.is_valid():
#             user=form.save()
#             username=request.POST.get('username')
#             print(username)
            
#             group=Group.objects.get(name='customer')
#             user.groups.add(group)
#             Customer.objects.create(
#                 user=user,
#                 username=username,
#                 dayofaccept=datetime.date.today(),
#             )
#             return redirect(loginpage)
#         else:
#             for msg in form.error_messages:
#                 messages.error(request, f"{msg}: {form.error_messages[msg]}")
#                 print(msg)
#     context={
#         'form':form
#     }
#     return render(request,'signuppage.html',context)




@un_authenticated
def signuppage(request):
    
    form=SignUpform()
    if request.method=='POST':
        form=SignUpform(request.POST)
        if form.is_valid():
            user=form.save()
            username=request.POST.get('username')
            email=request.POST.get('email')
            print(username)
            
            group=Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(
                user=user,
                username=username,
                dayofaccept=datetime.date.today(),
                email=email
            )
            return redirect(loginpage)
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
                print(msg)
    context={
        'form':form
    }
    return render(request,'signuppage.html',context)

















@un_authenticated
def loginpage(request):
    
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else :
            print('wrong Password')
    return render(request,'loginpage.html',{})


def logoutpage(request):
    logout(request)
    return redirect('home')

@login_required(login_url='loginpage')
@allowed_user(allowedroles=['customer'])
def home(request):
    user=request.user
    noofdonate1=Customer.objects.filter(need='Donator')
    noofdonate=0
    noofaccept=0
    # bloodgrpPresent=[]
    # bloodpresentApt=0
    # bloodpresentAng=0
    # bloodpresentOpt=0
    # bloodpresentOng=0
    # bloodpresentABpt=0
    # bloodpresentABng=0
    # bloodpresentBpt=0
    # bloodpresentBng=0
    for i in noofdonate1:
        if i.status=='GotIt':
            noofdonate+=1
            

    noofaccept1=Customer.objects.filter(need='Acceptor')
    for i in noofaccept1:
        if i.status=='GotIt':
            noofaccept+=1

    context={
        'user':user,
        'noofdonate':noofdonate,
        'noofaccept':noofaccept
    }

    return render(request,'home.html',context)

@login_required(login_url='loginpage')
def acceptor(request):
    form=AcceptorForm()
    if request.method=='POST':
        form=AcceptorForm(request.POST)
        form.save()
        return redirect('home')
    context={
        'form':form
    }
    return render(request,'acceptor.html',context)
@login_required(login_url='loginpage')
def donator(request):
    form=DonatorForm()
    if request.method=='POST':
        form=DonatorForm(request.POST)
        form.save()
        return redirect('home')
    context={
        'form':form
    }
    return render(request,'donator.html',context)










@login_required(login_url='loginpage')
@allowed_user(allowedroles=['customer'])
def customerpage(request):
    id=request.user
    instance=Customer.objects.get(username=id)
    form=CustomerForm(instance=instance)
    need=instance.need
    status=instance.status
    date=instance.dayofaccept
    if request.method=='POST':
        
        form=CustomerForm(request.POST,request.FILES,instance=instance)
        form.save()
        return redirect('customerpage')
    context={
        'form':form,
        'need':need,
        'status':status,
        'date':date
    }
    return render(request,'customerpage.html',context)



@login_required(login_url='loginpage')
@allowed_user(allowedroles=['customer'])

def formfill(request):
    username=request.user
    instance=Customer.objects.get(username=username)
    form=CustomerForm(instance=instance)
    if request.method=='POST':
        form=CustomerForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            form.save()
            print('hii')
            return redirect('customerpage')
        else:
            print('Error bro')
    context={
        'form':form
    }
    return render (request,'formfill.html',context)













@login_required(login_url='loginpage')
@allowed_user(allowedroles=['admin'])
def admin1(request):
    
        
    instanceAccept=Accept.objects.filter(status='Pending')
    instanceAcceptall=Accept.objects.all()
    instanceDonate=Donate.objects.filter(status='Pending')
    instanceDonateall=Donate.objects.all()
    instanceCustomerall=Customer.objects.all()
    

    context={
        'PendingAcceptor':instanceAccept,
        'AllAcceptor':instanceAcceptall,
        'PendingDonator':instanceDonate,
        'AllDoaner':instanceDonateall,
        'AllCustomer':instanceCustomerall
    }
    return render(request,'admin.html',context)

@login_required(login_url='loginpage')
@allowed_user(allowedroles=['admin'])
def editaccept(request,username):
    isinstance=Customer.objects.get(username=username)
    print(isinstance.name)
    form1=CustomerForm(instance=isinstance)
    if request.method=='POST':
        form1=CustomerForm(request.POST,request.FILES,instance=isinstance)
        print(form1)
        # # form=request.POST.get('status')
        # isinstance.status=form1.status
        # isinstance.dayofaccept=()
        # # if form is not 'Pending':
        # #     print('hii')
        # #     date=None
        # #     date=request.POST.get('date')
        # #     print(date)
        # #     if date is not None:
        # isinstance.dayofaccept=form1.dayofaccept
        
        
        form1.save()
        instance=Customer.objects.get(username=username)
        status=instance.status
        message=''
        dt=instance.dayofaccept
        month=str(dt.month)
        year=str(dt.year)
        day=str(dt.day)
        # print(type(str(dt.month)))
        
        if not status=='Pending':
            subject='Staus '+instance.status
            if status =='Accepted':
                dayofaccept=instance.dayofaccept
                message='Hii '+instance.name+'\nYour request as '+instance.need+' has been approved!'+'\n Date of Appointment is '+day+'-'+month+'-'+year+'\nThank You'
            elif status=='GotIt':
                message='Hii '+instance.name+'\nThank You using our services'+'\nStay Safe Stay Happy'+'\nThank You'
            else:
                message='Hii '+instance.name+'\nSorry Due to certain reasons your request is rejected :('+'\nPlease fill the form correctly'+'\nThank You'
            send_mail(subject, message, 'ascsingh500@gmail.com',[instance.email])
            return redirect(admin1)
    context={
        'customer':isinstance,
        'form':form1,
        
    }
    
    return render(request,'adminedit.html',context)

# @login_required(login_url='loginpage')
# @allowed_user(allowedroles=['admin'])
# def mailAppointment(request,username):
    
#     instance=Customer.objects.get(username=username)
#     status=instance.status
#     message=''
#     if not status=='Pending':
#         subject='Staus '+instance.status
#         if status =='Accepted':
#             message='Hii '+instance.name+'\nYour request as '+instance.need+' has been approved!'+'\n Date of Appointment is '+instance.dayofaccept+'\nThank You'
#         elif status=='GotIt':
#             message='Hii '+instance.name+'\nThank You using our services'+'\nStay Safe Stay Happy'+'\nThank You'
#         else:
#             message='Hii '+instance.name+'\nSorry Due to certain reasons your request is rejected :('+'\nPlease fill the form correctly'+'\nThank You'
#         send_mail(subject, message, ['techakash2000@gmail.com'])
#         return redirect(admin1)
#     return redirect('admine')
    

        