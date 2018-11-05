# rakutenAPIデータ取得準備

#mysqlインストール
<p>brew install mysql</p>

#port確認
<p>show variables like ‘port’</p>

#user作成
<p>create user "test"@"%" identified by 'test';</p>
<p>alter user 'test'@'localhost' identified WITH mysql_native_password by 'test';</p>

#ユーザー権限付与
<p>grant all on *.* to 'test'@'%';</p>

#設定保存
<p>FLUSH PRIVILEGES;</p>

#databaseを作成
<p>create database test;</p>

#テーブル作成
<p>create table test.genre1 (genre_id int NOT NULL PRIMARY KEY,genre_name varchar(255));</p>
<p>create table test.rank2 (item_id int AUTO_INCREMENT NOT NULL PRIMARY KEY,item_name varchar(255),rank_num int , genre_id int,foreign key (genre_id) references genre1(genre_id));</p>

#python用mysqlパッケージインストール
<p>pip install mysql-connector-python-rf</p>


