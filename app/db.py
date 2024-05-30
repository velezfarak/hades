from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

SQLLITE3 = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

POSTGRES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbshades',
        'HOST': 'localhost',
        'USER': 'postgres',
        'PASSWORD': '123456789',
        'PORT': 5433,
    }
}