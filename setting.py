##First Add the app name in setting.py in myproject###

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'quitzapp',


]
## Then create the Templates and Static files path in setting.py
import os
import path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
###___________________________________________________________________####
BASE_DIR2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR2,'templates')
###__________________________________________________________________###
STATIC_DIR = os.path.join(BASE_DIR2,'static')


