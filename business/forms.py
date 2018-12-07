from django import forms
from .models import Business, CommentBusiness, Promo


class BusinessForm(forms.ModelForm):

    class Meta:
        model = Business

        fields = [
            'name',
            'hours',
            'email',
            'address',
            'categories',
        ]
        labels = {
            'name':'Nombre de Establecimiento',
            'hours':'Horario',
            'email':'Correo Electronico',
            'address':'Direccion',
            'categories':'Categorias',
        }
        widgets = {
            'name': forms.TextInput ,
            'hours': forms.TextInput ,
            'email': forms.TextInput,
            'address': forms.TextInput,
            'categories': forms.CheckboxSelectMultiple ,
        }

class CommentBusinessForm(forms.ModelForm):

    class Meta:
        model = CommentBusiness

        fields = [
            'comment',
            'score',
            'business',
        ]
        labels = {
            'comment':'Agrega un comentario',
            'score':'Calificacion',
            'business':'Establecimiento',
        }

class PromoForm(forms.ModelForm):

    class Meta:
        model = Promo

        fields = [
            'name',
            'description',
            'business',
        ]
        labels = {
            'name':'Promo',
            'description':'Descripcion',
            'business':'Establecimiento',
        }
        widgets = {
            'name': forms.TextInput ,
            'description': forms.TextInput,
            'business': forms.CheckboxSelectMultiple ,
        }

""" class UserForm(forms.ModelForm):

    class Meta:
        model = User

        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'username':'Nombre de usuario',
            'first_name':'Nombre',
            'last_name':'Apellido',
            'email':'Correo Electronico',
        }
        widgets = {
            'username':form.TextInput,           
            'first_name': forms.TextInput ,
            'last_name': forms.TextInput ,
            'email': forms.TextInput,
        }
 """


