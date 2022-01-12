from operation.registerLogin import RegisterLogin
from log import Logger
import yaml

logging = Logger(__name__)
class BaseOP:

	def get_account(self,path=r'./config.yaml'):
		with open(path,'r',encoding="UTF-8") as f:
			config = yaml.safe_load(f)
			return config['login']


	def get_token(self):
		login = RegisterLogin().login(account=self.get_account()['account'],password=self.get_account()['password'])
		token = login['content']['data']['token']
		logging.logger.info(f"get_token获取到的token为::{token}")
		return token