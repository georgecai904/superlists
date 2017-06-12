from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string

# Create your tests here.
# class SmokeTest(TestCase):
#
#     def test_bad_math(self):
#         self.assertEqual(1 + 1, 3)

def remove_csrf(html_code):
    import re
    csrf_regex = r"<input (.)+ name='csrfmiddlewaretoken' (.)+ />"
    return re.sub(csrf_regex, '', html_code)

class HomePageTest(TestCase):

    def test_root_url_resolvess_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html= render_to_string("lists/home.html", request=request)
        self.assertEqual(remove_csrf(response.content.decode()), remove_csrf(expected_html))

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)
        self.assertIn('A new list item', response.content.decode())
        expected_html = render_to_string(
            'lists/home.html',
            {'new_item_text': 'A new list item'},
            request=request
        )
        self.assertEqual(remove_csrf(response.content.decode()), remove_csrf(expected_html))
