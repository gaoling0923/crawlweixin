from weixin.client import WeixinMpAPI

scope = ("snsapi_base", )
api = WeixinMpAPI(appid='wx6634d697e8cc0a29',
                  app_secret=APP_SECRET,
                  redirect_uri=REDIRECT_URI)
authorize_url = api.get_authorize_url(scope=scope)

access_token = api.exchange_code_for_access_token(code=code)

api = WeixinMpAPI(access_token=access_token)

user = api.user(openid="openid")