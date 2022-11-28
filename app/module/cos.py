# -*- coding: utf-8 -*-

from app.models.user import User
from app.module.base import BaseController
from app.helper.cos import Cos


class CosController(BaseController):

    def upload(self):
        data = self.post('data')
        username = self.post('username')
        password = self.post('password')
        user = User.find().where(username=username).one()
        if not user:
            return self.error('用户不存在')
        if user.password != password:
            return self.error('密码错误')
        model = Cos()
        rsp = model.upload(username,data)
        return self.ok(rsp)

    def download(self):
        file_name = self.post('file_name')
        model = Cos()
        rsp = model.download(file_name)
        return self.ok(str(rsp))