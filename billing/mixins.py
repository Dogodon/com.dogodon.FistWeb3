from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class LoginRequiredSuperuserMixin(LoginRequiredMixin, UserPassesTestMixin):
    """ Restreint l'accès aux superutilisateurs uniquement. """
    
    def test_func(self):
        return self.request.user.is_superuser
