from flask_sqlalchemy import SQLAlchemy
from typing import Any

db = SQLAlchemy()


class Game(db.Model):
    __tablename__ = "games"
    id = db.Column(db.Integer, primary_key=True)
    players = db.relationship("Player", backref="game", lazy=True)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    hash = db.Column(db.String, nullable=True)

    def add_user(self, username, hash):
        #to do


class Player(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    game_id = db.Column(db.Integer, db.ForeignKey("games.id"))

    
class Tiles(db.Model):
    __tablename__ = "tiles"
    id = db.Column(db.Integer, primary_key=True)
    suit = db.Column(db.String, nullable=False)
    value = db.Column(db.String, nullable=False)

    
class GameTiles(db.Model):
    __tablename__ = "game_tiles"
    tiles_id = db.Column(db.Integer, db.ForeignKey("tiles.id"))
    game_id = db.Column(db.Integer, db.Foreignkey("games.id"))
    player_id = db.Column(db.Integer, db.ForeignKey("players.id"))
    location = db.Column(db.String, Nullable=False)


    def __init__(self, tiles_id, game_id, player_id, location):
        self.tiles_id = tiles_id
        self.game_id = game_id
        self.player_id = player_id
        self.location = location
                         
    def initialize_wall(self) -> None:
        """
        initializes a wall of all the tiles that the game starts with

        post: returns None, only has side effect that a list of tiles is made
        """
        # for every tile in Tiles
        #   add to the database

        
    def description(self, location: str) -> int:
        """
        describes how many tiles are in the specified location

        pre: location = str and exists in the game
        post: returns integer of amount of tiles
        """
        # query for all the tiles in that location

        # return len(rows)

        
    def deal_hand(self, player_id: int, location: str) -> None:
        """
        Deals the first hand of the game, where everybody gets 13 tiles

        pre: player_id = int and exists in the game, location: string and exists in the game
        post: list is made?
        """
        # query and randomize
        # randomize and deal limit 13
        # delete those things from the database
        
    def deal_tile:
        # randomize and deal limit 1



class Hand(db.Model):
    __tablename__ = "hand"
    player_id = db.Column(db.Integer, Foreign_key("players.id"))
    tile_id = db.Column(db.Integer, Foreign_key("tiles.id")
    
class C
    
    def __init__(self) -> None:
        # query de database for every card
        self._tiles: list[Tile] = []

        for row in self.all:
            id = query(id)
            suit = query(suit)
            value = query(value)
            tile = Tile(id, suit, value)
            self._tiles.append(tile)


        def tiles_left(self) -> int:
            when deal_tile gaat er een vanaf
        
        def shuffle(self) -> None:
            random.shuffle(self._cards)
        
        def deal_tile(self) -> Card:
            return self._tiles.pop()
        
            
class Tile:

    def __init__(self, id: int, suit: str, value: Any) -> None:
        self.id = id
        self.suit = suit
        self.value = value

