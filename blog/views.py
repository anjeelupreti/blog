from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Blog
from blog.form import AddBlogForm, EditBlogForm

@login_required
def add_blog(request):
    form = AddBlogForm()
    if request.method == "POST":
        form = AddBlogForm(request.POST, request.FILES or None)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user  # Assuming Blog model has an author field
            blog.save()
            messages.success(request, 'Blog post added successfully.')
            return redirect('/blog/')
        else:
            messages.error(request, 'There was an error adding the blog post.')
    context = {"data": "this is blog add form", "form": form}
    return render(request, 'blog/add.html', context)

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
    blog_data = get_object_or_404(Blog, title=title)
    if blog_data.author != request.user:
        messages.error(request, 'You do not have permission to edit this blog post.')
        return redirect('/blog/')  # Or some kind of "permission denied" response

    if request.method == 'POST':
        form = EditBlogForm(request.POST, request.FILES or None, instance=blog_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog post updated successfully.')
            return redirect('/blog/')
        else:
            messages.error(request, 'There was an error updating the blog post.')
    else:
        form = EditBlogForm(instance=blog_data)

    context = {
        "data": blog_data,
        "form": form
    }
    return render(request, 'blog/edit.html', context)

@login_required
def delete_blog(request, title):
    blog_data = get_object_or_404(Blog, title=title)
    if blog_data.author != request.user:
        messages.error(request, 'You do not have permission to delete this blog post.')
        return redirect('/blog/') 

    blog_data.delete()
    messages.success(request, 'Blog post deleted successfully.')
    return redirect('/blog/')
