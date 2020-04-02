import requests


def request(method, url, jsondata={}, headers={}, httpcode=200, aresult=200):
    """
        名称：
            请求核心引擎
        参数：
            url：地址
            method：请求的方法
            jsondata：json格式的参数
            headers：请求头
        返回值：
            true：通过
            false：失败
    """
    res = requests.request(method, url=url, json=jsondata, headers=headers)
    try:
        assert httpcode == res.status_code
        assert aresult == res.json()["status"]
        return True
    except:
        return False
