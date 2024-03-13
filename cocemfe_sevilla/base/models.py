from django.db import models
from enum import Enum

# Create your models here.
class NotificationType(Enum):
    REVIEWER = "reviewer"
    STATUS = "status"
    NEW_SUGGESTION = "new_suggestion"
    WELCOME = "welcome"
