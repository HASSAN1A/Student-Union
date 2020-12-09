from django.shortcuts import render,redirect
from django.http import HttpResponse
from .decorators import user_has_union
from .models import StudentUnion,EmergencyService,Business,Post
from users.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import F
from .forms import BusinessForm,NewPostForm,UserProfileForm

@login_required(login_url='/accounts/login')
def home_page(request):


  unions=StudentUnion.get_all_studentunions()
  if request.user.profile.studentunion:
    bss=Business.get_all_bs_by_union(request.user.profile.studentunion_id)
    posts=Post.objects.filter(studentunion=request.user.profile.studentunion)
    security_services=EmergencyService.objects.filter(studentunion=request.user.profile.studentunion,service_type='Security') 
    hos_services=EmergencyService.objects.filter(studentunion=request.user.profile.studentunion,service_type='Hospital') 
    Acc_services=EmergencyService.objects.filter(studentunion=request.user.profile.studentunion,service_type='Acc') 
    context={
      'unions':unions,
      'bss':bss,
      's_services':security_services,
      'h_services':hos_services,
      'Acc_services':Acc_services,
      'posts':posts
    }
  else:
    context={
      'unions':unions
    }
  return render(request,'home.html',context)



@login_required(login_url='/accounts/login')
def join_union(request,union_id):
  union=StudentUnion.find_studentunion(union_id)
  Profile.objects.filter(user=request.user).update(studentunion=union)
  StudentUnion.objects.filter(id=union_id).update(union_members=F("union_members") + 1)  
  messages.success(request, f'You joined {union.union_name} studentunion.')
  return redirect ('home_page')


@login_required(login_url='/accounts/login')
@user_has_union
def e_services(request):
  security_services=EmergencyService.objects.filter(studentunion=request.user.profile.studentunion,service_type='Security') 
  hos_services=EmergencyService.objects.filter(studentunion=request.user.profile.studentunion,service_type='Hospital') 
  acc_services=EmergencyService.objects.filter(studentunion=request.user.profile.studentunion,service_type='Acc') 
  context={
    's_services':security_services,
    'h_services':hos_services,
    'acc_services':acc_services
  }

  return render(request,'e_services.html',context) 



@login_required(login_url='/accounts/login')
@user_has_union
def union_bs(request):
  bss=Business.get_all_bs_by_union(request.user.profile.studentunion_id)

  if request.method == "POST":
      form = BusinessForm(request.POST, request.FILES)
      if form.is_valid():
          business = form.save(commit=False)
          business.user = request.user
          business.studentunion=request.user.profile.studentunion
          business.save()
          messages.success(request, f'Business successfully added')
          form = BusinessForm()
  else:
      form = BusinessForm()


  context={
    'bss':bss,
    'form':form
  }

  return render(request,'union_businesses.html',context)




@login_required(login_url='/accounts/login')
@user_has_union
def union_posts(request):
  posts=Post.objects.filter(studentunion=request.user.profile.studentunion)

  if request.method == "POST":
      form = NewPostForm(request.POST)
      if form.is_valid():
          post = form.save(commit=False)
          post.user = request.user
          post.studentunion=request.user.profile.studentunion
          post.save()
          messages.success(request, f'Post successfully uploaded')
          form = NewPostForm()
  else:
      form = NewPostForm()

  context={
    'posts':posts,
    'form':form
  }

  return render(request,'union_posts.html',context)


@login_required(login_url='/accounts/login')
def my_profile(request):
  profile=request.user.profile
  if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if form.is_valid():
            form.save()
            messages.success(request, f'Profile updated successfully')
            return redirect('my_profile')
  else:
      form = UserProfileForm(instance=request.user.profile)
  

  context={
    'profile':profile,
    'form':form
  }

  return render(request,'my_profile.html',context)




@login_required(login_url='/accounts/login')
@user_has_union
def search_business(request):

    if 'bs_name' in request.GET and request.GET["bs_name"]:
        search_term = request.GET.get("bs_name")
        bss =Business.search_business(search_term,request.user.profile.studentunion_id)
        message = f"{search_term}"

        context={
          "message":message,
          'bss':bss
        }
        return render(request, 'search.html',context)

    else:
        message = "You haven't searched for any business"
        context={
          "message":message,
        }
        return render(request, 'search.html',context) 
