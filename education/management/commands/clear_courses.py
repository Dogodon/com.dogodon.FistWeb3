from django.core.management.base import BaseCommand
from education.models import Course, Quiz, Choice

class Command(BaseCommand):
    help = "Supprime tous les cours, quiz et choix"

    def handle(self, *args, **kwargs):
        Choice.objects.all().delete()
        Quiz.objects.all().delete()
        Course.objects.all().delete()

        self.stdout.write(self.style.SUCCESS("Tous les cours, quiz et choix ont été supprimés."))
