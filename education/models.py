from django.db import models

# Create your models here.

from django.contrib.auth import get_user_model

from django.db import models

# Create your models here.
# education/models.py
from django.db import models
# from django.contrib.auth import get_user_model
from authentication.models import User

User = get_user_model()  # Récupère le modèle utilisateur défini dans authentication





from django.db import models
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    order = models.IntegerField(unique=True)  # Pour organiser les cours
    is_unlocked = models.BooleanField(default=False)  # Ajoute ce champ

# class Course(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     is_unlocked = models.BooleanField(default=False)
#     order = models.IntegerField(unique=True)

class Quiz(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=255)

class Choice(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

# class Course(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     is_unlocked = models.BooleanField(default=False)
#     order = models.IntegerField()

#     def __str__(self):
#         return self.title

# class Quiz(models.Model):
#     course = models.ForeignKey(Course, related_name="quizzes", on_delete=models.CASCADE)
#     question = models.TextField()
#     correct_answer = models.CharField(max_length=200)  # Vérifie bien cette ligne

#     def __str__(self):
#         return self.question


# class Choice(models.Model):
#     quiz = models.ForeignKey(Quiz, related_name="choices", on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     is_correct = models.BooleanField(default=False)

#     def __str__(self):
#         return self.choice_text




# from django.db import models

# class Course(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     is_unlocked = models.BooleanField(default=False)
#     order = models.IntegerField()

#     def __str__(self):
#         return self.title

# class Quiz(models.Model):
#     course = models.ForeignKey(Course, related_name="quizzes", on_delete=models.CASCADE)
#     question = models.TextField()
#     correct_answer = models.CharField(max_length=200)

#     def __str__(self):
#         return self.question

# class Choice(models.Model):
#     quiz = models.ForeignKey(Quiz, related_name="choices", on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     is_correct = models.BooleanField(default=False)

#     def __str__(self):
#         return self.choice_text






















# from django.db import models
# from django.contrib.auth import get_user_model

# User = get_user_model()

# class Course(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     order = models.IntegerField(unique=True)  
#     is_unlocked = models.BooleanField(default=False)

#     def __str__(self):
#         return self.title

# class UserCourse(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)  # L'utilisateur suit un cours
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     progress = models.FloatField(default=0.0)  # Indique l'avancement en pourcentage

#     class Meta:
#         unique_together = ('user', 'course')  # Un utilisateur ne peut être inscrit qu'une seule fois à un cours

#     def __str__(self):
#         return f"{self.user.username} - {self.course.title}"
