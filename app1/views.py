from django.shortcuts import render, redirect , get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from app1.models import Person
from app1.forms import UserForm
from django.views.generic import ListView
# Create your views here.

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            dob = form.cleaned_data['dob']
            gender = form.cleaned_data['gender']

            Person.objects.create(first_name = first_name, last_name = last_name, dob = dob,
                                    gender = gender)
            context ={
                'name':first_name,
                'dob':dob,
                'gender':gender,
            }
    else:
        form = UserForm()
        context = {
            'form':form,
        }
    return render(request, 'app1/add.html', context)

def update_user(request,user_id_pk):
    instance = Person.objects.get(pk = user_id_pk)
    form = UserForm(instance = instance)
    if request.method == 'POST':
        form = UserForm(request.POST, instance = instance)
        if form.is_valid():
            form.save()
            return redirect('/view')
    context = {'form':form}
    return render(request, 'app1/edit.html', context)

def get_user_id(request, user_id_pk):
    instance = Person.objects.filter(pk = user_id_pk)
    return render(request, "app1/detail_view.html", {"result" : instance})

def get_user_all(request):
    user_obj = Person.objects.all()
    return render(request, 'app1/view.html', {"result" : user_obj})

def user_delete(request, pk):
    user = get_object_or_404(Person, pk=pk)
    data = dict()
    if request.method == 'POST':
        user.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        users = user.objects.all()
        data['html_user_list'] = render_to_string('partial_user_list.html', {
            'users': users
        })
    else:
        context = {'user': user}
        data['html_form'] = render_to_string('partial_user_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)