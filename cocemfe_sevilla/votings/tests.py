from django.test import TestCase
from django.urls import reverse

from datetime import datetime, timedelta

from documents.models import Document
from professionals.models import Professional
from suggestions.models import Suggestion
from votings.models import Voting

class VotingStatisticsTestCase(TestCase):
    def setUp(self):
        self.document = Document.objects.create(
            name="Documento de prueba",
            status="Votaciones",
            suggestion_start_date=datetime.now() - timedelta(days=5),
            suggestion_end_date=datetime.now() + timedelta(days=5),
            voting_start_date=datetime.now() - timedelta(days=3),
            voting_end_date=datetime.now() + timedelta(days=3),
        )
        self.professional1 = Professional.objects.create(username="Profesional 1")
        self.professional2 = Professional.objects.create(username="Profesional 2")
        self.document.professionals.add(self.professional1, self.professional2)
        self.suggestion1 = Suggestion.objects.create(
            main="Sugerencia 1",
            justification="Justificación 1",
            relevance="Importante",
            section="Sección 1",
            page=1,
            date=datetime.now() - timedelta(days=4),
            professional=self.professional1,
            document=self.document,
        )
        self.suggestion2 = Suggestion.objects.create(
            main="Sugerencia 2",
            justification="Justificación 2",
            relevance="Poco importante",
            section="Sección 2",
            page=2,
            date=datetime.now() - timedelta(days=3),
            professional=self.professional2,
            document=self.document,
        )
        self.vote1 = Voting.objects.create(
            vote=True,
            date=datetime.now() - timedelta(days=2),
            justification="Voto a favor",
            professional=self.professional1,
            suggestion=self.suggestion1,
        )
        self.vote2 = Voting.objects.create(
            vote=False,
            date=datetime.now() - timedelta(days=1),
            justification="Voto en contra",
            professional=self.professional2,
            suggestion=self.suggestion1,
        )

    def test_voting_statistics_view_with_valid_document_id(self):
        url = reverse('votings:voting_statistics', kwargs={'pk': self.document.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'voting_statistics.html')

    def test_voting_statistics_view_with_invalid_document_id(self):
        invalid_document_id = self.document.pk + 100
        url = reverse('votings:voting_statistics', kwargs={'pk': invalid_document_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_voting_statistics_view_without_suggestions(self):
        self.suggestion1.delete()
        self.suggestion2.delete()
        url = reverse('votings:voting_statistics', kwargs={'pk': self.document.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'voting_statistics.html')

    def test_voting_statistics_view_without_votes(self):
        self.suggestion1.votings.all().delete()
        self.suggestion2.votings.all().delete()
        url = reverse('votings:voting_statistics', kwargs={'pk': self.document.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'voting_statistics.html')
        self.assertEqual(response.context['suggestion_data'][0]['votes_agree'], 0)
        self.assertEqual(response.context['suggestion_data'][0]['votes_disagree'], 0)

    def test_voting_statistics_view_without_remaining_professionals(self):
        self.document.professionals.clear()
        url = reverse('votings:voting_statistics', kwargs={'pk': self.document.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'voting_statistics.html')
        self.assertEqual(response.context['suggestion_data'][0]['professionals_remaining'], 0)

    def test_voting_statistics_view_totals(self):
        Voting.objects.create(
            vote=False,
            date=datetime.now() - timedelta(days=1),
            justification="Voto en contra",
            professional=self.professional2,
            suggestion=self.suggestion1,
        )
        url = reverse('votings:voting_statistics', kwargs={'pk': self.document.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'voting_statistics.html')
        self.assertEqual(response.context['suggestion_data'][0]['votes_agree'], 1)
        self.assertEqual(response.context['suggestion_data'][0]['votes_disagree'], 2)
