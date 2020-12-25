from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import IdeaSerializer
from django.urls import reverse
from django.utils import timezone
import datetime

from .models import Idea, Ideas_Group
from .forms import IdeasForm, EditIdeasForm, AddGroupForm

class IdeaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ideas to be viewed or edited.
    """
    queryset = Idea.objects.all().order_by('-pub_date')
    serializer_class = IdeaSerializer

class IdeaApiView(APIView):

    def get(self, request, pk=None):
        res = get_object_or_404(Idea, pk=pk)
        
        return Response ({"msg": res, status:status.HTTP_200_OK})
 
# Create your views here.
class IndexView(generic.ListView):
    # model = Idea
    template_name = 'ideas/index.html'
    context_object_name = 'latest_ideas_list, ideas_list'
    
    #latest_ideas_list = Idea.objects.order_by('-pub_date')
    #paginator = Paginator(latest_ideas_list, 10)
    #latest_ideas_pages = paginator.page(1)
    def get(self, request):
        
        form = IdeasForm()
        latest_ideas_list = Idea.objects.order_by('-pub_date')
        paginator = Paginator(latest_ideas_list, 10)
        latest_ideas_pages = paginator.page(1)
        # ideas_list = Idea.objects.order_by('-pub_date')
        context = {
            'latest_ideas_list': latest_ideas_list[:6],
            'ideas_list': latest_ideas_pages,
            'form': form
        }
        return render(request,
                      self.template_name,
                      context)
    
    def post(self, request):
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            print(request.POST)
            form = IdeasForm(request.POST)
            print(form.is_valid())    
            # check whether it's valid:
            if form.is_valid():
                ideapost = form.save(commit=False)
                #ideapost.pub_date=timezone.now()
                print(form.cleaned_data['group'])
                ideapost.save()

        latest_ideas_list = Idea.objects.order_by('-pub_date')[:6]
        paginator = Paginator(latest_ideas_list, 10)
        latest_ideas_pages = paginator.page(1)
        context = {
            'latest_ideas_list': latest_ideas_list,
            'ideas_list': latest_ideas_pages,
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

    
class DetailMiniView(generic.DetailView):
    model = Idea
    template_name = 'ideas/details_miniview.html'

    
class EditView(generic.UpdateView):
    model=Idea
    template_name = 'ideas/idea_update_form.html'
    form_class = EditIdeasForm
    template_name_suffix = '_update_form'
    #redirect_url="ideas/details.html"
    def get_success_url(self):
        return reverse('ideas:index')
    # def get(self, request, id):
    #     idea = Idea.objects.get(pk=id)
    #     post = EditIdeasForm(request.GET or None, instance=idea)
    #     return render(request, template_name, {'idea': post})
    
    # def post(self, request, pk):
    #     #post = EditIdeasForm(request.POST or None, instance=idea)

    #     if request.method == 'POST':
    #         print('delete' in request.POST)
    #         if 'delete' in request.POST:
    #                 print('Delete method')
    #                 template_name = 'ideas/index.html'
    #                 idea.delete()
    #                 return redirect('ideas:index')
            # else:
            #     if req.is_valid():
            #         #post = post.save(commit=False)
            #         #ideapost.pub_date=timezone.now()
            #         #post.group=Ideas_Group.objects.last()

            #         post.save()
            #         print('HEY')
            #         return redirect('ideas:index', permanent=True) 
        # form = EditIdeasForm(request.POST)
        # print(form.is_valid())    
        # # check whether it's valid:
        # if form.is_valid():
        #     ideapost = form.save(commit=False)
        #     #ideapost.pub_date=timezone.now()
        #     print(form.cleaned_data['group'])
        #     ideapost.save()
        # if request.method == 'POST':
        #     if post.is_valid():
        #         #post = post.save(commit=False)
        #         #ideapost.pub_date=timezone.now()
        #         #post.group=Ideas_Group.objects.last()
        #         post.save()
        #         print('HEY')
        #         return redirect('ideas:index', permanent=True)

            
# def editView(request, id):
#     #model = Idea
#     idea = Idea.objects.get(pk=id)
#     template_name = 'ideas/edit.html'
#     post = EditIdeasForm(request.POST or None, instance=idea)
#     if request.method == 'POST':
#         print('delete' in request.POST)
#         if 'delete' in request.POST:
#                 print('Delete method')
#                 template_name = 'ideas/index.html'
#                 idea.delete()
#                 return redirect('ideas:index')
#         else:
#             if post.is_valid():
#                 #post = post.save(commit=False)
#                 #ideapost.pub_date=timezone.now()
#                 #post.group=Ideas_Group.objects.last()
                
#                 post.save()
#                 print('HEY')
#                 return redirect('ideas:index', permanent=True) 
#     return render(request, template_name, {'form':post, 'idea':idea})


# def deleteView(request, id):
#     idea = Idea.objects.get(pk=id)
#     template_name = 'ideas/index.html'
#     idea.delete()
#     render(request, template_name)

    
def addView(request):
    #model = Idea
    template_name = 'ideas/add.html'
    return HttpResponse("Hey your ideas are awesome.")


class GroupView(generic.ListView):
    model = Idea
    template_name = 'ideas_group_list.html'
    paginate_by = 10
    
    context_object_name = 'group_list'
    
    def get_queryset(self):
      category_slug = get_object_or_404(Ideas_Group,
                                        category_text=self.kwargs['slug'])
      return Idea.objects.filter(group=category_slug)    
    
    
class AddGroup(generic.CreateView):
    model = Ideas_Group
    form = AddGroupForm()
    fields = ['category_text']

    
class AboutView(generic.TemplateView):
    template_name = 'ideas/about.html'

    
class ContactView(generic.TemplateView):
    template_name = 'ideas/contact.html'

    
class LoginView(generic.TemplateView):
    template_name = 'ideas/login.html'

    
def login(request):
    return render(request, 'login.html')


def logout(request):
    logout(request)
    return render(request, 'logout.html')


class SearchResultsView(generic.ListView):
    model = Idea
    template_name = 'ideas/search_results.html'
    context_object_name = 'results_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        results_list = Idea.objects.filter(Q(idea_title__icontains=query) |
                                   Q(idea_text__icontains=query))
        return results_list
