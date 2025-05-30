# # from django.core.management.base import BaseCommand
# # from education.models import Course, Quiz
# # from django.contrib.auth import get_user_model

# # User = get_user_model()  # Récupère le modèle utilisateur défini dans AUTH_USER_MODEL

# # class Command(BaseCommand):
# #     help = "Ajoute des cours et des quiz à la base de données"

# #     def handle(self, *args, **kwargs):
# #         courses_data = [
# #             {
# #                 "title": "Introduction à la Gestion Financière",
# #                 "description": "Apprenez les bases de la gestion de votre argent.",
# #                 "is_unlocked": True,
# #                 "quizzes": [
# #                     {"question": "Que signifie le terme 'budget' ?", "answer": "Plan de dépenses"},
# #                     {"question": "Pourquoi est-il important d’économiser ?", "answer": "Sécurité financière"},
# #                     {"question": "Que représente un revenu ?", "answer": "Argent gagné"},
# #                     {"question": "Qu'est-ce qu'une dépense fixe ?", "answer": "Dépense récurrente"},
# #                     {"question": "Pourquoi faut-il éviter les dettes excessives ?", "answer": "Risque financier"},
# #                     {"question": "Que signifie 'intérêt composé' ?", "answer": "Intérêt sur intérêt"},
# #                     {"question": "Qu'est-ce qu'un investissement ?", "answer": "Placement d'argent"},
# #                     {"question": "Pourquoi diversifier ses investissements ?", "answer": "Réduction des risques"},
# #                     {"question": "Comment définir un objectif financier ?", "answer": "But d'épargne"},
# #                     {"question": "Qu'est-ce qu'une épargne d'urgence ?", "answer": "Fonds en cas d'imprévu"},
# #                 ]
# #             },
# #             {
# #                 "title": "Épargne et Budget",
# #                 "description": "Apprenez à établir un budget et à épargner efficacement.",
# #                 "is_unlocked": False,
# #                 "quizzes": [
# #                     {"question": "Quelle est la règle des 50/30/20 ?", "answer": "Budget en 3 catégories"},
# #                     {"question": "Quelle est l’utilité d’un fonds d’urgence ?", "answer": "Préparer les imprévus"},
# #                     # Ajoute 8 autres questions...
# #                 ]
# #             },
# #             {
# #                 "title": "Gestion des Dettes",
# #                 "description": "Comprenez comment gérer et réduire vos dettes.",
# #                 "is_unlocked": False,
# #                 "quizzes": [
# #                     {"question": "Qu'est-ce qu'un crédit à la consommation ?", "answer": "Prêt pour achats"},
# #                     # Ajoute 9 autres questions...
# #                 ]
# #             },
# #             {
# #                 "title": "Investissements",
# #                 "description": "Découvrez les bases de l’investissement et du placement d’argent.",
# #                 "is_unlocked": False,
# #                 "quizzes": [
# #                     {"question": "Qu'est-ce qu'une action ?", "answer": "Part d'une entreprise"},
# #                     # Ajoute 9 autres questions...
# #                 ]
# #             },
# #             {
# #                 "title": "Planification Financière",
# #                 "description": "Apprenez à planifier votre avenir financier efficacement.",
# #                 "is_unlocked": False,
# #                 "quizzes": [
# #                     {"question": "Pourquoi est-il important d’avoir une assurance ?", "answer": "Protection financière"},
# #                     # Ajoute 9 autres questions...
# #                 ]
# #             },
# #         ]

# #         # Crée un utilisateur ou récupère un utilisateur existant (par exemple, un administrateur)
# #         user, created = User.objects.get_or_create(username='admin', defaults={'password': 'adminpassword'})

# #         # Créer les cours et les quiz associés
# #         for course_data in courses_data:
# #             course, created = Course.objects.get_or_create(
# #                 title=course_data["title"],
# #                 description=course_data["description"],
# #                 unlocked=course_data["is_unlocked"],
# #                 order=courses_data.index(course_data) + 1  # Assigner l'ordre des cours
# #             )

