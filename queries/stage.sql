CREATE TABLE Stage (
    URL NOT NULL TEXT PRIMARY KEY,
    News int DEFAULT 0,
    Fun int DEFAULT 0,
    SocialMedia int DEFAULT 0,
    ICC int DEFAULT 0, -- internet censorship circumvention 
    LifeStyle int DEFAULT 0,
    Services int DEFAULT 0,
    Shop int DEFAULT 0,
    Community int DEFAULT 0,
    Education int DEFAULT 0,
);