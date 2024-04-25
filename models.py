from flask_sqlalchemy import SQLAlchemy
from typing import Any

db = SQLAlchemy()


class Game(db.Model):
    __tablename__ = "games"
    id = db.Column(db.Integer, primary_key=True)
    players = db.relationship("Player", backref="game", lazy=True)
    tiles = db.relationship("GameTiles", lazy=True)
#    active_player = "one to one relationship"
                             
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

                
    # def deal_tile(self) -> None:
    #     # randomize and deal limit 1

    
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    hash = db.Column(db.String, nullable=True)

    # def add_user(self, username, hash):
    #     #to do


class Player(db.Model):
    __tablename__ = "players"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    game_id = db.Column(db.Integer, db.ForeignKey("games.id"))

    
class Tile(db.Model):
    __tablename__ = "tiles"
    id = db.Column(db.Integer, primary_key=True)
    suit = db.Column(db.String, nullable=False)
    value = db.Column(db.String, nullable=False)

    
class GameTiles(db.Model):
    __tablename__ = "game_tiles"
    id = db.Column(db.Integer, primary_key=True)
    tiles_id = db.Column(db.Integer, db.ForeignKey("tiles.id"))
    game_id = db.Column(db.Integer, db.ForeignKey("games.id"))
    player_id = db.Column(db.Integer, db.ForeignKey("players.id"))
    location = db.Column(db.String, nullable=False)


    def __init__(self, tiles_id, game_id, player_id, location):
        self.tiles_id = tiles_id
        self.game_id = game_id
        self.player_id = player_id
        self.location = location



class Hand(db.Model):
    __tablename__ = "hand"
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey("players.id"))
    tile_id = db.Column(db.Integer, db.ForeignKey("tiles.id"))
    