# #             # Créer les quiz associés au cours et ajouter un utilisateur
# #             for quiz_data in course_data["quizzes"]:
# #                 quiz_data['user'] = user  # Ajoute un utilisateur par défaut ici
# #                 Quiz.objects.get_or_create(course=course, **quiz_data)

# #         self.stdout.write(self.style.SUCCESS("Cours et quiz ajoutés avec succès !"))
# from django.core.management.base import BaseCommand
# from education.models import Course, Quiz, Choice
# from django.contrib.auth import get_user_model

# User = get_user_model()  # Récupère le modèle utilisateur défini dans AUTH_USER_MODEL

# class Command(BaseCommand):
#     help = "Ajoute des cours et des quiz à la base de données"

#     def handle(self, *args, **kwargs):
#         courses_data = [
#             {
#                 "title": "Introduction à la Gestion Financière",
#                 "description": "Apprenez les bases de la gestion de votre argent.",
#                 "is_unlocked": True,
#                 "quizzes": [
#                     {
#                         "question": "Que signifie le terme 'budget' ?",
#                         "correct_answer": "Plan de dépenses",
#                         "choices": [
#                             "Plan de dépenses", "Évaluation des risques", "Répartition des revenus", "Calcul des profits"
#                         ]
#                     },
#                     # Ajoute d'autres quiz ici...
#                 ]
#             },
#             # Ajoute d'autres cours ici...
#             {
#                 "title": "Épargne et Budget",
#                 "description": "Apprenez à établir un budget et à épargner efficacement.",
#                 "is_unlocked": False,
#                 "quizzes": [
#                     {
#                         "question": "Quelle est la règle des 50/30/20 ?",
#                         "correct_answer": "Budget en 3 catégories",
#                         "choices": [
#                             "Budget en 3 catégories", 
#                             "Répartition égale des dépenses", 
#                             "Maximiser les économies",
#                             "Réduire les impôts"
#                         ]
#                     },
#                     {
#                         "question": "Quelle est l’utilité d’un fonds d’urgence ?",
#                         "correct_answer": "Préparer les imprévus",
#                         "choices": [
#                             "Réduire les dettes", 
#                             "Investir dans des actions", 
#                             "Préparer les imprévus", 
#                             "Améliorer la cote de crédit"
#                         ]
#                     },
#                     {
#                         "question": "Quel pourcentage du revenu devrait idéalement être alloué à l’épargne ?",
#                         "correct_answer": "20%",
#                         "choices": [
#                             "10%", 
#                             "20%", 
#                             "50%", 
#                             "30%"
#                         ]
#                     },
#                 ]
#             },
#             {
#                 "title": "Gestion des Dettes",
#                 "description": "Comprenez comment gérer et réduire vos dettes.",
#                 "is_unlocked": False,
#                 "quizzes": [
#                     {
#                         "question": "Qu'est-ce qu'un crédit à la consommation ?",
#                         "correct_answer": "Prêt pour achats",
#                         "choices": [
#                             "Prêt pour achats", 
#                             "Prêt pour investissements", 
#                             "Prêt immobilier", 
#                             "Prêt automobile"
#                         ]
#                     },
#                     {
#                         "question": "Quel est l'effet d'un taux d'intérêt élevé sur la gestion des dettes ?",
#                         "correct_answer": "Augmenter le coût total de la dette",
#                         "choices": [
#                             "Réduire les paiements mensuels", 
#                             "Augmenter le coût total de la dette", 
#                             "Rendre la dette plus facile à rembourser", 
#                             "Réduire la durée de la dette"
#                         ]
#                     },
#                     {
#                         "question": "Qu'est-ce qu'une consolidation de dettes ?",
#                         "correct_answer": "Regrouper plusieurs dettes en un seul prêt",
#                         "choices": [
#                             "Regrouper plusieurs dettes en un seul prêt", 
#                             "Augmenter le montant des dettes", 
#                             "Refuser de payer les dettes", 
#                             "Emprunter pour rembourser"
#                         ]
#                     },
#                 ]
#             },
#             {
#                 "title": "Investissements",
#                 "description": "Découvrez les bases de l’investissement et du placement d’argent.",
#                 "is_unlocked": False,
#                 "quizzes": [
#                     {
#                         "question": "Qu'est-ce qu'une action ?",
#                         "correct_answer": "Part d'une entreprise",
#                         "choices": [
#                             "Part d'une entreprise", 
#                             "Prêt à la banque", 
#                             "Obligation de remboursement", 
#                             "Produit financier à court terme"
#                         ]
#                     },
#                     {
#                         "question": "Quel est l'objectif principal de l'investissement à long terme ?",
#                         "correct_answer": "Maximiser les gains sur une période prolongée",
#                         "choices": [
#                             "Maximiser les gains sur une période prolongée", 
#                             "Générer un revenu immédiat", 
#                             "Réduire le risque financier", 
#                             "Faire des profits rapidement"
#                         ]
#                     },
#                     {
#                         "question": "Qu'est-ce qu'un portefeuille diversifié ?",
#                         "correct_answer": "Un ensemble d'investissements répartis sur différents types d'actifs",
#                         "choices": [
#                             "Un ensemble d'investissements répartis sur différents types d'actifs", 
#                             "Un investissement dans une seule action", 
#                             "Un investissement dans une seule entreprise", 
#                             "Un portefeuille d'obligations"
#                         ]
#                     },
#                 ]
#             },
#             {
#                 "title": "Planification Financière",
#                 "description": "Apprenez à planifier votre avenir financier efficacement.",
#                 "is_unlocked": False,
#                 "quizzes": [
#                     {
#                         "question": "Pourquoi est-il important d’avoir une assurance ?",
#                         "correct_answer": "Protection financière",
#                         "choices": [
#                             "Réduire les impôts", 
#                             "Protection financière", 
#                             "Investir dans des actions", 
#                             "Éviter les dettes"
#                         ]
#                     },
#                     {
#                         "question": "Qu'est-ce qu'un objectif financier SMART ?",
#                         "correct_answer": "Un objectif spécifique, mesurable, atteignable, réaliste et temporellement défini",
#                         "choices": [
#                             "Un objectif spécifique, mesurable, atteignable, réaliste et temporellement défini", 
#                             "Un objectif vague et flexible", 
#                             "Un objectif lié à l'économie", 
#                             "Un objectif qui n'a pas de délai"
#                         ]
#                     },
#                     {
#                         "question": "Pourquoi est-il important de revoir régulièrement ses objectifs financiers ?",
#                         "correct_answer": "Pour s'assurer qu'ils sont toujours adaptés à la situation actuelle",
#                         "choices": [
#                             "Pour s'assurer qu'ils sont toujours adaptés à la situation actuelle", 
#                             "Pour les ajuster uniquement si les finances se détériorent", 
#                             "Pour les supprimer en cas de difficulté", 
#                             "Pour augmenter les objectifs chaque année"
#                         ]
#                     },
#                 ]
#             }
#         ]

