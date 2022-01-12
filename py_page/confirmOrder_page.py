from py_page.base_api import BaseApi


class ConfirmOrderPageApi(BaseApi):

	def __init__(self,path="./yaml_api/confirmOrder_page.yaml",token=None):
		self.path = path
		self.token = token

	def addAddress_api(self,name,phone,address):
		addAddress = self.run_requests(self.path,'addAddress', token=self.token,name=name,phone=phone,address=address)
		return addAddress

	def confirmOrder_buy_api(self,goodsId):
		confirmOrder_buy = self.run_requests(self.path, 'confirmOrder_buy', token=self.token, goodsId=goodsId)
		return confirmOrder_buy

	def confirmOrder_detail_api(self,id):
		confirmOrder_detail = self.run_requests(self.path, 'cofirmOrder_detail', token=self.token, id=id)
		return confirmOrder_detail

	def payment_pcPrepay_api(self,order_id,pay_way=3):
		payment_pcPrepay = self.run_requests(self.path, 'payment_pcPrepay', token=self.token, order_id=order_id,pay_way=pay_way)
		return payment_pcPrepay





if __name__ == '__main__':
	addAddress = ConfirmOrderPageApi().addAddress_api('e478da1a76b45472142c2b1eb9600640')
	print(addAddress)
