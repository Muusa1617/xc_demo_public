from pymyorm.model import Model
from flask import request, current_app as app
from werkzeug.security import generate_password_hash, check_password_hash
import time
import hashlib


class Order(Model):
    # 此处埋点，暂时没有和订单相关的操作
    tablename = ''