from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

# Inicializamos SQLAlchemy para manejar la base de datos
# ✅ Buen uso de SQLAlchemy para la gestión de modelos

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)  # 🔧 Se puede especificar el tipo de columna
    user_name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)  # 📝 Cambié 'username' a 'user_name' para mayor claridad
    name: Mapped[str] = mapped_column(String(120), nullable=False)  # ✅ Buen uso de nombres descriptivos
    last_name: Mapped[str] = mapped_column(String(120), nullable=False)  # 📝 Añadido 'last_name' para mayor claridad
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    suscription_date: Mapped[str] = mapped_column(String(120), nullable=False)  # 📝 'suscription_date' debería ser 'subscription_date'
    password: Mapped[str] = mapped_column(String(120), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)  # ✅ Buen uso de Boolean para estado
    
    # Relaciones con favoritos
    favorite_characters: Mapped[List["FavoriteCharacter"]] = relationship(back_populates="owner")
    favorite_planets: Mapped[List["FavoritePlanet"]] = relationship(back_populates="owner")

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
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    birth_year: Mapped[int] = mapped_column(Integer, nullable=False)  # 📝 Cambié a Integer para representar el año
    gender: Mapped[str] = mapped_column(String(120), nullable=False)
    
    fav_chars: Mapped[List["FavoriteCharacter"]] = relationship(back_populates="character")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "gender": self.gender
        }

class Planet(db.Model):
    __tablename__ = "planet"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    climate: Mapped[str] = mapped_column(String(120), nullable=False)
    population: Mapped[int] = mapped_column(Integer, nullable=False)  # 📝 Cambié a Integer para representar la población
    
    fav_planets: Mapped[List["FavoritePlanet"]] = relationship(back_populates="planet")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "population": self.population
        }

class FavoriteCharacter(db.Model):
    __tablename__ = "favorite_character"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    character_id: Mapped[int] = mapped_column(ForeignKey("character.id"), nullable=False)
    
    owner: Mapped["User"] = relationship(back_populates="favorite_characters")
    character: Mapped["Character"] = relationship(back_populates="fav_chars")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id
        }

class FavoritePlanet(db.Model):
    __tablename__ = "favorite_planet"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    planet_id: Mapped[int] = mapped_column(ForeignKey("planet.id"), nullable=False)
    
    owner: Mapped["User"] = relationship(back_populates="favorite_planets")
    planet: Mapped["Planet"] = relationship(back_populates="fav_planets")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id
        }