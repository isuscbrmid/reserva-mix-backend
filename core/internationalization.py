from .json_reader import json_settings

settings = json_settings()

LANGUAGE_CODE = "es"

TIME_ZONE = settings["TIME_ZONE"]

USE_I18N = True

USE_L10N = True

USE_TZ = True
