import dj_database_url
import  os
from pathlib import Path 

BASE_DIR = Path(__file__).resolve().parent.parent 

SECRET_KEY = 'django-insecure-dtt%+92*ujq)@4whorng%#96pb4c_=k^3=v$#v6$dxr$2gn3ex' 

DEBUG = True

ALLOWED_HOSTS = ['www.pythra111.pythonanywhere.com', 'pythra111.pythonanywhere.com', 'localhost', 'www.capitalfinesse.com']

INSTALLED_APPS = [
    'cap',  
    'payment',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'capital.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'capital.wsgi.application'
DATABASES = {
    'default': dj_database_url.config(
        default="sqlite:///" + os.path.join(BASE_DIR, "db.sqlite3")
    )
}
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
LANGUAGE_CODE = 'en-us' 
TIME_ZONE = 'UTC' 
USE_I18N = True 
USE_TZ = True 
LOGIN_REDIRECT_URL = 'home'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 
STATIC_URL = 'static/' 
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STRIPE_PUBLIC_KEY = 'pk_test_51QRHPHIcFAr0rHYRlj8ol6zftlxLI4XSEJ3WOerlg4fWRfWMyHomUXbJFy5F1hXdkB2dwPqn0OKIjZvZY3TXCFMc00EfF1bAEl' 
STRIPE_SECRET_KEY ='sk_test_51QRHPHIcFAr0rHYROhb9ySxgp6cjXgwykGLz7qprfg6OmzAezveimqoDRcAOw44Ek99Oz6f7IG5KiIFeKTBA1qUB00gfxbcj5Z'