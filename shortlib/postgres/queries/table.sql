CREATE TABLE URLS (
    Original text NOT NULL ,
    New text NOT NULL PRIMARY KEY,
    ClickCount int DEFAULT 0,
    OwnerID bigint NOT NULL,
    OwnerChannel varchar(255),
    Lifetime bigint,
    CreatedAt Date
);