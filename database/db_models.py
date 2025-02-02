from datetime import datetime

from sqlalchemy import (
    Column,
    Integer, String, ForeignKey, DateTime, )
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class Base:
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return str(self)


Base = declarative_base(cls=Base)  # type: ignore


class TimestampMixin:
    created_at = Column(DateTime, nullable=True, default=datetime.utcnow)


class BaseItem(TimestampMixin, Base):
    __tablename__ = "base-items"
    label_text = Column(String(4096), unique=False, nullable=False)
    part_number = Column(String(4096), unique=False, nullable=False)
    special_id = Column(Integer, unique=True)

    tokens = relationship('BaseItemsTokens', back_populates='baseitems')

    def __repr__(self) -> str:
        return "=" * 50 + str(self.label_text)


class AnalogItem(TimestampMixin, Base):
    __tablename__ = "analog-items"
    label_text = Column(String(4096), unique=False, nullable=False)
    part_number = Column(String(4096), unique=False, nullable=False)
    id_shop = Column(Integer, ForeignKey('shops.id'), unique=False, nullable=False)
    id_base_item = Column(Integer, ForeignKey('base-items.special_id'), unique=False, nullable=False)

    tokens = relationship('AnalogItemsTokens', back_populates='analogitems')

    def __repr__(self) -> str:
        return "=" * 50 + str(self.label_text)


class Shop(TimestampMixin, Base):
    __tablename__ = "shops"
    shop_name = Column(String(4096), unique=True, nullable=True)


class BaseItemsTokens(TimestampMixin, Base):
    __tablename__ = "base-tokens"
    token = Column(String(4096), unique=False, nullable=False)
    id_item = Column(Integer, ForeignKey('base-items.id'), unique=False, nullable=False)
    baseitems = relationship('BaseItem', back_populates='tokens', uselist=False)

    def __repr__(self) -> str:
        return "-" * 50 + str(self.token)


class AnalogItemsTokens(TimestampMixin, Base):
    __tablename__ = "analog-tokens"
    token = Column(String(4096), unique=False, nullable=False)
    id_item = Column(Integer, ForeignKey('analog-items.id'), unique=False, nullable=False)
    analogitems = relationship('AnalogItem', back_populates='tokens', uselist=False)

    def __repr__(self) -> str:
        return "-" * 50 + str(self.token)