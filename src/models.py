from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

# Inicializamos la base de datos con SQLAlchemy
# ✅ Buen uso de SQLAlchemy para manejar la base de datos

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)  # 🔧 Se puede especificar el tipo de columna
    user_name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)  # 📝 Cambié el nombre a user_name para mayor claridad
    name: Mapped[str] = mapped_column(String(120), nullable=False)  # ✅ Buen uso de atributos
    last_name: Mapped[str] = mapped_column(String(120), nullable=False)  # 📝 Es bueno tener un campo para el apellido
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)  # ✅ Buen uso de validaciones
    suscription_date: Mapped[str] = mapped_column(String(120), nullable=False)  # 🔧 Considera usar DateTime para fechas
    password: Mapped[str] = mapped_column(String(120), nullable=False)  # ✅ Buen manejo de contraseñas
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)  # ✅ Buen uso de booleanos
    
    favorite_characters: Mapped[List["FavoriteCharacter"]] = relationship(back_populates="owner")  # ✅ Buen uso de relaciones
    favorite_planets: Mapped[List["FavoritePlanet"]] = relationship(back_populates="owner")  # ✅ Buen uso de relaciones

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
    id: Mapped[int] = mapped_column(primary_key=True)  # ✅ Buen uso de primary_key
    name: Mapped[str] = mapped_column(String(120), nullable=False)  # ✅ Buen uso de atributos
    birth_year: Mapped[int] = mapped_column(Integer, nullable=False)  # 🔧 Considera usar String si el año puede ser no numérico
    gender: Mapped[str] = mapped_column(String(120), nullable=False)  # ✅ Buen uso de atributos
    
    fav_chars: Mapped[List["FavoriteCharacter"]] = relationship(back_populates="character")  # ✅ Buen uso de relaciones

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "gender": self.gender
        }

class Planet(db.Model):
    __tablename__ = "planet"
    id: Mapped[int] = mapped_column(primary_key=True)  # ✅ Buen uso de primary_key
    name: Mapped[str] = mapped_column(String(120), nullable=False)  # ✅ Buen uso de atributos
    climate: Mapped[str] = mapped_column(String(120), nullable=False)  # ✅ Buen uso de atributos
    population: Mapped[int] = mapped_column(Integer, nullable=False)  # ✅ Buen uso de atributos
    
    fav_planets: Mapped[List["FavoritePlanet"]] = relationship(back_populates="planet")  # ✅ Buen uso de relaciones

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "population": self.population
        }

class FavoriteCharacter(db.Model):
    __tablename__ = "favorite_character"
    id: Mapped[int] = mapped_column(primary_key=True)  # ✅ Buen uso de primary_key
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)  # ✅ Buen uso de claves foráneas
    character_id: Mapped[int] = mapped_column(ForeignKey("character.id"), nullable=False)  # ✅ Buen uso de claves foráneas
    
    owner: Mapped["User"] = relationship(back_populates="favorite_characters")  # ✅ Buen uso de relaciones
    character: Mapped["Character"] = relationship(back_populates="fav_chars")  # ✅ Buen uso de relaciones

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id
        }

class FavoritePlanet(db.Model):
    __tablename__ = "favorite_planet"
    id: Mapped[int] = mapped_column(primary_key=True)  # ✅ Buen uso de primary_key
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)  # ✅ Buen uso de claves foráneas
    planet_id: Mapped[int] = mapped_column(ForeignKey("planet.id"), nullable=False)  # ✅ Buen uso de claves foráneas
    
    owner: Mapped["User"] = relationship(back_populates="favorite_planets")  # ✅ Buen uso de relaciones
    planet: Mapped["Planet"] = relationship(back_populates="fav_planets")  # ✅ Buen uso de relaciones

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id
        }