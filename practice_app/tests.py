from django.test import TestCase
from .models import PracticeModel


class ModelTests(TestCase):

    def setUp(self):
        self.user = PracticeModel.objects.create(
            name="Test Model",
            description="This is a test model",
            slug="test-model"
        )

    def test_model_str(self):
        practice_model = PracticeModel(name="Test Model",
                                       description="This is a test model",
                                       slug="test-model")
        self.assertEqual(str(practice_model), "Test Model")

    def test_models_count(self):
        self.assertEqual(PracticeModel.objects.count(), 1)
