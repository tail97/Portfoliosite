from pathlib import Path
SECRET_KEY = 'django-insecure-$#y_u&25*_o#k6y4lw**1j#&v^37atr%9xn!@g!ke9&h)x+x3j'
DEBUG = True
ALLOWED_HOSTS = []

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}