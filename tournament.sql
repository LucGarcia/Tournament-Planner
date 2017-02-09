-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Drop database if it already exists.
DROP DATABASE tournament;

-- Create database and assign name.
CREATE DATABASE tournament;

-- Connect to the database.
\c tournament;

-- Create a table for all players, including a name and an id.
CREATE TABLE players (
    id serial PRIMARY KEY,
    name text
    );

-- Create a table to store the matches with the results.
CREATE TABLE matches (
    match_id serial PRIMARY KEY,
    winner integer REFERENCES players(id),
    loser integer REFERENCES players(id)
    );

-- Create a view for the general ranking, which will return player id, player
-- name, number of wins and total games played, ordered from the player with
-- most wins to the one with least wins.
CREATE VIEW ranking AS
SELECT players.id, players.name,
    (SELECT count(matches.winner) FROM matches
        WHERE players.id = matches.winner) AS wins,
    (SELECT count(matches.match_id) FROM matches
        WHERE players.id = matches.winner OR
        players.id = matches.loser) AS matches
FROM players
ORDER BY wins DESC, matches DESC;