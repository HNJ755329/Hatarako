from django.test import TestCase
from django_webtest import WebTest
from ..forms import PostForm
from ..models import Post

# Create your tests here.
class PostViewTest(WebTest):
    def setUp(self):
        self.post = Post.objects.create()

    def test_view_page(self):
        page = self.app.get(self.post.get_absolute_url())
        print(page.forms)
        self.assertEqual(len(page.forms), 1)
    """
    def test_form_error(self):
        page = self.app.get(self.post.get_absolute_url())
        response = page.form.submit('submit')
        # print(response.content)
        self.assertContains(response.content, 'This field is required.')

    def test_form_success(self):
        page = self.app.get(self.post.get_absolute_url())
        page.form['contents'] = "はたらく言葉"
        page.form['industory'] = "業界"
        page.form['career'] = "職種"
        page.form['age'] = "年齢"
        page.form['color'] = "#000000"
        response = page.form.submit('submit')
        print(response.content)
        # self.assertRedirects(response, '/result')
    """