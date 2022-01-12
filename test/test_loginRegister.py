import pytest
import allure

from operation.registerLogin import RegisterLogin

@allure.feature("测试注册登录接口")
class TestLoginRegister:

	@allure.story("用正确的账号登录")
	@pytest.mark.parametrize('mobile,password',[('15200000001','111111.')])
	def test_login_01(self,mobile,password):
		register_login = RegisterLogin()
		login = register_login.login(mobile,password)
		status_code = login['status_code']
		msg = login['content']['msg']
		pytest.assume(status_code==200)
		pytest.assume(msg=='登录成功')

	@allure.story("用错误的密码登录")
	@pytest.mark.parametrize('mobile,password', [('15200000001', '1111111')])
	def test_login_02(self,mobile,password):
		register_login = RegisterLogin()
		login = register_login.register(mobile, password)
		status_code = login['status_code']
		msg = login['content']['msg']
		pytest.assume(status_code == 200)
		pytest.assume(msg == '密码错误')
