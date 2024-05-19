from django.test import TestCase
from chat_messages.models import ChatMessage
from chat_messages.forms import MessageForm
from chat_messages.admin import ChatMessageAdmin
from documents.models import Document
from professionals.models import Professional
from django.contrib.admin.sites import AdminSite
from django.utils import timezone

class ChatMessageAdminTest(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.chat_message_admin = ChatMessageAdmin(model=ChatMessage, admin_site=self.site)

    def test_list_display_contains_fields(self):
        self.assertIn('author', self.chat_message_admin.list_display)
        self.assertIn('content', self.chat_message_admin.list_display)
        self.assertIn('post_date', self.chat_message_admin.list_display)
        self.assertIn('document', self.chat_message_admin.list_display)

    def test_search_fields_contains_id(self):
        self.assertIn('id', self.chat_message_admin.search_fields)

    def test_icon_name_is_comment(self):
        self.assertEqual(self.chat_message_admin.icon_name, 'comment')

class ChatMessageFormTest(TestCase):
    def setUp(self):
        self.document = Document.objects.create(name='Test Document')
        self.professional = Professional.objects.create(username='testuser', email='test@example.com')

    def test_valid_form(self):
        data = {'content': 'This is a test message'}
        form = MessageForm(data=data)
        self.assertTrue(form.is_valid())

    def test_empty_content(self):
        data = {'content': ''}
        form = MessageForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors)

    def test_content_max_length(self):
        content = 'a' * 501
        data = {'content': content}
        form = MessageForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors)

    def test_missing_content(self):
        data = {}
        form = MessageForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors)

    def test_valid_form_with_document_and_author(self):
        data = {
            'content': 'This is a test message',
            'author': self.professional,
            'document': self.document,
            }
        form = MessageForm(data=data)
        self.assertTrue(form.is_valid())

        chat_message = form.save(commit=False)
        chat_message.document = self.document
        chat_message.author = self.professional
        chat_message.save()

        self.assertIsNotNone(chat_message.id)