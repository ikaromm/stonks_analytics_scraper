from typing import List

from stonks_analytics_scraper.db.entity.base import Base
from sqlalchemy import String, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.schema import UniqueConstraint, Index

from stonks_analytics_scraper.db.entity.fiis.fii_price import FiiPrice

class Fii(Base):
    __tablename__ = 'fii'
    __table_args__ = (
        UniqueConstraint('fii_name', 'segment', 'ticker', name='unique_fii'),
        Index('idx_fii_name', 'fii_name'),
        Index('idx_fii_segment', 'segment'),
        Index('idx_fii_ticker', 'ticker'),
    )



    fii_name = mapped_column(String(50), nullable=False)    
    ticker = mapped_column(String(10), nullable=False)
    segment = mapped_column(String(18), nullable=True)
    fii_type = mapped_column(Date, nullable=True)
    management = mapped_column(String(50), nullable=True)
    target_public = mapped_column(String(50), nullable=True)



    fii_prices: Mapped[List["FiiPrice"]] = relationship(
        back_populates="fii", cascade="all, delete-orphan"
    )
    fii_statistics: Mapped[List["FiiStatistics"]] = relationship(
        back_populates="fii", cascade="all, delete-orphan"
    )