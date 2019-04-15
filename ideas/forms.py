from django import forms
from ideas.models import Idea, Ideas_Group
from django.forms.models import inlineformset_factory

class IdeasForm(forms.ModelForm):
    idea_title = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':"do you have a name for your idea",
        'aria-describedby':"basic-addon1",}))
    
    idea_text = forms.CharField(widget=forms.Textarea(attrs={
                                    'class':'form-control',
                                    'placeholder':"what s the idea man",
                                    'aria-describedby':"basic-addon1",
                                    'rows':"10"}),
                                max_length=200,)
    
    group = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':"Category",
        'aria-describedby':"basic-addon1",}))

    idea_repo = forms.URLField(widget=forms.URLInput(attrs={
        'class':'form-control',
        'placeholder':"repo",
        'aria-describedby':"basic-addon1",}),
                               required=False)
    
    class Meta:
        model = Idea
        fields = ('idea_title',
                  'idea_text',
                  'group',
                  'idea_repo',)

    def clean(self):
        # group = self.cleaned_data.get('group')
        group, created = Ideas_Group.objects.get_or_create(
                    category_text=self.cleaned_data.get('group'))
        self.cleaned_data['group'] = group
        return super(IdeasForm, self).clean()
    
    def save(self, commit=True):
        group, created = Ideas_Group.objects.get_or_create(
                    category_text=self.cleaned_data.get('group'))
        print(11111)
        self.cleaned_data['group'] = group
        #self.group = group_new.id
        print(222222)
        return super(IdeasForm, self).save(commit)
    
class EditIdeasForm(forms.ModelForm):
    idea_title = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':"do you have a name for your idea",
        'aria-describedby':"basic-addon1",}))
    
    idea_text = forms.CharField(widget=forms.Textarea(attrs={
                                    'class':'form-control',
                                    'placeholder':"what s the idea man",
                                    'aria-describedby':"basic-addon1",
                                    'rows':"10" }),
                                max_length=200,)
    
    idea_repo = forms.URLField(widget=forms.URLInput(attrs={
        'class':'form-control',
        'placeholder':"repo",
        'aria-describedby':"basic-addon1",}),
                               required=False)

    #idea_repo.widget.attrs.update(
    class Meta:
        model = Idea
        fields = ('idea_title',
                  'idea_text',
                  'idea_repo',
                  'idea_owner',
                  'idea_status',
                  'group')
        

    #def save(self, commit=True):


     #   if commit:
            
class AddGroupForm(forms.ModelForm):
    category_text = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':"New Group",
        'aria-describedby':"basic-addon1",}))

    class Meta:
        model = Ideas_Group
        fields = ('category_text',)
