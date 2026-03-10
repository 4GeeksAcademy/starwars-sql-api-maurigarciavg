from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)  # ✅ Definición correcta del ID
    user_name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)  # 💡 Considera usar 'username' para consistencia
    name: Mapped[str] = mapped_column(String(120), nullable=False)  # ✅ Buen uso de Mapped
    last_name: Mapped[str] = mapped_column(String(120), nullable=False)  # ✅ Buen uso de Mapped
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)  # ✅ Buen uso de Mapped
    suscription_date: Mapped[str] = mapped_column(String(120), nullable=False)  # 💡 Considera usar un tipo de dato más específico
    password: Mapped[str] = mapped_column(String(120), nullable=False)  # ✅ Buen uso de Mapped
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)  # ✅ Buen uso de Mapped
    
    favorite_characters: Mapped[List["FavoriteCharacter"]] = relationship(back_populates="owner")  # ✅ Bien definido
    favorite_planets: Mapped[List["FavoritePlanet"]] = relationship(back_populates="owner")  # ✅ Bien definido

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "user_name": self.user_name,
            "name": self.name,
            "last_name": self.last_name
        }

class Character(db.Model):
    __tablename__ = "character"
    id: Mapped[int] = mapped_column(primary_key=True)  # ✅ Definición correcta del ID
    name: Mapped[str] = mapped_column(String(120), nullable=False)  # ✅ Buen uso de Mapped
    birth_year: Mapped[int] = mapped_column(Integer, nullable=False)  # 💡 Considera usar String si el año puede ser no numérico
    gender: Mapped[str] = mapped_column(String(120), nullable=False)  # ✅ Buen uso de Mapped
    
    fav_chars: Mapped[List["FavoriteCharacter"]] = relationship(back_populates="character")  # ✅ Bien definido

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "gender": self.gender
        }

class Planet(db.Model):
    __tablename__ = "planet"
    id: Mapped[int] = mapped_column(primary_key=True)  # ✅ Definición correcta del ID
    name: Mapped[str] = mapped_column(String(120), nullable=False)  # ✅ Buen uso de Mapped
    climate: Mapped[str] = mapped_column(String(120), nullable=False)  # ✅ Buen uso de Mapped
    population: Mapped[int] = mapped_column(Integer, nullable=False)  # 💡 Considera usar String si la población puede ser no numérica
    
    fav_planets: Mapped[List["FavoritePlanet"]] = relationship(back_populates="planet")  # ✅ Bien definido

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "population": self.population
        }

class FavoriteCharacter(db.Model):
    __tablename__ = "favorite_character"
    id: Mapped[int] = mapped_column(primary_key=True)  # ✅ Definición correcta del ID
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)  # ✅ Buen uso de Mapped
    character_id: Mapped[int] = mapped_column(ForeignKey("character.id"), nullable=False)  # ✅ Buen uso de Mapped
    
    owner: Mapped["User"] = relationship(back_populates="favorite_characters")  # ✅ Bien definido
    character: Mapped["Character"] = relationship(back_populates="fav_chars")  # ✅ Bien definido

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id
        }

class FavoritePlanet(db.Model):
    __tablename__ = "favorite_planet"
    id: Mapped[int] = mapped_column(primary_key=True)  # ✅ Definición correcta del ID
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)  # ✅ Buen uso de Mapped
    planet_id: Mapped[int] = mapped_column(ForeignKey("planet.id"), nullable=False)  # ✅ Buen uso de Mapped
    
    owner: Mapped["User"] = relationship(back_populates="favorite_planets")  # ✅ Bien definido
    planet: Mapped["Planet"] = relationship(back_populates="fav_planets")  # ✅ Bien definido

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id
        }