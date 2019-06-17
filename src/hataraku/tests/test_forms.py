from django.test import TestCase
from ..forms import PostForm
from ..models import Post

# Create your tests here.
class PostFormTest(TestCase):
    def setUp(self):
        # self.post = Post.objects.create(contents="contents", industory="industory")
        pass

    def test_valid_data(self):
        form = PostForm({
            'contents': "コンテンツ",
            'industory': "業界",
            'career': "職種",
            'age': "年齢",
            'color' : "#00FF00"
        })
        self.assertTrue(form.is_valid())
        post = form.save()
        self.assertEqual(post.contents, "コンテンツ")
        self.assertEqual(post.industory, "業界")
        self.assertEqual(post.career, "職種")
        self.assertEqual(post.age, "年齢")
        self.assertEqual(post.color, "#00FF00")

    def test_blank_data(self):
        form = PostForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'contents': ['This field is required.'],
            'industory': ['This field is required.'],
            'career': ['This field is required.'],
            'age': ['This field is required.'],
            'color': ['This field is required.'],
        })
