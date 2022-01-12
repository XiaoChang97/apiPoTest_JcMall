import requests
import yaml
from requests.packages import urllib3
import json
from string import Template

from log import Logger

logging = Logger(__name__)
class BaseApi:
    urllib3.disable_warnings()
    def request_api(self,method=None,api=None,params=None,data=None,json=None,headers=None,res_type='json',verify=False,**kwargs)->dict:
        host = "https://mall.jctesting.cn"
        api_url = host+api
        res_dict = dict()
        if method == 'get':
            try:
                res = requests.get(url=api_url,params=params,headers=headers,verify=verify)
                if res_type == 'json':
                    res_content = res.json()
                else:
                    res_content = res.text
                res_dict['status_code'] = res.status_code
                res_dict['content'] = res_content
                return res_dict
            except Exception as e:
                logging.logger.error(f"接口::{api}::请求出错::{e}")

        elif method == 'post':
            try:
                res = requests.post(url=api_url,data=data,json=json,headers=headers,verify=verify)
                if res_type == 'json':
                    res_content = res.json()
                else:
                    res_content = res.text
                res_dict['status_code'] = res.status_code
                res_dict['content'] = res_content
                return res_dict
            except Exception as e:
                logging.logger.error(f"接口::{api}::请求出错::{e}")


    def run_requests(self,yaml_path,api_name,**kwargs):
        try:
            with open(yaml_path,"r",encoding="UTF-8") as f:
                yaml_datas = yaml.safe_load(f)
                datas = yaml_datas[f'{api_name}']
                datas_str = json.dumps(datas)
                datas_str_var = Template(datas_str).substitute(kwargs)
                api_datas = json.loads(datas_str_var)
                logging.logger.info(f"读取YAML文件::{yaml_path}::请求的接口名称::{api_name}::传入接口参数::{kwargs}::接口请求参数api_datas::{api_datas}")
                request = self.request_api(method=api_datas['method'],api=api_datas['api'],headers=api_datas['headers'],
                                           params=api_datas['params'],data=api_datas['data'],json=api_datas['json'])
                logging.logger.info(f"接口::{api_datas['api']}::响应数据为::{request}")
                return request
        except Exception as e:
            logging.logger.error(f"读取YAML文件::{yaml_path}出错::{e}")





# if __name__ == '__main__':
#     r = BaseApi().run_requests("..\yaml_api\\registerlogin_page.yaml","register",token=1234345,goodsId=4)


