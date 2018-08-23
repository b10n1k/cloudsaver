from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic

from django.utils import timezone
import datetime

from .models import Idea, Ideas_Group
from .forms import IdeasForm, EditIdeasForm

# Create your views here.
class IndexView(generic.ListView):
    # model = Idea
    template_name = 'ideas/index.html'
    context_object_name = 'latest_ideas_list, ideas_list'

    def get(self, request):
        form = IdeasForm()
        latest_ideas_list = Idea.objects.order_by('-pub_date')
        #ideas_list = Idea.objects.order_by('-pub_date')
        context = {
            'latest_ideas_list': latest_ideas_list[:6],
            'ideas_list': latest_ideas_list,
            'form': form
        }
        return render(request,
                      self.template_name,
                      context)
    
    def post(self, request):
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = IdeasForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                ideapost = form.save(commit=False)
                #ideapost.pub_date=timezone.now()
                ideapost.group=Ideas_Group.objects.last()
                ideapost.save()
        latest_ideas_list = Idea.objects.order_by('-pub_date')[:6]
        context = {
            'latest_ideas_list': latest_ideas_list,
            'form': IdeasForm(),
        }
        return render(request,
                      self.template_name,
                      context)
            # if a GET (or any other method) we'll create a blank form
        #else:
        #   form = IdeasForm() 
    
class DetailView(generic.DetailView):
    model = Idea
    template_name = 'ideas/details.html'
    #idea = get_object_or_404(Idea, pk=id)
    #return render(request, 'ideas/details.html', {'idea': idea})

def editView(request, id):
    #model = Idea
    idea = Idea.objects.get(pk=id)
    template_name = 'ideas/edit.html'
    post = EditIdeasForm(request.POST or None, instance=idea)
    if request.method == 'POST':
        
        if post.is_valid():
            #post = post.save(commit=False)
            #ideapost.pub_date=timezone.now()
            #post.group=Ideas_Group.objects.last()
            post.save()
            print('HEY')
            return redirect('ideas:index',permanent=True)
   
    return render(request, template_name, {'form':post, 'idea':idea})

def addView(request):
    #model = Idea
    template_name = 'ideas/add.html'
    return HttpResponse("Hey your ideas are awesome.")

class AboutView(generic.TemplateView):
    template_name = 'ideas/about.html'

class ContactView(generic.TemplateView):
    template_name = 'ideas/contact.html'
