from django.shortcuts import render,redirect
from .forms import UserForm
from .models import User,UserProfile
from vendor.models import Vendor
from django.contrib import messages
from vendor.forms import VendorForm
def registerUser(request):
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            # password=form.cleaned_data['password']
            # user=form.save(commit=False)
            # user.set_password(password)
            # user.role=User.CUSTOMER
            # user.save()
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            user.role=User.CUSTOMER
            user.save()
            messages.success(request,"Your account has been successfully registered")
            return redirect("registerUser")
    else:
        form=UserForm()
    context={
            'form':form,
        }
    return render(request,'accounts/registerUser.html',context)
def registerVendor(request):
    if request.method=='POST':
        form=UserForm(request.POST)
        v_form=VendorForm(request.POST,request.FILES)
        if form.is_valid() and v_form.is_valid:
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            print(user)
            user.role=User.VENDOR
            user.save()
            vendor=v_form.save(commit=False)
            vendor.user=user
            user_profile=UserProfile.objects.get(user=user)
            # print(user_profile)
            vendor.user_profile=user_profile
            vendor.save()
            messages.success(request,"Your account has been registered successfully please wait for approval")
            return redirect('registerVendor')
        else:
            print(form.errors)
    else:     
        form=UserForm()
        v_form=Vendor=VendorForm()
    context={
        'form':form,
        'v_form':v_form
    }
    return render(request,'accounts/registerVendor.html',context)


# Create your views here.
