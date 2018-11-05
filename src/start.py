# /usr/bin/env python
# -*- coding: utf-8 -*-
import get_rakuten_info
import mysql_dao
import logging
import time

# loggerの設定
logger = logging.getLogger("log")
logging.basicConfig(filename="debug.log", filemode='a', level=logging.INFO, \
                    format='%(asctime)s:%(levelname)s:%(message)s')
sql = mysql_dao.Dao()
test=open("./category.md","a",encoding="utf-8")

# 親ジャンル取得
def genre_insert(noname_lis=[]):
    if noname_lis == []:
        genrel_dict = get_rakuten_info.Genrel_info().get_genrel(0)
        first_list = [0, "category", [],0]
        for x in genrel_dict["children"]:
            id = x["child"]["genreId"]
            name = x["child"]["genreName"]
            level=x["child"]["genreLevel"]
            noname_lis2=[id,name,[],level]
            first_list[2].append(noname_lis2)
        genre_insert(first_list)

    else:
        #受け取ったリスト引き数の２番のリストを繰り返し処理
        for x in noname_lis[2]:
            #受け取ったリスト　階層を確認、４階層以下であれば処理続行
            if x[3] < 4 :
                #カテゴリーの作成
                test.write("    " * (x[3] - 1) + "* " + x[1] + "\n")
                #DBジャンルテーブルへのインサート
                sql.insert_tabl_genre1(genre_id=x[0],genre_name=x[1])
                #rank情報インサート
                rank_insert(genre_id=x[0])
                print(x)

                if x[3]<3:
                    genrel_dict = get_rakuten_info.Genrel_info().get_genrel(x[0])
                    for y in genrel_dict["children"]:
                        id =y["child"]["genreId"]
                        name = y["child"]["genreName"]
                        level = y["child"]["genreLevel"]
                        noname_lis3 = [id, name, [],level]
                        x[2].append(noname_lis3)
                    genre_insert(x)
                    time.sleep(0.1)
            else:
                return

def rank_insert(genre_id):
    # ランク取得
    rank_info=get_rakuten_info.Rank_info().get_rank(genrel_id=genre_id)
    time.sleep(0.5)
    if 'error' in rank_info:
        return
    print(rank_info)
    for x in rank_info["Items"]:
        name=x["Item"]["itemName"]
        rank=x["Item"]["rank"]
        if rank <11:
            sql.inser_tabl_rank(name=name,rank=rank,genre=genre_id)



#再帰処理開始
genre_insert()

#カテゴリーファイルをクローズ
test.close()