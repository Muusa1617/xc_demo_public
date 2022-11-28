from app.module.base import BaseController
from app.models.gift import Gift
from app.models.user import User

class GiftController(BaseController):
    def new_code(self):
        gift_code = self.post('gift_code')
        model = Gift()
        model.gift_code = gift_code
        model.save()
        return self.ok('添加成功')

    def get_gift(self):
        gift_code = self.post('gift_code')
        username = self.post('username')
        password = self.post('password')
        user = User.find().where(username=username).one()
        if not user:
            return self.error('用户不存在')
        if user.password != password:
            return self.error('密码错误')
        gift = Gift.find().where(gift_code=gift_code).one()
        if not gift:
            return self.error('礼包码不存在')
        return self.ok('兑换成功')

