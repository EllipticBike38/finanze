from typing import Optional
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float,  Table
from sqlalchemy.orm import relationship
from enum import Enum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

tags_transactions = Table('tags_transactions', Base.metadata,
                          Column('tag_id', Integer, ForeignKey('tags.id')),
                          Column('transaction_id', Integer,
                                 ForeignKey('transazione.id'))
                          )


class Transazione(Base):
    __tablename__ = 'transazione'

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime, nullable=False)
    costo = Column(Float, nullable=False)
    nome = Column(String, nullable=False)
    descrizione = Column(String, nullable=False)

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship("User", back_populates="transazioni")

    abbonamento_id = Column(Integer, ForeignKey(
        'abbonamento.id'), nullable=True)
    abbonamento = relationship("Abbonamento", back_populates="transazioni")

    tags = relationship("Tag", secondary=tags_transactions,
                        back_populates="transactions")

    class Config:
        orm_mode = True
    ...


class Abbonamento(Base):
    __tablename__ = 'abbonamento'

    id = Column(Integer, primary_key=True, autoincrement=True)
    giorno = Column(Integer, nullable=False)
    mese = Column(Integer, nullable=False)
    inizio = Column(DateTime, nullable=False)
    fine = Column(DateTime, nullable=False)
    costo = Column(Float, nullable=False)
    nome = Column(String, nullable=False)
    descrizione = Column(String, nullable=False)

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship("User", back_populates="abbonamenti")

    transazioni = relationship("Transazione", back_populates="abbonamento")

    class Config:
        orm_mode = True


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    cognome = Column(String, nullable=False)
    nickname = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

    transazioni = relationship(
        "Transazione", back_populates="user",  cascade='delete')
    abbonamenti = relationship(
        "Abbonamento", back_populates="user",  cascade='delete')

    class Config:
        orm_mode = True


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    transactions = relationship(
        "Transazione", secondary=tags_transactions, back_populates="tags")

    class Config:
        orm_mode = True
