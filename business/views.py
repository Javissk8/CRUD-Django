from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Business, CommentBusiness, Promo
from .forms import BusinessForm, CommentBusinessForm, PromoForm
from django.contrib import messages

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        group = request.user.groups.all()[0].name
        if group == 'owner':
            businesses = Business.objects.filter(user_id=request.user.id)
            context = {
                'businesses': businesses
            }
            return render(request, 'home.html', context)
        if group == 'user':
            businesses = Business.objects.all()
            context = {
                'businesses': businesses
            }
            return render(request, 'home_users.html', context)
    else:
        businesses = Business.objects.all()
        context = {
            'businesses': businesses
        }
        return render(request, 'home_users.html', context)
    return render(request, 'home.html')

# Business

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
        form = BusinessForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                business = form.save(commit=False)
                business.user_id = request.user.id
                business.save()
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
                business
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

# Comments

def create_comment(request,business_id):
    if request.user.is_authenticated:
        group = request.user.groups.all()[0].name
        if group == 'user':
            form = CommentBusinessForm(request.POST or None)
            if request.method == 'POST':
                if form.is_valid():
                    comment = form.save(commit=False)
                    comment.user = request.user
                    comment.business_id = business_id
                    comment.save()
                    messages.add_message(request, messages.SUCCESS , 'Comentario agregado exitosamente!')
                return redirect('index')
            else:
                form = CommentBusinessForm()
                return render(request, 'create_comment.html', {'form':form})
        else:
            messages.add_message(request, messages.WARNING, 'Tienes que estar logueado como usuario')            
            return redirect('index')
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

def detail_comment(request, business_id):
    if request.user.is_authenticated:
        comments = CommentBusiness.objects.filter(business_id=business_id)
        print(comments)
        context = {
            'comments': comments
        }
        return render(request, 'detail_comment.html', context)
    return render(request, 'detail_comment.html')

def delete_comment(request,id):
    if request.user.is_authenticated:
        comment = CommentBusiness.objects.get(id=id)
        comment.delete()
        return render(request, 'delete.html')
    return render(request, 'delete.html')
# Promos

def create_promo(request, business_id):
    if request.user.is_authenticated:
        group = request.user.groups.all()[0].name
        if group == 'owner':
            form = PromoForm(request.POST or None)
            if request.method == 'POST':
                if form.is_valid():
                    Promo = form.save(commit=False)
                    Promo.business_id = business_id
                    Promo.save()
                    messages.add_message(request, messages.SUCCESS , 'Promo agregada exitosamente!')
                return redirect('index')
            else:
                form = PromoForm()
                return render(request, 'create_promo.html', {'form':form})
        else:
            messages.add_message(request, messages.WARNING, 'Tienes que estar logueado como Negocio para agregar promociones')            
            return redirect('index')
    return redirect('login')

# def edit_comment(request,business_id):
#     if request.user.is_authenticated:
#         comment = CommentBusiness.objects.get(id=business_id)
#         if request.method == 'POST':
#             form = CommentBusinessForm(request.POST, instance=comment)
#             if form.is_valid():
#                 form.save()
#             return redirect('detail_comment', business_id)
#         else:
#             form = CommentBusinessForm(instance=comment)
#             return render(request, 'edit_comment.html', {'form':form})
#     return redirect('login')

def detail_promo(request,business_id):
    if request.user.is_authenticated:
        promos = Promo.objects.filter(business_id=business_id)
        context = {
            'promos': promos
        }
        print(promos)
        return render(request, 'detail_promo.html', context)
    return render(request, 'detail_promo.html')

# def delete_comment(request,id):
#     if request.user.is_authenticated:
#         comment = CommentBusiness.objects.get(id=id)
#         comment.delete()
#         return render(request, 'delete.html')
#     return render(request, 'delete.html')

