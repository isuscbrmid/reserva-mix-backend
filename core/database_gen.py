import os
import os
from .json_reader import json_settings

settings = json_settings()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def database_config(ENV):
    return {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "HOST": settings["DB"][ENV]["HOST"],
            "NAME": settings["DB"][ENV]["NAME"],
            "USER": settings["DB"][ENV]["USER"],
            "PASSWORD": settings["DB"][ENV]["PASSWORD"],
        }
    }
