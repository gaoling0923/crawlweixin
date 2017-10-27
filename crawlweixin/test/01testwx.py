import requests


# class WeiXinLogin(View):
class WeiXinLogin():
    appid = 'wx6634d697e8cc0a29'  # 你自己的
    appsecret = 'd785bt925fbc7ebed62734cfdpe5951c'  # 你自己的
    code = ''
    state = ''

    # 为了方便大家看,我都写在一个函数里
    def get_info(self):

        # 第一步获取code跟state
        try:
            self.code = self.request.GET.get("code")
            self.state = self.request.GET.get("state")
        except Exception as e:
            print("获取code和stat参数错误：")

        # 2.通过code换取网页授权access_token
        try:
            url = u'https://api.weixin.qq.com/sns/oauth2/access_token'
            params = {
                'appid': self.appid,
                'secret': self.appsecret,
                'code': self.code,
                'grant_type': 'authorization_code'
            }
            res = requests.get(url, params=params).json()

            access_token = res["access_token"]  # 只是呈现给大家看,可以删除这行
            openid = res["openid"]  # 只是呈现给大家看,可以删除这行
        except Exception as e:
            print("获取access_token参数错误：")
        # 3.如果access_token超时，那就刷新
        # 注意,这里我没有写这个刷新功能,不影响使用,如果想写的话,可以自己去看文档

        # 4.拉取用户信息
        try:
            user_info_url = u'https://api.weixin.qq.com/sns/userinfo'
            params = {
                'access_token': res["access_token"],
                'openid': res["openid"],
            }
            res = requests.get(user_info_url, params=params).json()
            """
            注意,这里有个坑,res['nickname']表面上是unicode编码,
            但是里面的串却是str的编码,举个例子,res['nickname']的返回值可能是这种形式
            u'\xe9\x97\xab\xe5\xb0\x8f\xe8\x83\x96',直接存到数据库会是乱码.必须要转成
            unicode的编码,需要使用
            res['nickname'] = res['nickname'].encode('iso8859-1').decode('utf-8')
            这种形式来转换.
            你也可以写个循环来转化.
            for value in res.values():
                value = value.encode('iso8859-1').decode('utf-8')
            """
        except Exception as e:
            print("拉取用户信息错误")

        # 保存到数据库及登录
        # 返回的数据全部在res字典中

if __name__ == '__main__':
    print('开始')
    tt=WeiXinLogin()
    tt.get_info()