# blog/views.py


from django.shortcuts import render, redirect
from .models import Blog
from .form import AddBlogForm,EditBlogForm

    

def add_blog(request):
    form=AddBlogForm()
    if request.method == "POST":
        form = AddBlogForm(request.POST ,  request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('/blog/')
        else:
            print(form.errors)
    context = {"data": "this is blog add form", "form": form}
    return render(request, 'blog/add.html',context)

def list_blog(request):
    context = {
        "data": Blog.objects.all().order_by('-add_date')
        }
    return render(request, "blog/home.html", context)

def view_blog(request,title):
    context = {
        "blog": Blog.objects.get(title=title)
        }
    return render(request, "blog/view.html", context)


def edit_blog(request,title):
    blog_data = Blog.objects.get(title=title)
    if request.method == 'POST':
        form = EditBlogForm(request.POST or request.FILES or None, instance=blog_data)
        if form.is_valid():
            form.save()
            return redirect('/blog/')
        else:
            print(form.errors)
    else:
        form = AddBlogForm(instance=blog_data)

    context = {
        "data": blog_data,
        "form": form
    }
    return render(request, 'blog/edit.html', context) 


def delete_blog(request,title):
    Blog.objects.get(title=title).delete()
    return redirect('/blog/')
