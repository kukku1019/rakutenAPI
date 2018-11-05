# rakutenAPIデータ取得準備

#mysqlインストール
brew install mysql

#port確認
show variables like ‘port’

#user作成
create user "test"@"%" identified by 'test';
alter user 'test'@'localhost' identified WITH mysql_native_password by 'test';

#ユーザー権限付与
grant all on *.* to 'test'@'%';

#設定保存
FLUSH PRIVILEGES;

#databaseを作成
create database test;

#テーブル作成
create table test.genre1 (genre_id int NOT NULL PRIMARY KEY,genre_name varchar(255));
create table test.rank2 (item_id int AUTO_INCREMENT NOT NULL PRIMARY KEY,item_name varchar(255),rank_num int , genre_id int,foreign key (genre_id) references genre1(genre_id));

#python用mysqlパッケージインストール
pip install mysql-connector-python-rf


