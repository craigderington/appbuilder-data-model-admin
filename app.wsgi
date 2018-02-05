#!/usr/bin/python
import sys
import logging

activate_this = '/home/craigderington/sites/MyAppBuilder/.env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/craigderington/sites/MyAppBuilder/earl-data-model/app/')

from app import app as application