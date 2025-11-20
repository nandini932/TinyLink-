from django.test import TestCase
from .models import Link

class LinkTests(TestCase):
    def test_healthz(self):
        response = self.client.get('/api/healthz/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"ok": True, "version": "1.0"})

    def test_create_link(self):
        data = {"target_url": "https://example.com"}
        response = self.client.post('/api/links/', data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('code', response.json())

    def test_create_link_custom_code(self):
        data = {"target_url": "https://example.com", "code": "test123"}
        response = self.client.post('/api/links/', data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['code'], 'test123')

    def test_create_link_duplicate_code(self):
        Link.objects.create(code='dup', target_url='https://dup.com')
        data = {"target_url": "https://example.com", "code": "dup"}
        response = self.client.post('/api/links/', data, content_type='application/json')
        self.assertEqual(response.status_code, 409)

    def test_list_links(self):
        Link.objects.create(code='abc', target_url='https://abc.com')
        response = self.client.get('/api/links/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_get_link_stats(self):
        link = Link.objects.create(code='stats', target_url='https://stats.com')
        response = self.client.get(f'/api/links/{link.code}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 'stats')

    def test_delete_link(self):
        link = Link.objects.create(code='del', target_url='https://del.com')
        response = self.client.delete(f'/api/links/{link.code}/')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Link.objects.filter(code='del').exists())

    def test_redirect(self):
        link = Link.objects.create(code='redir', target_url='https://redir.com')
        response = self.client.get(f'/{link.code}/')
        self.assertEqual(response.status_code, 302)
        link.refresh_from_db()
        self.assertEqual(link.clicks, 1)

    def test_redirect_not_found(self):
        response = self.client.get('/nonexistent/')
        self.assertEqual(response.status_code, 404)