#         # Créer un utilisateur ou récupérer un utilisateur existant (par exemple, un administrateur)
#         user, created = User.objects.get_or_create(username='admin', defaults={'password': 'adminpassword'})

#         # Créer les cours et les quiz associés
#         for index, course_data in enumerate(courses_data, start=1):  # Utiliser l'index pour l'ordre des cours
#             course, created = Course.objects.get_or_create(
#                 title=course_data["title"],
#                 description=course_data["description"],
#                 is_unlocked=course_data["is_unlocked"],
#                 order=index
#             )

#             # Créer les quiz et choix associés
#             for quiz_data in course_data["quizzes"]:
#                 quiz = Quiz.objects.create(
#                     course=course,
#                     question=quiz_data["question"],
#                     correct_answer=quiz_data["correct_answer"]
#                 )

#                 # Créer les choix pour chaque quiz
#                 for choice_text in quiz_data["choices"]:
#                     is_correct = choice_text == quiz_data["correct_answer"]
#                     Choice.objects.create(quiz=quiz, choice_text=choice_text, is_correct=is_correct)

#         self.stdout.write(self.style.SUCCESS("Cours et quiz ajoutés avec succès !"))
# from django.core.management.base import BaseCommand
# from education.models import Course, Quiz
# from django.contrib.auth import get_user_model

