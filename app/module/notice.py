from app.models.notice import Notice
from app.module.base import BaseController


class NoticeController(BaseController):


    def describe(self):
        model = Notice.find().where(id=1).one()
        print('下面是msg')
        print(model)
        print(model.msg)
        return self.ok(str(model.msg))
        # return model.msg

    def modify(self):
        msg = self.post('msg')
        model = Notice.find().where(id=1).one()
        if not model:
            return self.error('改用不存在')
        model.msg = msg
        model.save()
        return self.ok('修改成功')

