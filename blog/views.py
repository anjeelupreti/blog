from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Blog
from blog.form import AddBlogForm, EditBlogForm
from django.http import HttpResponse

@login_required
def add_blog(request):
    if request.method == 'POST':
        form = AddBlogForm(request.POST, request.FILES)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.author = request.user  
           
            new_blog.save()
            return redirect('/blog/')
    else:
        form = AddBlogForm()
    
    return render(request, 'blog/add.html', {'form': form})

@login_required
def list_blog(request):
    context = {
        "data": Blog.objects.all().order_by('-add_date')
    }
    return render(request, "blog/home.html", context)

@login_required
def view_blog(request, title):
    context = {
        "blog": get_object_or_404(Blog, title=title)
    }
    return render(request, "blog/view.html", context)



@login_required
def edit_blog(request, title):
    blog = get_object_or_404(Blog, title=title)
    if request.user == blog.author:
        if request.method == 'POST':
            form = EditBlogForm(request.POST, request.FILES, instance=blog)
            if form.is_valid():
                form.save()
                return redirect('view_blog', title=blog.title)
        else:
            form = EditBlogForm(instance=blog) 
        return render(request, 'blog/edit.html', {'form': form})
    else:
        return HttpResponse("You do not have permission to edit this blog.")

@login_required
def delete_blog(request,title):
    blog = get_object_or_404(Blog, title=title)
    
    if request.user == blog.author:
        if request.method == 'POST':
            blog.delete()
            messages.success(request, 'Blog post deleted successfully.')
            return redirect('list_blog')
        else:
            return render(request, 'blog/home.html', {'blog': blog})
    else:
        messages.error(request, 'You are not authorized to delete this blog post.')
        return redirect('list_blog')
