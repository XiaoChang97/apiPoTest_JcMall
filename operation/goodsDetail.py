from operation.base_op import BaseOP
from py_page.goodsDetail_page import GoodsDetailPageApi
from py_page.shopCar_page import ShopCarPageApi

class GoodsDetail(BaseOP):

	def __init__(self):
		self.token = self.get_token()

	def addGoods_in_shopCar(self,goodsId):
		res = GoodsDetailPageApi(token=self.token).goodsDetail_cartAdd_api(goodsId=goodsId)
		return res

	def dellGoods_in_shopCar(self,cartId):
		res = ShopCarPageApi(token=self.token).cart_del_api(cart_id=cartId)
		return res

