#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2

import bleach


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    c = db.cursor()
    query = 'DELETE FROM matches;'
    c.execute(query)
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    c = db.cursor()
    query = 'DELETE FROM players;'
    c.execute(query)
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    c = db.cursor()
    query = 'SELECT count(*) FROM players;'
    c.execute(query)
    count = c.fetchone()[0]
    db.close()
    return count


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    c = db.cursor()
    query = 'INSERT INTO players (name) VALUES (%s);'
    safe_name = bleach.clean(name)  # to sanitize input
    c.execute(query, (safe_name,))
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    c = db.cursor()
    query = 'SELECT * FROM ranking;'
    c.execute(query)
    standings = c.fetchall()
    db.close()
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    c = db.cursor()
    query = 'INSERT INTO matches (winner, loser) VALUES (%s, %s);'
    safe_winner = bleach.clean(winner)
    safe_loser = bleach.clean(loser)
    c.execute(query, (safe_winner, safe_loser))
    db.commit()
    db.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    # Acquiring ids and names from view ranking.
    db = connect()
    c = db.cursor()
    c.execute('SELECT name FROM ranking;')
    names = c.fetchall()
    c.execute('SELECT id FROM ranking;')
    ids = c.fetchall()
    # Create list.
    playlist = []
    ids_count = 0
    names_count = 0

    for i in range(len(ids) / 2):
        playlist.extend(zip(ids[ids_count],
                            names[names_count],
                            ids[ids_count + 1],
                            names[names_count + 1]))
        ids_count += 2
        names_count += 2

    db.close()
    return playlist
