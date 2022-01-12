from py_page.base_api import BaseApi
from py_page.home_page import HomePageApi


class OrderListApi(BaseApi):

	def __init__(self,path="./yaml_api/orderList_page.yaml",token=None):
		self.path = path
		self.token = token

	def orderList_api(self):
		orderList = self.run_requests(self.path,'order_list', token=self.token)
		return orderList






if __name__ == '__main__':
	pass
