from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import PermissionDenied
from django.http import request
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserForm
from django.forms.models import inlineformset_factory
import logging

logger = logging.getLogger(__name__)


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


def profile(request):
    return render(request, 'accounts/login.html')


@login_required()  # only logged in users should access this
def edit_user(pk, request):
    # querying the User object with pk from url
    user = User.objects.get(pk=pk)
    logger.error(pk)

    # prepopulate UserProfileForm with retrieved user values from above.
    user_form = UserForm(instance=user)
    # The sorcery begins from here, see explanation below
    ProfileInlineFormset = inlineformset_factory(User, UserProfile,
                                                 fields=('gender', 'height', 'weight', 'city'))
    formset = ProfileInlineFormset(instance=user)
    if user.is_authenticated and request.user.id == user.id:
        if request.method == "POST":
            user_form = UserForm(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)
            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)
                if formset.is_valid():
                    created_user.save()
                    formset.save()
                    return HttpResponseRedirect('/accounts/profile/')
        return render(request, "accounts/editProfile.html", {
            "noodle": pk,
            "noodle_form": user_form,
            "formset": formset,
        })
    else:
        raise PermissionDenied
