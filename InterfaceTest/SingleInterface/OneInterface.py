# Data 2020.09.28
import requests

from loguru import logger


class SendRequest:
    url = 'http://192.168.49.96:8090/qjzh-iot-http/report'
    prod_path = '/ZHG/app1/lamp_HttpSvr'

    def One_interface(self, data_json):
        """
           :param prod_path: 具体到产品（/租户/应用/产品）
           :param data_json: {
                       "dev_sn":"sensor_001",在产品静态属性中，创建的设备标识符字段，类似于sn
                       "dev_status":1, 动态属性
                       }
           :return:
           """
        Send_path = self.url + self.prod_path
        logger.info(f'接口url：{Send_path}')
        return requests.post(url=Send_path, json=data_json)


if __name__ == '__main__':
    Request = SendRequest()  # 实例化1111
    # 模拟单个设备请求
    data = {
        "sn": "lamp_002",  # 设备sn
        "brightness": 50,
        "status": "0",
    }
    logger.info('发送的报文%s'%data)
    # 模拟发送请求
    resp = Request.One_interface(data)
    logger.info(f'响应的报文：{resp.text}')
