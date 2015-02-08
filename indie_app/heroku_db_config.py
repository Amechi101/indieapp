import os

############## Heroku Settings ########################
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2", # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        "NAME": "", 

    }
}


# Parse database configuration from $DATABASE_URL
if not os.environ.has_key('DATABASE_URL'):
    os.environ['DATABASE_URL'] = 'postgres://fpyfzfpjxajdbh:XinpGlrb5jifObW6zdz70WS6o2@ec2-23-21-235-249.compute-1.amazonaws.com:5432/da0jlh34a082ck'

import dj_database_url
DATABASES['default'] =  dj_database_url.config()


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']