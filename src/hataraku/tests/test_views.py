from django.test import TestCase
from django.test import RequestFactory
from django.views.generic.base import TemplateView
from ..models import Post
from ..views import *

# Create your tests here.
class ViewPostCreateTests(TestCase):
    """Test whether our post entries show up on the page"""
    def setUp(self):
        pass

    def test_result_nondata(self):
        response = self.client.get('/result')
        self.assertEqual(response.status_code, 200)

    def test_result_not_Valid_data(self):     
        data = {
            'contents': 'はたらく言葉',
            'industory': '業界',
        }
        factory = RequestFactory()
        request = factory.post('/result', data)
        response = hataraku_result(request)
        self.assertEqual(response.status_code, 200)

    def test_result_Valid_data(self):     
        data = {
            'contents': 'はたらく言葉',
            'industory': '業界',
            'career' : "職種",
            'age' : "年齢",
            'color' : "#00FF00",
        }
        factory = RequestFactory()
        request = factory.post('/result', data=data)
        response = hataraku_result(request)
        self.assertEqual(response.status_code, 200)

    def test_one_post(self):
        Post.objects.create(contents="はたらく言葉", industory="業界", career="職種", age="年齢", color="#000000")
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'はたらく言葉')
        self.assertContains(response, '業界／職種・年齢')

    def test_one_post_uuid(self):
        post = Post.objects.create(contents="はたらく言葉", industory="業界", career="職種", age="年齢", color="#000000")
        response = self.client.get(post.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'はたらく言葉')
        self.assertContains(response, '業界／職種・年齢')

    def test_two_posts(self):
        Post.objects.create(contents="はたらく言葉1", industory="業界1", career="職種1", age="年齢1", color="#000001")
        Post.objects.create(contents="はたらく言葉2", industory="業界2", career="職種2", age="年齢2", color="#000002")
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'はたらく言葉1')
        self.assertContains(response, 'はたらく言葉2')
    
    def test_huge_posts(self):
        sample_N = 11
        post_list = []
        for i in range(sample_N):
            post_list.append(Post.objects.create(contents="contents_" + str(i) ))
        response = self.client.get('/')
        for j in range(sample_N):
            if j == 0:
                # 表示できるのは10個まで。古い順から見えなくなる。
                self.assertNotContains(response, "contents_" + str(j))
            else:
                self.assertContains(response, "contents_" + str(j))
        # 0番目に移動すると内容が見れる。
        response = self.client.get(post_list[0].get_absolute_url())
        self.assertContains(response, "contents_" + str(0))
