from app.module.base import BaseController
import snowflake.client

class OrderController(BaseController):

    def new_order_id(self):
        return self.ok(snowflake.client.get_guid())