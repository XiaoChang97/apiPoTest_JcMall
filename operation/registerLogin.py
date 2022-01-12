from py_page.registerLogin_page import RegisterLoginPageApi

class RegisterLogin:

	def login(self,account,password):
		login_res = RegisterLoginPageApi().login_api(account,password)
		return login_res


	def register(self,mobile,password):
		register_res = RegisterLoginPageApi().register_api(mobile,password)
		return register_res