# User = get_user_model()  # Récupère le modèle utilisateur défini dans AUTH_USER_MODEL

# class Command(BaseCommand):
#     help = "Ajoute des cours et des quiz à la base de données"

#     def handle(self, *args, **kwargs):
#         courses_data = [
#             {
#                 "title": "Introduction à la Gestion Financière",
#                 "description": "Apprenez les bases de la gestion de votre argent.",
#                 "is_unlocked": True,
#                 "quizzes": [
#                     {"question": "Que signifie le terme 'budget' ?", "answer": "Plan de dépenses"},
#                     {"question": "Pourquoi est-il important d’économiser ?", "answer": "Sécurité financière"},
#                     {"question": "Que représente un revenu ?", "answer": "Argent gagné"},
#                     {"question": "Qu'est-ce qu'une dépense fixe ?", "answer": "Dépense récurrente"},
#                     {"question": "Pourquoi faut-il éviter les dettes excessives ?", "answer": "Risque financier"},
#                     {"question": "Que signifie 'intérêt composé' ?", "answer": "Intérêt sur intérêt"},
#                     {"question": "Qu'est-ce qu'un investissement ?", "answer": "Placement d'argent"},
#                     {"question": "Pourquoi diversifier ses investissements ?", "answer": "Réduction des risques"},
#                     {"question": "Comment définir un objectif financier ?", "answer": "But d'épargne"},
#                     {"question": "Qu'est-ce qu'une épargne d'urgence ?", "answer": "Fonds en cas d'imprévu"},
#                 ]
#             },
#             {
#                 "title": "Épargne et Budget",
#                 "description": "Apprenez à établir un budget et à épargner efficacement.",
#                 "is_unlocked": False,
#                 "quizzes": [
#                     {"question": "Quelle est la règle des 50/30/20 ?", "answer": "Budget en 3 catégories"},
#                     {"question": "Quelle est l’utilité d’un fonds d’urgence ?", "answer": "Préparer les imprévus"},
#                     # Ajoute 8 autres questions...
#                 ]
#             },
#             {
#                 "title": "Gestion des Dettes",
#                 "description": "Comprenez comment gérer et réduire vos dettes.",
#                 "is_unlocked": False,
#                 "quizzes": [
#                     {"question": "Qu'est-ce qu'un crédit à la consommation ?", "answer": "Prêt pour achats"},
#                     # Ajoute 9 autres questions...
#                 ]
#             },
#             {
#                 "title": "Investissements",
#                 "description": "Découvrez les bases de l’investissement et du placement d’argent.",
#                 "is_unlocked": False,
#                 "quizzes": [
#                     {"question": "Qu'est-ce qu'une action ?", "answer": "Part d'une entreprise"},
#                     # Ajoute 9 autres questions...
#                 ]
#             },
#             {
#                 "title": "Planification Financière",
#                 "description": "Apprenez à planifier votre avenir financier efficacement.",
#                 "is_unlocked": False,
#                 "quizzes": [
#                     {"question": "Pourquoi est-il important d’avoir une assurance ?", "answer": "Protection financière"},
#                     # Ajoute 9 autres questions...
#                 ]
#             },
#         ]

