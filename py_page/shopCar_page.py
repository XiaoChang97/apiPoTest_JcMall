from py_page.base_api import BaseApi
from py_page.home_page import HomePageApi


class ShopCarPageApi(BaseApi):

	def __init__(self,path="./yaml_api/shopCar_page.yaml",token=None):
		self.path = path
		self.token = token

	def cart_del_api(self,cart_id):
		cart_del = self.run_requests(self.path,'cart_del', token=self.token, cart_id=cart_id)
		return cart_del

	def get_carList_cart_ids(self):
		cartId_list = list()
		carList = HomePageApi(token=self.token).shopCarList_api()
		goodsList = carList['content']['data']['lists']
		if len(goodsList)>0:
			for goods in goodsList:
				cartId_list.append(goods['cart_id'])
		return cartId_list




if __name__ == '__main__':
	# categoryList = HomePageApi().goods_categoryList_api('978dcfb7e39caf9ba1cce14aa10f23a7')
	# print(categoryList)
	# commonData = HomePageApi().commonData_api('978dcfb7e39caf9ba1cce14aa10f23a7')
	# print(commonData)
	getGoodsDetail = HomePageApi().getGoodsDetail_api('978dcfb7e39caf9ba1cce14aa10f23a7',4)
	print(getGoodsDetail)
	pcIndex = HomePageApi().pcIndex_api('978dcfb7e39caf9ba1cce14aa10f23a7')
	print(pcIndex)
	# searchGoodsList = HomePageApi().searchGoodsList_api('978dcfb7e39caf9ba1cce14aa10f23a7', '小米')
	# print(searchGoodsList)
