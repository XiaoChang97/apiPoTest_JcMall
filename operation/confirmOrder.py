from operation.base_op import BaseOP
from py_page.confirmOrder_page import ConfirmOrderPageApi



class ConfirmOrder(BaseOP):

	def __init__(self):
		self.token = self.get_token()

	# 增加收获地址
	def add_address(self,name,phone,address):
		res = ConfirmOrderPageApi(token=self.token).addAddress_api(name,phone,address)
		return res

	# 支付生成订单
	def pay_confirmOrder(self,goodsId,pay_way=3):
		# 提交订单
		res_1 = ConfirmOrderPageApi(token=self.token).confirmOrder_buy_api(goodsId)
		order_id = res_1['content']['data']['order_id']
		# 选择支付方式进行支付
		ConfirmOrderPageApi(token=self.token).payment_pcPrepay_api(order_id=order_id,pay_way=pay_way)
		# 支付完成返回订单详情
		res_2 = ConfirmOrderPageApi(token=self.token).confirmOrder_detail_api(id=order_id)
		return res_2



