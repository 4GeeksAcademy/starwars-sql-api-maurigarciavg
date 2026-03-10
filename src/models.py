from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)  # 🔧 Definido correctamente como primary_key
    user_name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)  # ✅ Bien hecho: username único
    name: Mapped[str] = mapped_column(String(120), nullable=False)  # ✅ Bien hecho: nombre
    last_name: Mapped[str] = mapped_column(String(120), nullable=False)  # ✅ Bien hecho: apellido
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)  # ✅ Bien hecho: email único
    suscription_date: Mapped[str] = mapped_column(String(120), nullable=False)  # 🔧 Cambiar a tipo de dato adecuado
    password: Mapped[str] = mapped_column(String(120), nullable=False)  # ✅ Bien hecho: contraseña
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)  # ✅ Bien hecho: estado activo
    
    favorite_characters: Mapped[List["FavoriteCharacter"]] = relationship(back_populates="owner")  # ✅ Bien hecho: relación con personajes favoritos
    favorite_planets: Mapped[List["FavoritePlanet"]] = relationship(back_populates="owner")  # ✅ Bien hecho: relación con planetas favoritos

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
    id: Mapped[int] = mapped_column(primary_key=True)  # 🔧 Definido correctamente como primary_key
    name: Mapped[str] = mapped_column(String(120), nullable=False)  # ✅ Bien hecho: nombre
    birth_year: Mapped[int] = mapped_column(Integer, nullable=False)  # 🔧 Cambiar a String si es necesario
    gender: Mapped[str] = mapped_column(String(120), nullable=False)  # ✅ Bien hecho: género
    
    fav_chars: Mapped[List["FavoriteCharacter"]] = relationship(back_populates="character")  # ✅ Bien hecho: relación con favoritos

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "gender": self.gender
        }

class Planet(db.Model):
    __tablename__ = "planet"
    id: Mapped[int] = mapped_column(primary_key=True)  # 🔧 Definido correctamente como primary_key
    name: Mapped[str] = mapped_column(String(120), nullable=False)  # ✅ Bien hecho: nombre
    climate: Mapped[str] = mapped_column(String(120), nullable=False)  # ✅ Bien hecho: clima
    population: Mapped[int] = mapped_column(Integer, nullable=False)  # 🔧 Cambiar a String si es necesario
    
    fav_planets: Mapped[List["FavoritePlanet"]] = relationship(back_populates="planet")  # ✅ Bien hecho: relación con favoritos

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "population": self.population
        }

class FavoriteCharacter(db.Model):
    __tablename__ = "favorite_character"
    id: Mapped[int] = mapped_column(primary_key=True)  # 🔧 Definido correctamente como primary_key
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)  # ✅ Bien hecho: referencia a usuario
    character_id: Mapped[int] = mapped_column(ForeignKey("character.id"), nullable=False)  # ✅ Bien hecho: referencia a personaje
    
    owner: Mapped["User"] = relationship(back_populates="favorite_characters")  # ✅ Bien hecho: relación con usuario
    character: Mapped["Character"] = relationship(back_populates="fav_chars")  # ✅ Bien hecho: relación con personaje

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id
        }

class FavoritePlanet(db.Model):
    __tablename__ = "favorite_planet"
    id: Mapped[int] = mapped_column(primary_key=True)  # 🔧 Definido correctamente como primary_key
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)  # ✅ Bien hecho: referencia a usuario
    planet_id: Mapped[int] = mapped_column(ForeignKey("planet.id"), nullable=False)  # ✅ Bien hecho: referencia a planeta
    
    owner: Mapped["User"] = relationship(back_populates="favorite_planets")  # ✅ Bien hecho: relación con usuario
    planet: Mapped["Planet"] = relationship(back_populates="fav_planets")  # ✅ Bien hecho: relación con planeta

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id
        }