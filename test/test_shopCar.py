import pytest
import allure

from operation.shopCar import ShopCar
from log import Logger

logging = Logger(__name__)
@allure.feature("测试购物车")
class TestShopCar:

	logging.logger.info("############开始测试购物车接口逻辑############")

	@allure.story("把商品加入购物车")
	def test_addGoods_shopCar_01(self,goodsId=4):
		logging.logger.info(f"************开始执行测试用例::test_addGoods_shopCar_01::把商品{goodsId}加入购物车************")
		with allure.step("删除购物车中的所有商品"):
			cart_ids = ShopCar().getCartIdsList_from_shopCar()
			if len(cart_ids)>0:
				for cart_id in cart_ids:
					ShopCar().dellGoods_in_shopCar(cart_id)
		with allure.step(f"把商品{goodsId}加入购物车"):
			addGoods = ShopCar().addGoods_in_shopCar(goodsId=goodsId)
		with allure.step(f"查看购物车列表"):
			shopCarList = ShopCar().getCar_goodsList()
		addGoods_status_code = addGoods['status_code']
		addGoods_msg = addGoods['content']['msg']
		shopCarList_status_code = shopCarList['status_code']
		shopCarList_goodsId = shopCarList['content']['data']['lists'][0]['goods_id']

		pytest.assume(addGoods_status_code==200)
		pytest.assume(addGoods_msg=='加入成功')
		pytest.assume(shopCarList_status_code == 200)
		pytest.assume(shopCarList_goodsId==goodsId)

	@allure.story("把商品从购物车中删除")
	def test_dellGoods_shopCar_02(self,goodsId=4):
		logging.logger.info(f"************开始执行测试用例::test_dellGoods_shopCar_02::把商品从购物车中删除************")
		with allure.step("把商品加入购物车"):
			ShopCar().addGoods_in_shopCar(goodsId=goodsId)
		with allure.step("删除购物车中的所有商品"):
			cart_ids = ShopCar().getCartIdsList_from_shopCar()
			if len(cart_ids) > 0:
				for cart_id in cart_ids:
					ShopCar().dellGoods_in_shopCar(cart_id)
		with allure.step(f"查看购物车列表"):
			shopCarList = ShopCar().getCar_goodsList()
		shopCarList_status_code = shopCarList['status_code']
		shopCarList_goodsList = shopCarList['content']['data']['lists']

		pytest.assume(shopCarList_status_code == 200)
		pytest.assume(len(shopCarList_goodsList) == 0)
