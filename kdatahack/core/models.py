from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType


class SelfAwareModelMixin(object):
    def contenttype(self):
        return ContentType.objects.get_for_model(self)

    def contenttype_id(self):
        return self.contenttype().pk

    def app_label(self):
        return self.contenttype().app_label

    def model_name(self):
        return self.contenttype().model
