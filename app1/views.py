from django.shortcuts import render
from .models import User

# Create your views here.
def index(requests):
    data=User.objects.all()
    context={
        "data":data,
    }
    return render(requests,"index.html",context)

def add(requests):
    if requests.method=="POST":
        name=requests.POST.get("name")
        contact=requests.POST.get("contact")
        city=requests.POST.get("city")
        country=requests.POST.get("country")

        user=User.objects.create(name=name,contact=contact,city=city,country=country)
        if user:
            user.save()
            data=User.objects.all()
            context={
                "data":data,
            }
            return render(requests,'index.html',context)
        else:
            return redirect("index")

    elif requests.method=="GET":
        data=User.objects.all()
        context={
            "data":data,
        }
        return render(requests,'index.html',context)
    else:
        return render(requests,'index.html')
    
def show(requests):
    data=User.objects.all()
    context={
        "data":data,
    }
    return render(requests,"index.html",context)

def edit(requests):
    if requests.method=="post":
        id=requests.post.get("id")
        user=User.objects.fiter(id=id)
        if user:
            context={
                "user":user,
            }
            return render(requests,"show.html",context)
