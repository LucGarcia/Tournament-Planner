Overview
--------

Tournament Planner is the 4th project in the Udacity Full Stack Web Developer Nanodegree.

In it, a database API is used to manage a swiss-style tournament, allowing users to add players and results from matches to a PostgreSQL database, as well as planning the next round of matches by pairing players with opponents with a similar number of wins.


Contents
--------

* tournament.sql: creates and configures the database schema, which includes two tables
_players_, containing a sequentially-assigned numeric ID and the name of the player;
_matches_, containing a sequentially-assigned match ID, a winner ID and a loser ID which both reference the ID in table players;
and a view _ranking_, that creates a list of players including ID, name, matches won and matches played.

* tournament.py: includes the functions to handle interactions with the database, such as connect with the database, register players, record the results from matches, delete players and matches records, create a ranking list or return a list of pairings for the next round of matches.

* tournament_test.py: this file is a test designed to ensure both the database and the API work.

* lil_test.py: simulates a tournament with 100 matches between players, and was used in production to test functions and queries.


Requirements
------------

Python 2.7 or superior.
PostgreSql
Psycopg2


Installation and usage
----------------------

To use it on a tournament:

1. clone the repository to your local computer.
2. cd to the tournaments file.
3. import tournament on a Python shell and use the functions, for example:
```python
import tournament.py
registerPlayer('John Doe')
```

To create yourself the database API and SQL file (as practice with database manipulation):

1. clone the repository to your local computer.
2. erase the code from the tournament.py and tournament.sql files, except the comments and function names.
3. write your code.
4. you can run ``` python lil_test.py``` during production and ``` python tournament_test.py``` to test all functions in your API.








