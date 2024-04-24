from flask_sqlalchemy import SQLAlchemy
from typing import Any

db = SQLAlchemy()


class Game(db.Model):
    __tablename__ = "games"
    id = db.Column(db.Integer, primary_key=True)
    players = db.Column(db.String, nullable=False)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    game_id = db.Column(db.Integer)


class Tiles(db.Model):
    __tablename__ = "all_tiles"
    id = db.Column(db.Integer, primary_key=True)
    suit = db.Column(db.String, nullable=False)
    value = db.Column(db.String, nullable=False)


class Wall:
    __tablename__ = "wall"
    game_id = db.Column(db.Integer, Foreign_key=True)
    tile_id = db.Column(db.Integer, Foreign_key=True)

    def initialize:
        # start up the wall with the randomized tiles?

    def startup_hand:
        # randomize and deal limit 13
        
    def deal_tile:
        # randomize and deal limit 1



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

