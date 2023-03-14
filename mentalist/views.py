from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from . models import thumbnail,UserPermissions,contents
from django.shortcuts import render


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    else:
        try:
            user_permissions = UserPermissions.objects.get(user=request.user)
        except UserPermissions.DoesNotExist:
            user_permissions = UserPermissions.objects.create(user=request.user)
        
        carddata = thumbnail.objects.all().values("course_image")
        course_images = [data["course_image"] for data in carddata]
        hyperlinks = contents.objects.all().values('slug','link')
        slugs = [slug['slug'] for slug in hyperlinks]
        links = [link['link'] for link in hyperlinks]
        # print(links)
        

        permissions = []
        if user_permissions:
            permissions = [user_permissions.card1, user_permissions.card2, user_permissions.card3, user_permissions.card4, user_permissions.card5, user_permissions.card6, user_permissions.card7, user_permissions.card8]

        card_permissions = zip(course_images, permissions,slugs,links)
        

        context = {
            'card_permissions': card_permissions,
        }
        # print(type(card_permissions))

        return render(request, 'index.html', context)




def user_login(request):
    if request.user.is_authenticated:
        return render(request,'index.html')
    else:
        if request.method =="POST":
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,"Invalid username or password!")
                return render(request,'login.html')
def user_logout(request):
    logout(request)
    # You can add a success message if you like:
    messages.success(request, 'You have been logged out.')
    return render(request,'login.html') 


def video_page(request,slug):
    content = contents.objects.filter(slug=slug).first()
    return render(request,"video.html",{'content':content})
