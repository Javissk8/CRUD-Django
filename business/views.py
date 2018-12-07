from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Business, CommentBusiness
from .forms import BusinessForm, CommentBusinessForm, PromoForm

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        user = request.user
        businesses = Business.objects.all()
        context = {
            'businesses': businesses
        }
        return render(request, 'home.html', context)
    return render(request, 'home.html')

def detail_business(request, business_id):
    if request.user.is_authenticated:
        business = Business.objects.get(id=business_id)
        context = {
            'business': business
        }
        return render(request, 'detail.html', context)
    return render(request, 'detail.html')

def create_business(request):
    if request.user.is_authenticated:
        print('ok')
        form = BusinessForm(request.POST or None)
        if request.method == 'POST':
            print('ok2')
            if form.is_valid():
                print('ok3')
                form.save()
            return redirect('index')
        else:
            print('algo dif')
            form = BusinessForm()
            return render(request, 'create_business.html', {'form':form})
    return redirect('login')

def edit_business(request, business_id):
    if request.user.is_authenticated:
        business = Business.objects.get(id=business_id)
        if request.method == 'POST':
            form = BusinessForm(request.POST, instance=business)
            if form.is_valid():
                form.save()
            return redirect('detail_business', business_id)
        else:
            form = BusinessForm(instance=business)
            return render(request, 'edit_business.html', {'form':form})
    return redirect('login')

def delete_business(request, business_id):
    if request.user.is_authenticated:
        business = Business.objects.get(id=business_id)
        business.delete()
        return render(request, 'delete.html')
    return render(request, 'delete.html')


""" def edit_user(request):
    form = UserForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=False)
        return redirect('index')
    else:
        form = UserForm()
        return render(request, 'edit_profile.html', {'form':form}) """

def create_comment(request):
    if request.user.is_authenticated:
        form = CommentBusinessForm(request.POST or None)
        if request.method == 'POST':
            print(form.is_valid())
            if form.is_valid():
                print(request)
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
            return redirect('index')
        else:
            form = CommentBusinessForm()
            return render(request, 'create_comment.html', {'form':form})
    return redirect('login')

def edit_comment(request,business_id):
    if request.user.is_authenticated:
        comment = CommentBusiness.objects.get(id=business_id)
        if request.method == 'POST':
            form = CommentBusinessForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
            return redirect('detail_comment', business_id)
        else:
            form = CommentBusinessForm(instance=comment)
            return render(request, 'edit_comment.html', {'form':form})
    return redirect('login')

def detail_comment(request,id):
    if request.user.is_authenticated:
        comment = CommentBusiness.objects.get(id=id)
        context = {
            'comment': comment
        }
        return render(request, 'detail_comment.html', context)
    return render(request, 'detail_comment.html')

def delete_comment(request,id):
    if request.user.is_authenticated:
        comment = CommentBusiness.objects.get(id=id)
        comment.delete()
        return render(request, 'delete.html')
    return render(request, 'delete.html')

'''promo'''

def create_promo(request):
    if request.user.is_authenticated:
        form = PromoForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                form.save(commit=False)
            return redirect('index')
        else:
            form = PromoForm()
            return render(request, 'create_promo.html', {'form':form})
    return redirect('login')

def edit_comment(request,business_id):
    if request.user.is_authenticated:
        comment = CommentBusiness.objects.get(id=business_id)
        if request.method == 'POST':
            form = CommentBusinessForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
            return redirect('detail_comment', business_id)
        else:
            form = CommentBusinessForm(instance=comment)
            return render(request, 'edit_comment.html', {'form':form})
    return redirect('login')

def detail_comment(request,business_id):
    if request.user.is_authenticated:
        comment = CommentBusiness.objects.get(id=business_id)
        context = {
            'comment': comment
        }
        return render(request, 'detail_comment.html', context)
    return render(request, 'detail_comment.html')

def delete_comment(request,id):
    if request.user.is_authenticated:
        comment = CommentBusiness.objects.get(id=id)
        comment.delete()
        return render(request, 'delete.html')
    return render(request, 'delete.html')

