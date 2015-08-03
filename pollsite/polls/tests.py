import datetime

from django.test import TestCase
from django.utils import timezone

from polls.models import Question, Choice

class QuestionModelTest(TestCase):

    def setUp(self):
        self.q1 = Question()
        self.q1.question_text = "What is your question?"
        self.q1.pub_date = timezone.now()
        self.q1.save()

        self.q2 = Question()
        self.q2.question_text = "What is your next question?"
        self.q2.pub_date = timezone.now()
        self.q2.save()

    def tearDown(self):
        pass

    def test_save_and_retrieve_Question(self):
        saved_items = Question.objects.all()
        self.assertEqual(saved_items.count(), 2)
        self.assertEqual(saved_items[0].question_text, self.q1.question_text)
        self.assertEqual(saved_items[1].question_text, self.q2.question_text)

    def test_save_and_retrieve_Choice(self):
        self.q1.choice_set.create(choice_text = 'Choice 1', votes=0)
        self.q1.choice_set.create(choice_text = "Choice 2", votes=1)

        saved_items = Choice.objects.all()
        self.assertEqual(saved_items.count(), 2)
        self.assertEqual(saved_items[0].choice_text, "Choice 1")
        self.assertEqual(saved_items[1].choice_text, "Choice 2")
