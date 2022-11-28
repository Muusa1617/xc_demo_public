# -*- coding: utf-8 -*-

import os
import warnings
from datetime import timedelta

warnings.filterwarnings('ignore')


class Config(object):
    ENV = 'development'
    DEBUG = False
    TESTING = False
    HOST = '0.0.0.0'
    PORT = 8000
    BASE_PATH = os.path.abspath(os.path.dirname(__file__))

    # session
    SECRET_KEY = ''
    PERMANENT_SESSION_LIFETIME = timedelta(hours=1)

    # file upload
    MAX_CONTENT_LENGTH = 8 * 1024 * 1024  # 8M

    # database: mysql / postgresql
    DB_POOL_SIZE = 1
    DB_CONF = dict(
        source='mysql',
        host='',
        port='',
        user='',
        password='',
        database='demo1',
        charset='utf8'
    )

    # redis
    REDIS_URL = 'redis://127.0.0.1:6379/0'

    # cache
    CACHE_CONF = [
        '127.0.0.1:11211'
    ]

    # oss
    OSS_CONF = dict(
        endpoint='',
        bucket='',
        access_key_id='',
        access_key_secret=''
    )

    # cos
    COS_CONF = dict(
        secret_id = '',     # 替换为用户的 SecretId，请登录访问管理控制台进行查看和管理，https://console.cloud.tencent.com/cam/capi
        secret_key = '',   # 替换为用户的 SecretKey，请登录访问管理控制台进行查看和管理，https://console.cloud.tencent.com/cam/capi
        region = '',      # 替换为用户的 region，已创建桶归属的region可以在控制台查看，https://console.cloud.tencent.com/cos5/bucket
        # COS支持的所有region列表参见https://cloud.tencent.com/document/product/436/6224
        token = '',               # 如果使用永久密钥不需要填入token，如果使用临时密钥需要填入，临时密钥生成和使用指引参见https://cloud.tencent.com/document/product/436/14048
        scheme = 'https',
        bucket = ''
    )


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    ENV = 'production'
    pass


class TestingConfig(Config):
    ENV = 'testing'
    pass


config = dict(
    development=DevelopmentConfig,
    production=ProductionConfig,
    testing=TestingConfig
)
