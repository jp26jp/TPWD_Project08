from io import StringIO
from django.core.management import call_command
from django.utils import timezone
from django.urls import reverse
from django.test import TestCase

from .models import Mineral


class MineralModelTests(TestCase):
    def setUp(self):
        self.mineral1 = Mineral.objects.create(name="A Cool Name")
        self.mineral2 = Mineral.objects.create(name="A Different Name")

    def test_mineral_creation(self):
        now = timezone.now()
        self.assertLess(self.mineral1.created_at, now)

    def test_slug_generation(self):
        self.assertTrue(self.mineral1.slug == "a-cool-name")

    def test_string_representation(self):
        mineral = Mineral.objects.create(name="A cool rock")
        self.assertEqual(str(mineral), mineral.name)

    def test_management_commands(self):
        out = StringIO()
        call_command('add_minerals_to_database', stdout=out)
        self.assertIn('Mineral data has been successfully added!', out.getvalue())


class MineralViewsTests(TestCase):
    def setUp(self):
        self.mineral1 = Mineral.objects.create(name="A Cool Name")
        self.mineral2 = Mineral.objects.create(name="Different Name", group="Random Things")

    def test_mineral_list_view(self):
        resp = self.client.get(reverse('minerals:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral1, resp.context['minerals'])
        self.assertIn(self.mineral2, resp.context['minerals'])

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('minerals:detail', kwargs={'slug': self.mineral1.slug}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral1, resp.context['mineral'])

    def test_mineral_letter_view(self):
        resp = self.client.get(reverse('minerals:letter', kwargs={'letter': "d"}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral2, resp.context['minerals'][0])

    def test_mineral_group_view(self):
        resp = self.client.get(reverse('minerals:group', kwargs={'group': "random"}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral2, resp.context['minerals'][0])