#         # Crée un utilisateur ou récupère un utilisateur existant (par exemple, un administrateur)
#         user, created = User.objects.get_or_create(username='admin', defaults={'password': 'adminpassword'})

#         # Créer les cours et les quiz associés
#         for course_data in courses_data:
#             course, created = Course.objects.get_or_create(
#                 title=course_data["title"],
#                 description=course_data["description"],
#                 unlocked=course_data["is_unlocked"],
#                 order=courses_data.index(course_data) + 1  # Assigner l'ordre des cours
#             )

#             # Créer les quiz associés au cours et ajouter un utilisateur
#             for quiz_data in course_data["quizzes"]:
#                 quiz_data['user'] = user  # Ajoute un utilisateur par défaut ici
#                 Quiz.objects.get_or_create(course=course, **quiz_data)

#         self.stdout.write(self.style.SUCCESS("Cours et quiz ajoutés avec succès !"))
from django.core.management.base import BaseCommand
from education.models import Course, Quiz, Choice
from django.contrib.auth import get_user_model
from django.db.models import Max


User = get_user_model()  # Récupère le modèle utilisateur défini dans AUTH_USER_MODEL
class Command(BaseCommand):
    help = "Ajoute des cours et des quiz à la base de données"

    def handle(self, *args, **kwargs):
        courses_data = [
            {
                "title": "Introduction à la Facturation",
                "description": "Découvrez les bases de la facturation et son importance dans la gestion d'une entreprise.",
                "is_unlocked": True,
                "quizzes": [
                    {
                        "question": "Qu'est-ce qu'une facture ?",
                        "correct_answer": "Un document légal qui enregistre une transaction commerciale",
                        "choices": [
                            "Un document légal qui enregistre une transaction commerciale", 
                            "Un reçu de paiement", 
                            "Une preuve de livraison", 
                            "Un contrat d'achat"
                        ]
                    },
                    {
                        "question": "Quels éléments doivent obligatoirement figurer sur une facture ?",
                        "correct_answer": "Nom de l'entreprise, description des biens/services, montant total",
                        "choices": [
                            "Nom de l'entreprise, description des biens/services, montant total", 
                            "Numéro de téléphone de l'entreprise, adresse du client", 
                            "Adresse de l'entreprise, taux de TVA", 
                            "Montant total uniquement"
                        ]
                    }
                ]
            },
            {
                "title": "L'Importance Juridique de la Facturation",
                "description": "Apprenez pourquoi la facturation est un outil essentiel pour les transactions légales.",
                "is_unlocked": False,
                "quizzes": [
                    {
                        "question": "Pourquoi la facturation est-elle importante sur le plan juridique ?",
                        "correct_answer": "Elle sert de preuve en cas de litige",
                        "choices": [
                            "Elle sert de preuve en cas de litige", 
                            "Elle permet de calculer les taxes", 
                            "Elle permet de définir le montant du paiement", 
                            "Elle est utilisée pour les remboursements"
                        ]
                    },
                    {
                        "question": "Quel document peut remplacer une facture dans un contrat commercial ?",
                        "correct_answer": "Un bon de commande",
                        "choices": [
                            "Un bon de commande", 
                            "Un reçu de paiement", 
                            "Un devis", 
                            "Un contrat signé"
                        ]
                    }
                ]
            },
            {
                "title": "Histoire de la Facturation",
                "description": "Comprenez l'évolution de la facturation à travers l'histoire.",
                "is_unlocked": False,
                "quizzes": [
                    {
                        "question": "Quand a été créée la première facture connue ?",
                        "correct_answer": "En 3300 avant J.C.",
                        "choices": [
                            "En 3300 avant J.C.", 
                            "En 1200 après J.C.", 
                            "En 1500 après J.C.", 
                            "Au Moyen Âge"
                        ]
                    },
                    {
                        "question": "Qui a popularisé l'utilisation des factures modernes ?",
                        "correct_answer": "Les commerçants de la Renaissance",
                        "choices": [
                            "Les commerçants de la Renaissance", 
                            "Les marchands de l'Empire romain", 
                            "Les entreprises industrielles du XIXe siècle", 
                            "Les commerçants de l'Égypte antique"
                        ]
                    }
                ]
            },
            {
                "title": "Les Avantages de la Facturation",
                "description": "Découvrez les nombreux avantages de la facturation pour une entreprise.",
                "is_unlocked": False,
                "quizzes": [
                    {
                        "question": "Quel est l'un des principaux avantages de la facturation ?",
                        "correct_answer": "Assurer la traçabilité des transactions",
                        "choices": [
                            "Assurer la traçabilité des transactions", 
                            "Réduire les coûts de production", 
                            "Augmenter les ventes immédiatement", 
                            "Offrir des réductions aux clients"
                        ]
                    },
                    {
                        "question": "La facturation permet-elle d'améliorer la gestion de la trésorerie ?",
                        "correct_answer": "Oui, en suivant les paiements à recevoir",
                        "choices": [
                            "Oui, en suivant les paiements à recevoir", 
                            "Non, elle n'a pas d'impact sur la trésorerie", 
                            "Oui, mais uniquement dans les grandes entreprises", 
                            "Non, elle est uniquement utile pour le calcul des taxes"
                        ]
                    }
                ]
            },
            {
                "title": "Gestion des Paiements et des Créances",
                "description": "Apprenez à gérer les paiements et les créances pour assurer une bonne santé financière de votre entreprise.",
                "is_unlocked": False,
                "quizzes": [
                    {
                        "question": "Qu'est-ce qu'une créance ?",
                        "correct_answer": "Une somme d'argent qu'un client doit à l'entreprise",
                        "choices": [
                            "Une somme d'argent qu'un client doit à l'entreprise", 
                            "Un paiement anticipé", 
                            "Un remboursement effectué par un client", 
                            "Un document prouvant une vente"
                        ]
                    },
                    {
                        "question": "Quel est l'objectif principal de la gestion des créances ?",
                        "correct_answer": "Assurer que les paiements sont reçus à temps",
                        "choices": [
                            "Assurer que les paiements sont reçus à temps", 
                            "Réduire les coûts de production", 
                            "Accélérer le processus de production", 
                            "Offrir des réductions aux clients"
                        ]
                    },
                    {
                        "question": "Quel est l'impact d'une mauvaise gestion des créances ?",
                        "correct_answer": "Un risque de liquidité pour l'entreprise",
                        "choices": [
                            "Un risque de liquidité pour l'entreprise", 
                            "Une augmentation des ventes", 
                            "Un meilleur contrôle des coûts", 
                            "Une réduction des impôts"
                        ]
                    }
                ]
            }
        ]

        # S'assurer que le champ 'order' est unique et ne provoque pas de doublons
        for index, course_data in enumerate(courses_data, start=1):
            # Chercher le dernier order
            last_order = Course.objects.aggregate(Max('order'))['order__max'] or 0
            new_order = last_order + 1 + index  # Incrémente l'order pour éviter des doublons
            course, created = Course.objects.get_or_create(
                title=course_data["title"],
                description=course_data["description"],
                is_unlocked=course_data["is_unlocked"],
                order=new_order
            )

            # Créer les quiz et choix associés
            for quiz_data in course_data["quizzes"]:
                quiz = Quiz.objects.create(
                    course=course,
                    question=quiz_data["question"],
                    correct_answer=quiz_data["correct_answer"]
                )

                # Créer les choix pour chaque quiz
                for choice_text in quiz_data["choices"]:
                    is_correct = choice_text == quiz_data["correct_answer"]
                    Choice.objects.create(quiz=quiz, choice_text=choice_text, is_correct=is_correct)

        self.stdout.write(self.style.SUCCESS("Cours et quiz sur la facturation et la gestion des paiements ajoutés avec succès !"))




