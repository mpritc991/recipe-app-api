# This
# "#!" is called a she'bang. used to mark the file as a "shell script file"
#!/bin/sh

# 'set -e' makes it so if any part of the start up script fails, it all fails
set -e

python manage.py wait_for_db
pythong manage.py collectstatic --noinput
python manage.py migrate

#uWSGI running in on a TCP socket, port 9000, from our ngenx server.
# set on 4 different wsgi workers (can be changed depending on cpu count in your server)
# "master" sets this as the main thing running in your wsgi server
# enable threads allows "multi-threading" in our application, allowing use thru wsgi service
# --module means its going to (specified in d-c.yaml) /app/app/wsgi and running it as a module
uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi