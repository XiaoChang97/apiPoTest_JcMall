from py_page.base_api import BaseApi


class HomePageApi(BaseApi):

	def __init__(self,path="./yaml_api/home_page.yaml",token=None):
		self.path = path
		self.token = token

	def goods_categoryList_api(self):
		categoryList = self.run_requests(self.path,'goods_category', token=self.token)
		return categoryList

	def commonData_api(self):
		commonData = self.run_requests(self.path,'commonData', token=self.token)
		return commonData

	def pcIndex_api(self):
		pcIndex = self.run_requests(self.path,'index', token=self.token)
		return pcIndex

	def getGoodsDetail_api(self,id):
		getGoodsDetail = self.run_requests(self.path,'getGoodsDetail', token=self.token, id=id)
		return getGoodsDetail

	def searchGoodsList_api(self,name):
		searchGoodsList = self.run_requests(self.path, 'searchGoodsList', token=self.token, name=name)
		return searchGoodsList

	def shopCarList_api(self):
		shopCarList = self.run_requests(self.path, 'shopCarList', token=self.token)
		return shopCarList



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
