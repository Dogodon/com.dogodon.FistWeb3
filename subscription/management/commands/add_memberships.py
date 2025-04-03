# education/management/commands/add_memberships.py
from django.core.management.base import BaseCommand
from subscription.models import Membership, UserMembership
from authentication.models import User

class Command(BaseCommand):
    help = 'Ajoute des memberships et associe-les à des utilisateurs'

    def handle(self, *args, **kwargs):
        # Exemple de données de memberships
        memberships = [
            {'membership_type': 'Extended', 'duration': 60, 'duration_period': 'Days', 'price': 60.00},
            {'membership_type': 'Advanced', 'duration': 60, 'duration_period': 'Days', 'price': 45.00},
            {'membership_type': 'Medium', 'duration': 12, 'duration_period': 'Months', 'price': 100.00},
            {'membership_type': 'Basic', 'duration': 30, 'duration_period': 'Days', 'price': 20.00},
            {'membership_type': 'Free', 'duration': 6, 'duration_period': 'Months', 'price': 0.00},
        ]

        # Ajout des memberships
        for membership_data in memberships:
            membership, created = Membership.objects.get_or_create(**membership_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Le membership {membership.membership_type} a été ajouté avec succès."))
            else:
                self.stdout.write(self.style.WARNING(f"Le membership {membership.membership_type} existe déjà."))

        # Exemple de données d'utilisateurs à associer avec un membership
        users = User.objects.all()  # Récupère tous les utilisateurs (ou spécifie des utilisateurs spécifiques)
        for user in users:
            # Exemple d'association d'un utilisateur avec un membership
            user_membership = UserMembership.objects.create(user=user, membership=membership)
            self.stdout.write(self.style.SUCCESS(f"L'utilisateur {user.username} a été associé au membership {membership.membership_type}."))
