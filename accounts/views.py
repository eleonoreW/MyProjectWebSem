from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import PermissionDenied
from django.http import request
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserForm, UserProfileForm
from django.forms.models import inlineformset_factory
import logging

logger = logging.getLogger(__name__)


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

@login_required()  # only logged in users should access this
def profile(pk, request):
    # querying the User object with pk from url
    user = User.objects.get(pk=pk)
    logger.error(pk)

    # prepopulate UserProfileForm with retrieved user values from above.
    a = UserProfile.objects.get(pk=1)
    form = UserProfileForm(request.POST, instance=a)
    form.save()
    return render(request, 'accounts/profile.html')

