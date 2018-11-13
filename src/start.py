# /usr/bin/env python
# -*- coding: utf-8 -*-
import get_rakuten_info
import mysql_dao
import logging
import time

##API設定
#楽天API利用ID
api_id="xxx"
#ジャンルサーチAPIURL
api_url="https://app.rakuten.co.jp/services/api/IchibaGenre/Search/20140222"
#ランキングサーチAPIURL
api_rank_url = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628"

sql = mysql_dao.Dao()
test=open("./category.md","a",encoding="utf-8")

# 親ジャンル取得
def genre_insert(noname_lis=[]):
    #初回のルートジャンルリクエスト場合
    if noname_lis == []:
        genrel_dict = get_rakuten_info.Genrel_info(api_id=api_id,api_url=api_url).get_genrel(0)
        first_list = [0, "category", [],0]
        for x in genrel_dict["children"]:
            id = x["child"]["genreId"]
            name = x["child"]["genreName"]
            level=x["child"]["genreLevel"]
            noname_lis2=[id,name,[],level]
            first_list[2].append(noname_lis2)
        genre_insert(first_list)

    else:
        #２回目以後の処理
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
                #階層が３階層到達した場合、４階層のデータ取得しないように制御
                if x[3]<3:
                    genrel_dict = get_rakuten_info.Genrel_info(api_id=api_id,api_url=api_url).get_genrel(x[0])
                    #レスポンスのjsonのリストデータを順番ずつ処理
                    for y in genrel_dict["children"]:
                        #ジャンルID取得
                        id =y["child"]["genreId"]
                        #ジャンルネーム取得
                        name = y["child"]["genreName"]
                        #現在のジャンルのレベル取得
                        level = y["child"]["genreLevel"]
                        #新しいフォーマットに収納
                        noname_lis3 = [id, name, [],level]
                        #関数もらったnoname_lisリストに２番の空のリストに対して、
                        # 上記新しいデータフォーマットリストを追加
                        x[2].append(noname_lis3)
                    #再帰処理、自分を呼び出して、
                    # 新しいデータフォーマットを追加済みのnoname_lisを渡す
                    genre_insert(x)
                    #リクエストをスリップする。
                    time.sleep(0.1)
            else:
                #4階層のデータあった場合関数を終了
                return

def rank_insert(genre_id):
    # ランクのレスポンスを取得
    rank_info=get_rakuten_info.Rank_info(api_id=api_id,api_url=api_rank_url).get_rank(genrel_id=genre_id)
    #リクエストをスリップ。
    time.sleep(0.5)
    #ランクデータが無い場合があり、DB操作を実施しない。
    if 'error' in rank_info:
        return
    print(rank_info)
    #rankデータのjsonを新しいフォーマットにし、DBにinsert実施。
    for x in rank_info["Items"]:
        name=x["Item"]["itemName"]
        rank=x["Item"]["rank"]
        #ランク１１位以下の場合DBにinsert
        if rank <11:
            sql.inser_tabl_rank(name=name,rank=rank,genre=genre_id)



#再帰処理開始
genre_insert()

#カテゴリーファイルをクローズ
test.close()