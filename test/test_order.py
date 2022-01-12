import pytest
import allure

from operation.shopCar import ShopCar
from operation.confirmOrder import ConfirmOrder
from operation.order import Order
from log import Logger

logging = Logger(__name__)
@allure.feature("测试订单")
class TestOrder:

	logging.logger.info("############开始测试订单逻辑############")

	@allure.story("购买商品生成一条订单")
	def test_payOrder_01(self,goodsId=4):
		logging.logger.info(f"************开始执行测试用例::test_payOrder_01::购买商品{goodsId}生成订单************")
		with allure.step("购买商品获取订单id"):
			order_detail = ConfirmOrder().pay_confirmOrder(goodsId)
			order_id = order_detail['content']['data']['id']
		with allure.step("获取订单列表订单id"):
			idList = Order().get_orderIdList()

		pytest.assume(order_id in idList)



