from django.test import TestCase
from ..models import Post

import uuid
import django
import datetime

# Create your tests here.
class ModelPostTests(TestCase):
    def setUp(self):
        Post.objects.create()
        Post.objects.create(created_on="fail-time")
        # Post.objects.create(id="fail-id") -> django.core.exceptions.ValidationError
        Post.objects.create(contents="はたらく言葉", industory="業界", career="職種", age="年齢", color="#000000")
        print('models/setUp!')

    def test_delete(self):
        Post.objects.all().delete()
        print('models/delete')

    def test_id_is_uuid(self):
        for post in Post.objects.all():
            print("  uuid : " + str(post.id))
            self.assertIsInstance(post.id, uuid.UUID)
        print('models/id_is_uuid!')

    def test_created_on(self):
        for post in Post.objects.all():
            print("  created_on : " + str(post.created_on))
            # setUpで作ったデータのインスタンスの判定
            self.assertIsInstance(post.created_on, datetime.datetime)
            # setUpで作ったデータが過去のものか判定。比較可能のためにtimezone=Noneとする。
            self.assertLessEqual(post.created_on.replace(tzinfo=None), datetime.datetime.now())
        print('models/created_on!')

class ModelPostCreateTests(TestCase):
    def test_is_empty(self):
        post = Post.objects.all()
        self.assertEqual(post.count(), 0)
        print('models/test_is_empty!')
    
    def test_create_huge_data(self):
        for i in range(1000):
            try:
                Post.objects.create()
            except:
                self.fail('create huge data error!!')
                break
        print("create_object_num : " + str(i + 1) )

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

    def test_create_id(self):
        test_str = '*' * 10
        self.assertRaises(django.core.exceptions.ValidationError, Post.objects.create, id="")
        self.assertRaises(django.core.exceptions.ValidationError, Post.objects.create, id=test_str)

    def test_create_created_on(self):
        test_str = '*' * 10
        Post.objects.create(created_on="")
        Post.objects.create(created_on=test_str)
        #self.assertRaises(django.core.exceptions.ValidationError, Post.objects.create, created_on="")
        #self.assertRaises(django.core.exceptions.ValidationError, Post.objects.create, created_on=test_str)

    def test_create_FalseKey(self):
        test_str = '*' * 10
        self.assertRaises(TypeError, Post.objects.create, FalseKey="")
        self.assertRaises(TypeError, Post.objects.create, FalseKey=test_str)
