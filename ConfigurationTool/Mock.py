# _*_ coding: utf-8 _*_
# Date: 2020/9/3
import json
from flask import Flask, request, jsonify

# 创建一个服务，把当前这个python文件当做一个服务

APP = Flask(__name__)
key = None
IP = None
Configuration = None


# @APP.route()可以将普通函数转变为服务 登录接口的路径、请求方式
@APP.route('/api/login', methods=["post"])
def login():
    """
    盒子模拟配置工具登录接口
    :return:
    """
    global key
    if key is None:
        login_param = request.data
        request_param = json.loads(login_param)
        print(request_param)
        print(type(request_param))
        json_content = {
            "Token": "7GBox",  # 消息来源
            "Sn": "xxx",  # 盒子SN
            "Mac": "12:12:12:12:12:12",  # 盒子mac
            "Key": 132,  # 临时登录秘钥
            "Result": "success"  # 执行结果success/failed
        }
        key = 1
    return jsonify(json_content)


def json_content1_success(args):
    pass


@APP.route('/api/logout', methods=["post"])
def logout():
    """
    盒子模拟配置工具退出接口
    :return:
    """
    global key
    if key == 1:
        logout_param = request.data
        request_param = json.loads(logout_param)
        print(request_param)
        print(type(request_param))
        json_content_success = {
            "Token": "7GBox",  # 消息来源
            "Sn": "xxx",  # 盒子SN
            "Mac": "12:12:12:12:12:12",  # 盒子mac
            "Result": "success"  # 执行结果success/failed
        }
        key = None
    else:
        print("调用接口失败")
        json_content_failed = {
            "Token": "7GBox",  # 消息来源
            "Sn": "xxx",  # 盒子SN
            "Mac": "12:12:12:12:12:12",  # 盒子mac
            "Result": "falsed"  # 执行结果success/failed
        }
        return jsonify(json_content_failed)
    return jsonify(json_content_success)


@APP.route('/api/ip', methods=["get", "post"])
def GetIp():
    """
    盒子模拟配置工具获取IP接口
    :return:
    """
    global IP
    if request.method == "GET":
        GetIp_param = request.data
        request_param = json.loads(GetIp_param)
        print(request_param)
        if IP is None:
            json_content = {
                "Token": "7GBox",
                "Sn": "xxx",
                "Mac": "12:12:12:12:12:12",
                "Ip": "192.168.53.212",
                "Gateway": "192.168.53.1",
                "NetMask": "255.255.255.0",
                "Result": "success"}
        else:
            json_content = {
                "Token": "7GBox",
                "Sn": "xxx",
                "Mac": "12:12:12:12:12:12",
                "Ip": IP,
                "Gateway": "192.168.53.1",
                "NetMask": "255.255.255.0",
                "Result": "success"}
        return jsonify(json_content)
    else:  # 设置盒子IP接口
        GetIp_param = request.data
        request_param = json.loads(GetIp_param)
        IP = request_param.get("Ip")
        json_content = {
            "Token": "7GBox",
            "Sn": "xxx",
            "Mac": "12:12:12:12:12:12",
            "Ip": IP,
            "Result": "success"
        }
        return jsonify(json_content)


# @APP.route('/api/ip', methods=["post"])
# def SetIp():
#     """
#     盒子模拟配置工具设置IP接口
#     :return:
#     """
#     SetIp_param = request.data
#     request_param = json.loads(SetIp_param)
#     print(request_param)
#     print(type(request_param))
#
#     json_content = {
#         "Token": "7GBox",
#         "Sn": "xxx",
#         "Mac": "12:12:12:12:12:12",
#         "Ip": "192.168.53.212",
#         "Result": "success"
#     }
#     return jsonify(json_content)

@APP.route('/api/devices', methods=["get"])
def GetConfiguration():
    """
    盒子模拟个配置工具获取盒子配置接口
    :return:
    """
    GetConfiguration_param = request.data
    request_param = json.loads(GetConfiguration_param)
    print(request_param)
    print(type(request_param))
    if Configuration is None:
        json_content = {
            "Token": "7GTool",
            "Usr": "Admin",
            "PassWd": "Admin123",
            "Key": "123",
            "Sn": "xxx",
            "Mac": "12:12:12:12:12:12",
            "Devices": [
                {
                    "DevType": "GW",
                    "DevModel": "7G",
                    "ManufacturerId": 123,
                    "InterfaceType": "misc",
                    "DevId": 0,
                    "PduPort": 0,
                    "Sn": "xxxx",
                    "Configs": {
                        "ConfigSn": 123,
                        "Ip": "192.168.53.21",
                        "Gateway": "192.168.53.1",
                        "NetMask": "255.255.255.0",
                        "Ntp": "192.168.53.1",
                        "Server": "192.168.53.1",
                        "ConfigServer": "192.168.53.100"
                    }
                },
                {
                    "DevType": "Lamp",
                    "DevModel": "YUMIN",
                    "ManufacturerId": 122,
                    "InterfaceType": "rs485",
                    "DevId": 3,
                    "PduPort": 0,
                    "Sn": "xxxx",
                    "Configs": {
                        "Port": 3,
                        "Addr": "1",
                        "Baund": 9600,
                        "Parity": "N",
                        "Stop": 1,
                        "Data": 8
                    }
                }
            ]
        }
        return jsonify(json_content)


