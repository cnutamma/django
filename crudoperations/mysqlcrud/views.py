from django.shortcuts import render, redirect
from mysqlcrud.forms import EmployeeForm
from mysqlcrud.models import Employee

# from .models import User

"""
we can create views of models in two ways:
1)By creating EmployeeForm
2)By passing individual requests to the object
"""


def createempview(request):
    if request.method == "POST":
        empform = EmployeeForm(request.POST)
        if empform.is_valid():
            try:
                empform.save()
                return redirect("/admin")
            except:
                pass

    else:
        empform = EmployeeForm()

    return render(request, 'create.html', {'empform': empform})



"""def userreg(request):
    return render(request,"userreg.html",{})

"""

"""
def insertuser(request):
    id=request.POST['tid']
    name=request.POST['tname']
    sal=request.POST['tsal']
    us=User(vid=id,vname=name,vsal=sal)
    us.save()
    return render(request,'admin.html',{})


"""