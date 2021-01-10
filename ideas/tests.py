import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Idea, Ideas_Group
from django.urls import reverse 


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
        mock_group = Ideas_Group.objects.create(category_text="test")
        mock_idea = Idea.objects.create(idea_title="bbb", idea_text="testtxt", group=mock_group)
        response = self.client.post(reverse("ideas:edit",
                                            kwargs={'pk': mock_idea.pk}),
                                    {'idea_title': 'updated',
                                     'idea_text': 'testtxt',
                                     'idea_repo': '',
                                     'idea_owner': '',
                                     'idea_status': '',
                                     'group': mock_group.id} )
        self.assertEqual(response.status_code, 302)
        mock_idea.refresh_from_db()
        self.assertEquals(mock_idea.idea_title, 'updated')
