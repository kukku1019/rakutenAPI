# rakutenAPI
<<<<<<< HEAD
è®Œï½½èžŸï½©ç¹§?½¸ç¹ï½£ç¹ï½³ç¹ï½«ç¹ï½»ç¹ï½©ç¹ï½³ç¹§?½­ç¹ï½³ç¹§?½°èœ¿é–€?½¾è¼¸PI

#port
mysql> show variables like eportf;
#ƒ†[ƒU\ì¬
create user "test"@"%" identified by 'test';
alter user 'test'@'localhost' identified WITH mysql_native_password by 'test';

#ƒ†[ƒU[Œ ŒÀ•t—^
grant all on *.* to test@localhost;
#Œ ŒÀ”½‰f
FLUSH PRIVILEGES;

#databaseì¬
create database test;
#ƒe[ƒuƒ‹ì¬
create table test.genre1 (genre_id int NOT NULL PRIMARY KEY,genre_name varchar(255));
create table test.rank2 (item_id int AUTO_INCREMENT NOT NULL PRIMARY KEY,item_name varchar(255),rank_num int , genre_id int,foreign key (genre_id) references genre1(genre_id));

=======
æ¥½å¤©ã‚¸ãƒ£ãƒ³ãƒ«ãƒ»ãƒ©ãƒ³ã‚­ãƒ³ã‚°APIå–å¾—ã‚¹ã‚¯ãƒªãƒ—ãƒˆ
>>>>>>> 614fb11344e63f6ae825d92c450235f4777d6d75
