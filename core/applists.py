__DJANGO_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
)

__OWN_APPS = (
    "apps.bookings",
)

__THIRD_PARTY_APPS = (
    "rest_framework",
    'rest_framework_simplejwt',
)

INSTALLED_APPS = __DJANGO_APPS + __OWN_APPS + __THIRD_PARTY_APPS
