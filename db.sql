CREATE table User
(
    userId   INTEGER not null
        primary key autoincrement,
    userName text(50),
    password text(100)
);

CREATE table Games
(
    gameId    INTEGER not null
        primary key autoincrement,
    player1Id INTEGER not null,
    player2Id INTEGER not null,
    winner    INTEGER
);

CREATE table statistic
(
    userId        INTEGER not null
        references User,
    numberOfGames INTEGER,
    numberOfWins  INTEGER
);