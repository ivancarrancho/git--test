from django.shortcuts import render, redirect
from django.http import JsonResponse
from app.models import ExpensesRegistry
from app.models import Wife
from app.models import Husband
from app.forms import ExpensesForm


def data_accounts(request):
    data_list = ExpensesRegistry.objects.all()
    range_list = range(100)
    template = 'home.html'

    return render(request, template, {
        'data_list': data_list,
        'range_list' : range_list,
    })

def dates_concepts(request, pk):
    template = 'detail.html'
    date_concept = ExpensesRegistry.objects.get(pk = pk)

    return render(request,template, {
        'expense': date_concept,
    })

def sum_expense(request, pk):
    my_expense = ExpensesRegistry.objects.get(pk = pk)
    suma = int(my_expense.expenses) * int(request.POST.get('add'))
    return JsonResponse({
        'expenses_now': suma,
    }, status = 201)

def create_data(request):
    if request.method == 'POST':
        myForm = ExpensesForm(request.POST)
        if myForm.is_valid():
            myForm.save()
            return redirect('/home')
    else:
        myForm = ExpensesForm()
    return render(request, 'create_data.html', {'myForm': myForm})

def wifes_data(request):
    template = 'wifes.html'
    wifes = Wife.objects.all()
    return render(request, template,{
        'wifes':wifes,
    })

def husbands_data(request):
    template = 'husbands.html'
    husbands = Husband.objects.all()
    return render(request, template,{
        'husbands':husbands,
    })
