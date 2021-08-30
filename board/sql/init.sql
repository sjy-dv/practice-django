create table board(
    `idx` int(11) not null auto_increment,
    `title` varchar(255) not null,
    `desc` varchar(5000) not null,
    `writer` varchar(255) not null,
    PRIMARY KEY(`idx`)
);

create table member(
    `idx` int(11) not null auto_increment,
    `userid` varchar(255) not null,
    `password` varchar(255) not null,
    PRIMARY KEY(`idx`)
);