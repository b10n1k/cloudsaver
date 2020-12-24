import datetime

from django.test import TestCase, Client
from django.utils import timezone
from .models import Idea, Ideas_Group


class IdeasModelTests(TestCase):

    def SetUp(self):
        test_group = Ideas_Group.objects.create(category_text="test")
        test_idea = Idea.objects.create(idea_title='unittest',
                                        idea_text='works',
                                        group=test_group)

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_idea = Idea(pub_date=time)
        self.assertIs(future_idea.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_idea = Idea(pub_date=time)
        self.assertIs(old_idea.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_idea = Idea(pub_date=time)
        self.assertIs(recent_idea.was_published_recently(), True)


    def test_can_update_Idea(self):
        #idea = Idea(idea_title="New")
        c = Client()
        #idea = Idea.objects.get(idea_title='unittest')
        testid = Idea(1,"bbb","testtxt")
        c.post('/idea/%s/edit/' % testid.id, {'idea_title': 'updated'} )
        self.assertEquals(testid.idea_title, 'updated')
