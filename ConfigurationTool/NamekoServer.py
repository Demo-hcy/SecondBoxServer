from flask import jsonify
from nameko.rpc import rpc


@rpc('/api/devices', mathod=['get'])
def updata(self, payload):
    json_content = {

        [{
            "DevType": "Lamp",
            "DevModel": "YUMIN",
            "ManufacturerId": 122,
            "DevId": 3,
            "Sn": "xxxx",
            "Online": "False",  # 设备检测在线状态结果
            "Description": "paraments error",  # 设置检测结果失败描述
            "Configs": {
                "Port": 3,
                "Addr": "1",
                "Baund": 9600,
                "Parity": "N",
                "Stop": 1,
                "Data": 8
            }}
        ]
    }
    payload = json_content
    return jsonify(payload)


if __name__ == '__main__':
    rpc.run(port=8080, host='192.168.50.131')
