from py_page.base_api import BaseApi


class GoodsDetailPageApi(BaseApi):

	def __init__(self,path="./yaml_api/goodsDetail_page.yaml",token=None):
		self.path = path
		self.token = token

	def goodsDetail_orderBuy_api(self,goodsId):
		goodsDetail_orderBuy = self.run_requests(self.path,'goodsDetail_orderBuy',token=self.token,goodsId=goodsId)
		return goodsDetail_orderBuy

	def goodsDetail_cartAdd_api(self,goodsId):
		goodsDetail_cartAdd = self.run_requests(self.path,'goodsDetail_cartAdd', token=self.token,goodsId=goodsId)
		return goodsDetail_cartAdd






if __name__ == '__main__':
	orderBuy = GoodsDetailPageApi().goodsDetail_orderBuy_api('e478da1a76b45472142c2b1eb9600640',4)
	print(orderBuy)
