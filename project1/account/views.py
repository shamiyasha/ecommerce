from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.

def login(request):
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      
      user = auth.authenticate(username = username,password = password)

      if user is not None:
         auth.login(request,user)
         return redirect('/')
      else:
         messages.info(request,'invalid credentials')
         return redirect('login')
   else:  
    return render(request,'login.html')

def register(request):
    
    if request.method == 'POST':
        
       first_name = request.POST['firstname']
       last_name = request.POST['lastname']
       user_name = request.POST['username']
       email = request.POST['email']
       password1 = request.POST['password1']
       password2 = request.POST['password2']

       if password1 == password2:
          if User.objects.filter(username = user_name).exists():
             messages.info(request,'username is already exist')
             return redirect('register')
          elif User.objects.filter(email = email).exists():
             messages.info(request,'mail is already exist') 
             return redirect('register') 
          else:        
           user = User.objects.create_user(username = user_name,password=password1,email=email,first_name=first_name,last_name=last_name)
           user.save()
           print('user created')
           return redirect('login')
         
       else:
          messages.info(request,'password is not matching') 
          return redirect('register')
       
    else:
     return render(request,'register.html')
    
def logout(request):
   auth.logout(request)
   return redirect("/")    

def mumbai(request):
   return render(request,'mumbai.html')