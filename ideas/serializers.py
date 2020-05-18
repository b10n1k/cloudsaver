from .models import Idea 
from rest_framework import serializers


class IdeaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Idea
        fields = ['idea_title', 'idea_text', 'idea_repo',
                  'idea_owner', 'idea_status','group']