@APP.route('/api/devices', methods=["post"])
def WriteConfiguration():
    """
    盒子模拟个配置工具写入配置接口
    :return:
    """
    WriteConfiguration_param = request.data
    request_param = json.loads(WriteConfiguration_param)
    print(request_param)
    print(type(request_param))
    json_content = {
        "Token": "7GBox",  # 消息来源
        "Sn": "xxx",  # 盒子SN
        "Mac": "12:12:12:12:12:12",  # 盒子mac
        "Result": "success"  # 执行结果success/failed
    }
    return jsonify(json_content)


@APP.route('/api/locker', methods=["get"])
def GetLockStatus():
    """
    盒子模拟个配置工具获取锁的状态接口
    :return:
    """
    GetLockStatus_param = request.data
    request_param = json.loads(GetLockStatus_param)
    print(request_param)
    print(type(request_param))
    json_content = {"Devices": [{
        "DevType": "Locker",
        "DevModel": "RUILON",
        "ManufacturerId": 122,
        "DevId": 3,
        "Sn": "xxxx",
        "Online": "False",  # 设备检测在线状态结果
        "Description": "paraments error",  # 设 置检测结果失败描述
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
    return jsonify(json_content)


@APP.route('/api/infor_screen', methods=["get"])
def InformationScreen():
    """
    盒子模拟个配置工具获取信息屏的状态接口
    大屏：http://192.168.1.212/api/infor_screen
    环境传感: http://ip/api/infor_screen
    Pdu：http://ip/api/pdu
    空开：http://ip/api/breaker
    摄像头：http://ip/api/ipc_onvif
    一键报警：http://ip/api/sos_onvif
    灯：http://ip/api/lamp
    广播：http://ip/api/brocast
    :return:
    """
    InformationScreen_param = request.data
    request_param = json.loads(InformationScreen_param)
    print(request_param)
    print(type(request_param))
    json_content = {"Devices": [{
        "DevType": "Locker",
        "DevModel": "RUILON",
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
    return jsonify(json_content)


@APP.route('/api/activation', methods=["post"])
def Activation():
    """
    盒子模拟个配置工具激活智慧盒接口
    :return:
    """
    Activation_param = request.data
    request_param = json.loads(Activation_param)
    print(request_param)
    print(type(request_param))
    json_content = {
        "Token": "7GBox",
        "Sn": "xxx",
        "Mac": "12:12:12:12:12:12",
        "Activation": "True",
        "Result": "success"
    }
    return jsonify(json_content)


@APP.route('/api/activation', methods=["get"])
def GetActivation():
    """
    盒子模拟个配置工具10、获取当前智盒模式（出厂、配置、入网、激活）接口
    :return:
    """
    GetActivation_param = request.data
    request_param = json.loads(GetActivation_param)
    print(request_param)
    print(type(request_param))
    json_content = {
        "Token": "7GBox",  # 消息来源
        "Sn": "xxx",  # 盒子SN
        "Mac": "12:12:12:12:12:12",  # 盒子mac
        "Activation": 0,  # 0:1:2:3-->出厂、配置、入网、激活
        "Result": "success"  # 执行结果success/failed
    }

    return jsonify(json_content)


@APP.route('/api/reset', methods=["post"])
def ClearConfiguration():
    """
    盒子模拟个配置工具10、获取当前智盒模式（出厂、配置、入网、激活）接口
    :return:
    """
    ClearConfiguration_param = request.data
    request_param = json.loads(ClearConfiguration_param)
    print(request_param)
    print(type(request_param))
    json_content = {
        "Token": "7GBox",  # 消息来源
        "Sn": "xxx",  # 盒子SN
        "Mac": "12:12:12:12:12:12",  # 盒子mac
        "Result": "success"  # 执行结果success/failed
    }
    return jsonify(json_content)


if __name__ == '__main__':
    APP.run(port=8080, host='192.168.50.131')
