from django.shortcuts import render

# Create your views here.




from django.shortcuts import render

# Create your views here.
# education/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Course, Quiz


# @login_required
def courses(request):
    courses = Course.objects.all().order_by("order")

    # Déverrouiller uniquement le premier cours s'il ne l'est pas déjà
    first_course = courses.first()
    if first_course and not first_course.is_unlocked:
        first_course.is_unlocked = True
        first_course.save()

    return render(request, 'courses.html', {'courses': courses})




# @login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    quizzes = Quiz.objects.filter(course=course)
    course.is_unlocked = False  # Assurer que ce cours est marqué comme terminé

    previous_course = Course.objects.filter(order__lt=course.order).last()
    next_course = Course.objects.filter(order__gt=course.order).first()

    passed = False  # Par défaut, l'utilisateur n'a pas encore réussi

    if request.method == "POST":
        score = 0
        total_quizzes = len(quizzes)

        for quiz in quizzes:
            user_answer = request.POST.get(f"answers_{quiz.id}")
            correct_answer = quiz.correct_answer

            if user_answer == correct_answer:
                score += 1

        passed = score >= (total_quizzes // 2)  # L'utilisateur doit avoir au moins 50% de bonnes réponses

        if passed:
            course.is_unlocked = True  # Assurer que ce cours est marqué comme terminé
            course.save()

            if next_course and not next_course.is_unlocked:
                next_course.is_unlocked = True  # Déverrouiller le prochain cours
                next_course.save()

        return render(request, "formation/course_detail.html", {
            "course": course,
            "quizzes": quizzes,
            "score": score,
            "total_quizzes": total_quizzes,
            "passed": passed,
            "submitted": True,
            "previous_course": previous_course,
            "next_course": next_course
        })

    return render(request, "formation/course_detail.html", {
        "course": course,
        "quizzes": quizzes,
        "previous_course": previous_course,
        "next_course": next_course
    })


# @login_required
# def course_detail(request, course_id):
#     # Récupère le cours et les quiz associés
#     course = get_object_or_404(Course, id=course_id)
#     quizzes = Quiz.objects.filter(course=course)

#     # Récupérer les cours précédents et suivants pour la navigation
#     previous_course = Course.objects.filter(order__lt=course.order).last()
#     next_course = Course.objects.filter(order__gt=course.order).first()

#     # Si l'utilisateur accède au premier cours, le déverrouiller immédiatement
#     if course.order == 1 and not course.is_unlocked:
#         course.is_unlocked = True
#         course.save()

#     if request.method == "POST":
#         # Récupérer les réponses soumises dans le formulaire
#         user_answers = request.POST.getlist("answers")  # Liste de réponses soumises
#         correct_answers = [quiz.answer for quiz in quizzes]  # Liste des bonnes réponses

#         # Calcul du score
#         score = sum(1 for i in range(len(quizzes)) if user_answers[i] == correct_answers[i])

#         # Si l'utilisateur réussit, débloquer le cours suivant
#         if score >= 7:
#             course.is_unlocked = True
#             course.save()

#             return render(request, "formation/course_detail.html", {
#                 "course": course, "quizzes": quizzes, "passed": True, "submitted": True, 
#                 "previous_course": previous_course, "next_course": next_course
#             })
#         else:
#             return render(request, "formation/course_detail.html", {
#                 "course": course, "quizzes": quizzes, "passed": False, "submitted": True,
#                 "previous_course": previous_course, "next_course": next_course
#             })

#     return render(request, "formation/course_detail.html", {
#         "course": course, "quizzes": quizzes, "previous_course": previous_course, "next_course": next_course
#     })

