# rakutenAPI
<<<<<<< HEAD
讌ｽ螟ｩ繧?��繝｣繝ｳ繝ｫ繝ｻ繝ｩ繝ｳ繧?��繝ｳ繧?��蜿門?��輸PI

#port
mysql> show variables like �eport�f;
#���[�U�\�쐬
create user "test"@"%" identified by 'test';
alter user 'test'@'localhost' identified WITH mysql_native_password by 'test';

#���[�U�[�����t�^
grant all on *.* to test@localhost;
#�������f
FLUSH PRIVILEGES;

#database�쐬
create database test;
#�e�[�u���쐬
create table test.genre1 (genre_id int NOT NULL PRIMARY KEY,genre_name varchar(255));
create table test.rank2 (item_id int AUTO_INCREMENT NOT NULL PRIMARY KEY,item_name varchar(255),rank_num int , genre_id int,foreign key (genre_id) references genre1(genre_id));

=======
楽天ジャンル・ランキングAPI取得スクリプト
>>>>>>> 614fb11344e63f6ae825d92c450235f4777d6d75
