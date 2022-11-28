from app.module.base import BaseController
from app.models.user import User


class UserController(BaseController):

    def add(self):
        username = self.post('username')
        phone = self.post('phone')
        money = self.post('money')
        gender = self.post('gender')

        model = User()
        model.username = username
        model.phone = phone
        model.money = money
        model.gender = gender
        model.save()

        return self.ok('添加成功')

    def edit(self):
        id = self.post('id')
        username = self.post('username')
        phone = self.post('phone')
        money = self.post('money')
        gender = self.post('gender')

        model = User.find().where(id=id).one()
        if not model:
            return self.error('改用不存在')
        model.username = username
        model.phone = phone
        model.money = money
        model.gender = gender
        model.save()

        return self.ok('修改成功')

    def delete(self):
        id = self.post('id')
        User.find().where(id=id).delete()
        return self.ok('删除成功')

    def list(self):
        self.init_page()
        model = User.find()
        total = model.count()
        all = model.offset(self.offset).limit(self.limit).all(raw=True)
        return self.resp_page(all, total)

