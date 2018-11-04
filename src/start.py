# /usr/bin/env python
# -*- coding: utf-8 -*-
from mysql_dao import Dao
from get_rakuten_info import Genrel_info, Rank_info
import logging
import time

# loggerの設定
logger = logging.getLogger("log")
logging.basicConfig(filename="debug.log", filemode='a', level=logging.DEBUG, \
                    format='%(asctime)s:%(levelname)s:%(message)s')
sql = Dao()
test=open("./category.md","a",encoding="utf-8")

# 親ジャンル取得
def genre_insert(noname_lis=[]):
    if noname_lis == []:
        genrel_dict = Genrel_info().get_genrel(0)
        first_list = [0, "category", [],0]
        for x in genrel_dict["children"]:
            id = x["child"]["genreId"]
            name = x["child"]["genreName"]
            level=x["child"]["genreLevel"]
            noname_lis2=[id,name,[],level]
            first_list[2].append(noname_lis2)
        genre_insert(first_list)

    else:
        for x in noname_lis[2]:
            if x[3] < 4 :
                print(noname_lis)
                test.write("    " * (x[3] - 1) + "* " + x[1] + "\n")
                if x[3]<3:
                    genrel_dict = Genrel_info().get_genrel(x[0])
                    for y in genrel_dict["children"]:
                        id =y["child"]["genreId"]
                        name = y["child"]["genreName"]
                        level = y["child"]["genreLevel"]
                        print(level)
                        print(name)
                        noname_lis3 = [id, name, [],level]
                        x[2].append(noname_lis3)
                    genre_insert(x)
                    time.sleep(0.1)
            else:
                return
genre_insert()

test.close()