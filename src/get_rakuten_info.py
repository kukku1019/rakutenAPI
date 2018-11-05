# /usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import logging

# loggerの設定
logger = logging.getLogger("log")
logging.basicConfig(filename="debug.log", filemode='a', level=logging.DEBUG, \
                    format='%(asctime)s:%(levelname)s:%(message)s')


class Genrel_info():
    def __init__(self, api_id="xxxxxxxxx", \
                 api_url="https://app.rakuten.co.jp/services/api/IchibaGenre/Search/20140222", \
                 header={"Content-Type": "application/json"}):

        # API利用すためのID
        self.api_id = api_id
        # ジャンルサーチのAPI
        self.api_url = api_url
        self.header = header

    # ジャンルJSON取得メソッド
    def get_genrel(self, genrel_id):
        param = {"applicationId": self.api_id, "genreId": genrel_id}
        try:
            resp = requests.get(self.api_url, headers=self.header, params=param)
            logger.debug(str(genrel_id) + ":genrel_serch request ok")
        except:
            logger.warning(str(genrel_id) + "genrel_serch request error")
        return resp.json()


class Rank_info():
    def __init__(self,api_id = "xxxxxxxxxx",\
                 api_url = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628",
                 header={"Content-Type": "application/json"}):

        self.api_id = api_id
        self.api_url = api_url
        self.header=header

    def get_rank(self, genrel_id):
        param = {"applicationId": self.api_id, "genreId": genrel_id}
        try:
            resp = requests.get(self.api_url, headers=self.header, params=param)
            logger.debug(str(genrel_id) + ":rank_serch request ok")
        except:
            logger.warning(str(genrel_id) + "rank_serch request failed")

        return resp.json()
