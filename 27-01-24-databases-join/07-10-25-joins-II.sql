 create database football_db;


 \c football_db 

 CREATE TABLE Players (
    player_name VARCHAR(100) PRIMARY KEY,
    club_name VARCHAR(100),
    national_team_name VARCHAR(100)
);

CREATE TABLE Clubs (
    club_name VARCHAR(100) PRIMARY KEY,
    country VARCHAR(100)
);

CREATE TABLE NationalTeams (
    national_team_name VARCHAR(100) PRIMARY KEY,
    continent VARCHAR(100)
);

INSERT INTO NationalTeams (national_team_name, continent)
VALUES 
    ('Brazil', 'South America'),
    ('Germany', 'Europe'),
    ('Argentina', 'South America'),
    ('France', 'Europe'),
    ('Spain', 'Europe'),
    ('Nigeria', 'Africa'),
    ('Japan', 'Asia');

INSERT INTO Clubs (club_name, country)
VALUES 
    ('Real Madrid', 'Spain'),
    ('Bayern Munich', 'Germany'),
    ('PSG', 'France'),
    ('Barcelona', 'Spain'),
    ('Chelsea', 'England'),
    ('Juventus', 'Italy'),
    ('Santos', 'Brazil');

INSERT INTO Players (player_name, club_name, national_team_name)
VALUES 
    ('Lionel Messi', 'PSG', 'Argentina'),
    ('Cristiano Ronaldo', 'Juventus', 'Portugal'),
    ('Neymar Jr', 'PSG', 'Brazil'),
    ('Kylian Mbappe', 'PSG', 'France'),
    ('Thomas Muller', 'Bayern Munich', 'Germany'),
    ('Manuel Neuer', 'Bayern Munich', 'Germany'),
    ('Gerard Pique', 'Barcelona', 'Spain'),
    ('Sergio Ramos', 'Real Madrid', 'Spain'),
    ('Eden Hazard', 'Real Madrid', 'Belgium'),
    ('Victor Osimhen', 'Chelsea', 'Nigeria'),
    ('Takumi Minamino', 'Chelsea', 'Japan'),
    ('Paulo Dybala', 'Juventus', 'Argentina'),
    ('Marquinhos', 'Santos', 'Brazil'),
    ('Thiago Silva', 'Chelsea', 'Brazil');



SELECT p.player_name,nt.national_team_name
FROM Players p INNER JOIN NationalTeams nt ON
p.national_team_name = nt.national_team_name;

SELECT p.player_name,c.club_name FROM 
Players p INNER JOIN CLubs c ON
p.club_name = c.club_name;

SELECT c.club_name , p.player_name FROM
Clubs c LEFT JOIN Players p ON c.club_name = p.club_name;

SELECT national_team_name nt, p.player_name FROM
NationalTeams nt LEFT JOIN Players p ON nt.national_team_name = p.national_team_name;


SELECT p.player_name,c.club_name,nt.national_team_name FROM
Players p INNER JOIN Clubs c ON c.club_name = p.club_name 
INNER JOIN NationalTeams nt ON nt.national_team_name = p.national_team_name;