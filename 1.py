url = "https://api.upbit.com/vi/ticker"
            param = {"markets": "KRW=BTC"}
            # "https://api.upbit.com/v1/ticker?markets=KRW-DOGE"
            response = requests.get(url, params=param)
            result = response.json()