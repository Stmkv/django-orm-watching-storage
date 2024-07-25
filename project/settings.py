import os
from dotenv import load_dotenv
from environs import Env

env = Env()
env.read_env()

load_dotenv()

DATABASE_ENGINE = env("DATABASE_ENGINE")
DATABASE_HOST = env("DATABASE_HOST")
DATABASE_PORT = env("DATABASE_PORT")
DATABASE_NAME = env("DATABASE_NAME")
DATABASE_USER = env("DATABASE_USER")
DATABASE_PASSWORD = env("DATABASE_PASSWORD")
SECRET_KEY = env("SECRET_KEY")
ROOT_URLCONF = env("ROOT_URLCONF")
DEBUG = env.bool("DEBUG", False)

DATABASES = {
    "default": {
        "ENGINE": DATABASE_ENGINE,
        "HOST": DATABASE_HOST,
        "PORT": DATABASE_PORT,
        "NAME": DATABASE_NAME,
        "USER": DATABASE_USER,
        "PASSWORD": DATABASE_PASSWORD,
    }
}

INSTALLED_APPS = ["datacenter"]

ALLOWED_HOSTS = ["*"]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
    },
]

USE_L10N = True
LANGUAGE_CODE = "ru-ru"
TIME_ZONE = "Europe/Moscow"
USE_TZ = True
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
