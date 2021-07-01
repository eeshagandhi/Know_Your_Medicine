from django.urls.base import reverse
from accounts.decorators import unauthenticated_user
from display.models import Category, medicine_data, post
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from display.models import medicine_data, post, Category,comment
from .forms import CommentForm, EditForm, MedForm, MedSearchForm, FeedbackForm, AddForm, EditForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
# Create your views here.
class profile(ListView):
    model= post
    template_name= 'profile.html'
def home(request):
    return render(request,'home.html')
@login_required(login_url='login')
def main(request):
    return render(request, 'main.html')
def about(request):
    return render(request, 'about.html')
def search(request):
    #queryset=medicine_data.objects.all()
    form=MedSearchForm(request.POST or None)
    context={
        #"queryset":queryset,
        "form":form,
    }
    if request.method == 'POST':
        queryset = medicine_data.objects.all().order_by('-id').filter(Prescribed_medicine__icontains=form['Prescribed_medicine'].value(),Disease__icontains=form['Disease'].value())
        context = {
        "queryset": queryset,
        "form": form,
        }
        if queryset.exists():
            return render(request, 'search.html',context)
        else:
            messages.info(request,'Data not found')
    return render(request, 'search.html',context)

@login_required(login_url='login')
def feedback(request):
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        "form": form,
    }
    return render(request, 'feedback.html',context)

class add_comment(CreateView):
    model=comment
    form_class=CommentForm
    template_name='add_comment.html'
    success_url=reverse_lazy('check')

    def form_valid(self, form):
        form.instance.med_id=self.kwargs['id']
        return super().form_valid(form)
def med_edit(request, id=None):  
 instance = get_object_or_404(medicine_data, id=id)
 form = MedForm(request.POST or None, instance=instance)
 if form.is_valid():
    instance = form.save(commit=False)
    instance.save()
    return redirect('check')
 context = {
     "title": 'Edit ' + str(instance.Prescribed_medicine),
     "instance": instance,
     "form": form,
   }
 return render(request, "feedback.html", context)
@login_required(login_url='login')
def check(request):
    form=MedSearchForm(request.POST or None)
    context={
        "form":form,
    }
    if request.method == 'POST':
        queryset = medicine_data.objects.all().order_by('-id').filter(Prescribed_medicine__icontains=form['Prescribed_medicine'].value(),Disease__icontains=form['Disease'].value())
        context = {
        "queryset": queryset,
        "form": form,
        }
        if queryset.exists():
            messages.info(request,'Data already exists, Click on the medicine name to provide additional info')
            return render(request, 'check.html',context)
        else:
            return redirect('feedback')
    return render(request, 'check.html',context)
class blog(ListView):
    model= post
    template_name= 'blog.html'
    ordering=['-id']

    def get_context_data(self,*args, **kwargs):
        cat_menu=Category.objects.all()
        context=super(blog, self).get_context_data(*args, **kwargs)
        context["cat_menu"]=cat_menu
        return context
class post_details(DetailView):
    model=post
    template_name="post_details.html"
    def get_context_data(self,*args, **kwargs):
        cat_menu=Category.objects.all()
        context=super(post_details, self).get_context_data(*args, **kwargs)
        collection= get_object_or_404(post, id=self.kwargs['pk'])
        total_likes=collection.total_likes()
        context["cat_menu"]=cat_menu
        context["total_likes"]=total_likes
        return context

#@login_required(login_url='accounts/login')
#def add_post(request):
 #   form = AddForm(request.POST or None)
  #  if form.is_valid():
   #     form.save()
    #context = {
     #   "form": form,
      #  }
    #return render(request, 'add_post.html',context)
class add_post(CreateView):
    model=post
    form_class=AddForm
    template_name='add_post.html'
    def get_context_data(self,*args, **kwargs):
        cat_menu=Category.objects.all()
        context=super(add_post, self).get_context_data(*args, **kwargs)
        context["cat_menu"]=cat_menu
        return context
class add_category(CreateView):
    model=Category
    template_name='add_category.html'
    fields='__all__'
    def get_context_data(self,*args, **kwargs):
        cat_menu=Category.objects.all()
        context=super(add_category, self).get_context_data(*args, **kwargs)
        context["cat_menu"]=cat_menu
        return context
def category(request,cat):
    specific_posts= post.objects.filter(category=cat)
    return render(request, 'categories.html', {'cat':cat.title(),'specific_posts':specific_posts})

def likes(request, pk):
    bpost = get_object_or_404(post, id=request.POST.get('post_id'))
    bpost.likes.add(request.user)
    return HttpResponseRedirect(reverse('post_details', args=[str(pk)]))

class edit_post(UpdateView):
    model=post
    form_class=EditForm
    template_name='edit_post.html'
    def get_context_data(self,*args, **kwargs):
        cat_menu=Category.objects.all()
        context=super(edit_post, self).get_context_data(*args, **kwargs)
        context["cat_menu"]=cat_menu
        return context
    
class delete_post(DeleteView):
    model=post
    template_name='delete_post.html'
    success_url=reverse_lazy('blog')
    def get_context_data(self,*args, **kwargs):
        cat_menu=Category.objects.all()
        context=super(delete_post, self).get_context_data(*args, **kwargs)
        context["cat_menu"]=cat_menu
        return context
