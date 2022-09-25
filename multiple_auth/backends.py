from django.db.models import Q
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.conf import settings

UserModel = get_user_model()


class MultipleAuthentication(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        if username is None or password is None:
            return

        try:
            multiple_auth_settings = settings.MULTIPLE_AUTH
        except AttributeError:
            return None

        multiple_auth_fields = multiple_auth_settings['auth_fields']

        q_object = None
        first_iteration = True
        for field in multiple_auth_fields:
            field_ = {f'{field}__iexact': username}

            if first_iteration:
                q_object = Q(**field_)
                first_iteration = False
            else:
                q_object |= Q(**field_)

        try:
            user = UserModel._default_manager.get(q_object)
        except UserModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
