from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Tree

# Create your tests here.
class TreeTests(TestCase):
    tree = Tree(name='pine')

    def setUp(self):
        """runs BEFORE EACH test"""
        self.user = get_user_model().objects.create_user(
            username='tester',
            email='tester@email.com',
            password='pass'
        )

        self.tree = Tree.objects.create(
            name = 'pine',
            planter = self.user,
            description = 'smells like pine!'
        )

    def test_str(self):
        """checks __str__"""
        tree = Tree(name='pine')
        self.assertEqual(str(tree), tree.name)

    def test_tree_info(self):
        """tests the tree created holds the information it was given"""
        self.assertEqual(f'{self.tree.name}', 'pine')
        self.assertEqual(f'{self.tree.planter}', 'tester')
        self.assertEqual(f'{self.tree.description}', 'smells like pine!')

    def test_list_view(self):
        response = self.client.get(reverse('tree_list'))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, 'Tree - pine')
        self.assertTemplateUsed(response, 'tree_list.html')

    def test_detail_view(self):
        response = self.client.get(reverse('tree_details', args='1'))
        no_response = self.client.get('/trees/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'smells like pine!')
        self.assertTemplateUsed(response, 'tree_details.html')

    def test_create_view(self):
        response = self.client.post(reverse('tree_create'), {
            'name': 'maple',
            'planter': self.user,
            'description': 'big leaf',
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'maple')
        self.assertContains(response, 'big leaf')
        self.assertTemplateUsed(response, 'tree_create.html')

    def test_update_view(self):
        response = self.client.post(reverse('tree_update',args='1'), {
            'name': 'Updated name',
            'description': 'Updated description',
        })
        self.assertEqual(response.status_code, 302)


    def test_update_view_redirect(self):
        response = self.client.post(reverse('tree_update',args='1'), {
            'name': 'Updated name',
            'description': 'Updated description',
        }, follow=True)

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'Updated name')

        self.assertTemplateUsed('tree_detail.html')

    def test_snack_delete_view(self):
        response = self.client.get(reverse('tree_delete',args='1'))
        self.assertEqual(response.status_code, 200)

# python manage.py test