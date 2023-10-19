#!/bin/bash
if test -f "/app/manage.py"; then
   # python manage.py migrate      # Apply database migrations
   if [ "$APP_ENV" == "local" ]        # Collect static files on in DEV
   then
      python manage.py runserver 0.0.0.0:8000
   else
      # production
      python manage.py collectstatic --noinput
      # Launch supervisor
      /usr/local/bin/supervisord -n
   fi
fi
