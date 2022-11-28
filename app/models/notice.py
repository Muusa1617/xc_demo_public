from pymyorm.model import Model
from flask import request, current_app as app
from werkzeug.security import generate_password_hash, check_password_hash
import time
import hashlib

class Notice(Model):
    tablename = 'notice'
    pass
