from operation.base_op import BaseOP
from py_page.orderList_page import OrderListApi

class Order(BaseOP):

	def __init__(self):
		self.token = self.get_token()

	# 获取订单列表所有的订单id
	def get_orderIdList(self):
		id_list = list()
		res = OrderListApi(token=self.token).orderList_api()
		data_list = res['content']['data']['list']
		for order in data_list:
			id_list.append(order['id'])
		return id_list


