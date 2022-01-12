from py_page.base_api import BaseApi


class RegisterLoginPageApi(BaseApi):

	def __init__(self,path="./yaml_api/registerlogin_page.yaml",token=None):
		self.path = path
		self.token = token

	def login_api(self,account,password):
		login = self.run_requests(self.path,'login', account=account,password=password)
		return login

	def register_api(self,mobile,password):
		register = self.run_requests(self.path,'register', mobile=mobile,password=password)
		return register



if __name__ == '__main__':
	login = RegisterLoginPageApi().login_api('15200000002','111111.')
	print(login)
	register = RegisterLoginPageApi().register_api('15200000001','111111.')
	print(register)
