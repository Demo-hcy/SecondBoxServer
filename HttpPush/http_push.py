# _*_ coding: utf-8 _*_
# Date: 2020/9/17
import time
from loguru import logger
import requests


class SendRequest:
    url = 'http://192.168.49.96:8090/qjzh-iot-http/report'  # 推送属性

    # url = 'http://192.168.49.96:8090/qjzh-iot-http/event'    # 推送事件

    def send_request(self, prod_path, data_json):
        """
        :param prod_path: 具体到产品（/租户/应用/产品）
        :param data_json: {
                    "dev_sn":"sensor_001",在产品静态属性中，创建的设备标识符字段，类似于sn
                    "dev_status":1, 动态属性
                    }
        :return:
        """
        full_url = self.url + prod_path
        logger.info(f'接口url：{full_url}')
        return requests.post(url=full_url, json=data_json)


if __name__ == '__main__':
    prod_path = '/ZHG/app1/lamp_HttpSvr'

    start_time = time.time()  # 开始时间
    to_request = SendRequest()  # 实例化

    # 模拟单个设备请求
    data = {
        "sn": "lamp_002",  # 设备sn
        "brightness": 50,
        "status": "0",
    }

    logger.info(f'发送的报文：{data}')
    # 模拟发送请求
    resp = to_request.send_request(prod_path, data)
    logger.info(f'响应的报文：{resp.text}')

    end_time = time.time()  # 结束时间
    total_time = end_time - start_time  # 总耗时
    logger.info(f'总耗时：{total_time}s')
