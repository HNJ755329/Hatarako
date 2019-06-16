from django.test import TestCase
from ..models import Post
import uuid
import django
import pymysql

# Create your tests here.
class ModelTests(TestCase):
    def setUp(self):
        Post.objects.create()
        Post.objects.create(contents="はたらく言葉", industory="業界", career="職種", age="年齢", color="#000000")
        print('models/setUp!')

    def test_id_is_uuid(self):
        for post in Post.objects.all():
            print("  uuid : " + str(post.id))
            self.assertIsInstance(post.id, uuid.UUID)
        print('models/id_is_uuid!')

class ModelCreateTests(TestCase):
    def test_is_empty(self):
        post = Post.objects.all()
        self.assertEqual(post.count(), 0)
        print('models/test_is_empty!')

    def test_create_contents(self):
        test_str = '*' * 250
        Post.objects.create(contents="")
        Post.objects.create(contents=test_str)

    def test_create_industory(self):
        test_str_max = '*' * 30
        test_str_overmax = '*' * 31
        Post.objects.create(industory="")
        Post.objects.create(industory=test_str_max)
        # Post.objects.create(industory=test_str_overmax)
        # 最大値以上の値でエラーが出るか検証
        self.assertRaises(django.db.utils.DataError, Post.objects.create, industory=test_str_overmax)

    def test_create_career(self):
        test_str_max = '*' * 30
        test_str_overmax = '*' * 31
        Post.objects.create(career="")
        Post.objects.create(career=test_str_max)
        self.assertRaises(django.db.utils.DataError, Post.objects.create, career=test_str_overmax)

    def test_create_age(self):
        test_str_max = '*' * 20
        test_str_overmax = '*' * 21
        Post.objects.create(age="")
        Post.objects.create(age=test_str_max)
        self.assertRaises(django.db.utils.DataError, Post.objects.create, age=test_str_overmax)

    def test_create_color(self):
        test_str_max = '*' * 7
        test_str_overmax = '*' * 8
        Post.objects.create(color="")
        Post.objects.create(color=test_str_max)
        self.assertRaises(django.db.utils.DataError, Post.objects.create, color=test_str_overmax)
