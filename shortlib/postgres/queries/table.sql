CREATE TABLE URLS (
    Original text NOT NULL,
    New text NOT NULL PRIMARY KEY,
    OwnerID bigint NOT NULL,
    OwnerChannel varchar(255),
    Lifetime bigint,
    CreatedAt timestamp default NOW()
);

CREATE TABLE Clicks (
    URL text NOT NULL,
    IPV4 varchar(16) NOT NULL,
    UserAgent text,
    clickTime timestamp default NOW()::timestamp,
    PRIMARY KEY (URL, IPV4)
);