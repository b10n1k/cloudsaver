from django import forms
from ideas.models import Idea

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
                  'idea_repo',)

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
            
        
