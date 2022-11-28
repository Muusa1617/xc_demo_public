# -*- coding=utf-8
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import os
from config import config as config_1

class Cos(object):

    def __init__(self) -> None:
        config_name = os.environ.get('FLASK_CONFIG', 'development')
        conf = config_1[config_name]
        self.conf = conf
        self.secret_id = conf.COS_CONF['secret_id']     # 替换为用户的 SecretId，请登录访问管理控制台进行查看和管理，https://console.cloud.tencent.com/cam/capi
        self.secret_key = conf.COS_CONF['secret_key']   # 替换为用户的 SecretKey，请登录访问管理控制台进行查看和管理，https://console.cloud.tencent.com/cam/capi
        self.region = conf.COS_CONF['region']      # 替换为用户的 region，已创建桶归属的region可以在控制台查看，https://console.cloud.tencent.com/cos5/bucket
        # COS支持的所有region列表参见https://cloud.tencent.com/document/product/436/6224
        self.token = conf.COS_CONF['token']               # 如果使用永久密钥不需要填入token，如果使用临时密钥需要填入，临时密钥生成和使用指引参见https://cloud.tencent.com/document/product/436/14048
        self.scheme = conf.COS_CONF['scheme']   
        self.bucket = conf.COS_CONF['bucket']
        config = CosConfig(Region=self.region, SecretId=self.secret_id, SecretKey=self.secret_key, Token=self.token, Scheme=self.scheme)
        self.client = CosS3Client(config)

    def upload(self,file_name,data):
        response = self.client.put_object(
        Bucket=self.bucket,
        Body=data,
        Key=file_name
        )
        print('-------')
        print(response['ETag'])
        return response

    def download(self,file_name):
        response = self.client.get_object(
            Bucket=self.bucket,
            Key=file_name,)       
        response['Body'].get_stream_to_file(file_name)
        print('-----')
        print(response['Body'])
        return response