# ###############################FINANCE TRACKER
# class Command(BaseCommand):
#     help = "Ajoute des cours et des quiz à la base de données"

#     def handle(self, *args, **kwargs):
#         courses_data = [
#             {
#                 "title": "Introduction à la Gestion Financière",
#                 "description": "Apprenez les bases de la gestion de votre argent.",
#                 "is_unlocked": True,
#                 "quizzes": [
#                     {
#                         "question": "Que signifie le terme 'budget' ?",
#                         "correct_answer": "Plan de dépenses",
#                         "choices": [
#                             "Plan de dépenses", "Évaluation des risques", "Répartition des revenus", "Calcul des profits"
#                         ]
#                     },
#                     # Ajoute d'autres quiz ici...
#                 ]
#             },
#             # Ajoute d'autres cours ici...
#             {
#                 "title": "Épargne et Budget",
#                 "description": "Apprenez à établir un budget et à épargner efficacement.",
#                 "is_unlocked": False,
#                 "quizzes": [
#                     {
#                         "question": "Quelle est la règle des 50/30/20 ?",
#                         "correct_answer": "Budget en 3 catégories",
#                         "choices": [
#                             "Budget en 3 catégories", 
#                             "Répartition égale des dépenses", 
#                             "Maximiser les économies",
#                             "Réduire les impôts"
#                         ]
#                     },
#                     {
#                         "question": "Quelle est l’utilité d’un fonds d’urgence ?",
#                         "correct_answer": "Préparer les imprévus",
#                         "choices": [
#                             "Réduire les dettes", 
#                             "Investir dans des actions", 
#                             "Préparer les imprévus", 
#                             "Améliorer la cote de crédit"
#                         ]
#                     },
#                     {
#                         "question": "Quel pourcentage du revenu devrait idéalement être alloué à l’épargne ?",
#                         "correct_answer": "20%",
#                         "choices": [
#                             "10%", 
#                             "20%", 
#                             "50%", 
#                             "30%"
#                         ]
#                     },
#                 ]
#             },
#             {
#                 "title": "Gestion des Dettes",
#                 "description": "Comprenez comment gérer et réduire vos dettes.",
#                 "is_unlocked": False,
#                 "quizzes": [
#                     {
#                         "question": "Qu'est-ce qu'un crédit à la consommation ?",
#                         "correct_answer": "Prêt pour achats",
#                         "choices": [
#                             "Prêt pour achats", 
#                             "Prêt pour investissements", 
#                             "Prêt immobilier", 
#                             "Prêt automobile"
#                         ]
#                     },
#                     {
#                         "question": "Quel est l'effet d'un taux d'intérêt élevé sur la gestion des dettes ?",
#                         "correct_answer": "Augmenter le coût total de la dette",
#                         "choices": [
#                             "Réduire les paiements mensuels", 
#                             "Augmenter le coût total de la dette", 
#                             "Rendre la dette plus facile à rembourser", 
#                             "Réduire la durée de la dette"
#                         ]
#                     },
#                     {
#                         "question": "Qu'est-ce qu'une consolidation de dettes ?",
#                         "correct_answer": "Regrouper plusieurs dettes en un seul prêt",
#                         "choices": [
#                             "Regrouper plusieurs dettes en un seul prêt", 
#                             "Augmenter le montant des dettes", 
#                             "Refuser de payer les dettes", 
#                             "Emprunter pour rembourser"
#                         ]
#                     },
#                 ]
#             },
#             {
#                 "title": "Investissements",
#                 "description": "Découvrez les bases de l’investissement et du placement d’argent.",
#                 "is_unlocked": False,
#                 "quizzes": [
#                     {
#                         "question": "Qu'est-ce qu'une action ?",
#                         "correct_answer": "Part d'une entreprise",
#                         "choices": [
#                             "Part d'une entreprise", 
#                             "Prêt à la banque", 
#                             "Obligation de remboursement", 
#                             "Produit financier à court terme"
#                         ]
#                     },
#                     {
#                         "question": "Quel est l'objectif principal de l'investissement à long terme ?",
#                         "correct_answer": "Maximiser les gains sur une période prolongée",
#                         "choices": [
#                             "Maximiser les gains sur une période prolongée", 
#                             "Générer un revenu immédiat", 
#                             "Réduire le risque financier", 
#                             "Faire des profits rapidement"
#                         ]
#                     },
#                     {
#                         "question": "Qu'est-ce qu'un portefeuille diversifié ?",
#                         "correct_answer": "Un ensemble d'investissements répartis sur différents types d'actifs",
#                         "choices": [
#                             "Un ensemble d'investissements répartis sur différents types d'actifs", 
#                             "Un investissement dans une seule action", 
#                             "Un investissement dans une seule entreprise", 
#                             "Un portefeuille d'obligations"
#                         ]
#                     },
#                 ]
#             },
#             {
#                 "title": "Planification Financière",
#                 "description": "Apprenez à planifier votre avenir financier efficacement.",
#                 "is_unlocked": False,
#                 "quizzes": [
#                     {
#                         "question": "Pourquoi est-il important d’avoir une assurance ?",
#                         "correct_answer": "Protection financière",
#                         "choices": [
#                             "Réduire les impôts", 
#                             "Protection financière", 
#                             "Investir dans des actions", 
#                             "Éviter les dettes"
#                         ]
#                     },
#                     {
#                         "question": "Qu'est-ce qu'un objectif financier SMART ?",
#                         "correct_answer": "Un objectif spécifique, mesurable, atteignable, réaliste et temporellement défini",
#                         "choices": [
#                             "Un objectif spécifique, mesurable, atteignable, réaliste et temporellement défini", 
#                             "Un objectif vague et flexible", 
#                             "Un objectif lié à l'économie", 
#                             "Un objectif qui n'a pas de délai"
#                         ]
#                     },
#                     {
#                         "question": "Pourquoi est-il important de revoir régulièrement ses objectifs financiers ?",
#                         "correct_answer": "Pour s'assurer qu'ils sont toujours adaptés à la situation actuelle",
#                         "choices": [
#                             "Pour s'assurer qu'ils sont toujours adaptés à la situation actuelle", 
#                             "Pour les ajuster uniquement si les finances se détériorent", 
#                             "Pour les supprimer en cas de difficulté", 
#                             "Pour augmenter les objectifs chaque année"
#                         ]
#                     },
#                 ]
#             }
#         ]

#         # Créer un utilisateur ou récupérer un utilisateur existant (par exemple, un administrateur)
#         user, created = User.objects.get_or_create(username='admin', defaults={'password': 'adminpassword'})

#         # Créer les cours et les quiz associés
#         for index, course_data in enumerate(courses_data, start=1):  # Utiliser l'index pour l'ordre des cours
#             course, created = Course.objects.get_or_create(
#                 title=course_data["title"],
#                 description=course_data["description"],
#                 is_unlocked=course_data["is_unlocked"],
#                 order=index
#             )

#             # Créer les quiz et choix associés
#             for quiz_data in course_data["quizzes"]:
#                 quiz = Quiz.objects.create(
#                     course=course,
#                     question=quiz_data["question"],
#                     correct_answer=quiz_data["correct_answer"]
#                 )

#                 # Créer les choix pour chaque quiz
#                 for choice_text in quiz_data["choices"]:
#                     is_correct = choice_text == quiz_data["correct_answer"]
#                     Choice.objects.create(quiz=quiz, choice_text=choice_text, is_correct=is_correct)

#         self.stdout.write(self.style.SUCCESS("Cours et quiz ajoutés avec succès !"))
