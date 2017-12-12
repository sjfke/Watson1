# config.py

# But in DEBUG mode flask binds only to 127.0.0.1
# Ignore the app.run(host='0.0.0.0' port=8080) option doesn't work in DEBUG mode.
# $ export FLASK_APP=run.py; flask run --host='0.0.0.0' # to over-ride
#
# Enable Flask's debugging features. Should be False in production
DEBUG = True
