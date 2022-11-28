from app.module.base import BaseController


class HelloController(BaseController):

    def world(self):
        return 'hello world'