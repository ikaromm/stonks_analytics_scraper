from stonks_analytics_scraper.db.entity.base import Base
from stonks_analytics_scraper.db.entity.stocks.stock_price import StockPrice
from stonks_analytics_scraper.db.entity.stocks.stock_statistics import (
    StockStatistics,
)

from sqlalchemy import Date, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.schema import Index, UniqueConstraint

from typing import List


class Stock(Base):
    __tablename__ = "stock"

    __table_args__ = (
        UniqueConstraint("name", "cnpj", "ticker", name="unique_stock"),
        Index("idx_stock_name", "name"),
        Index("idx_stock_cnpj", "cnpj"),
        Index("idx_stock_ticker", "ticker"),
    )

    name = mapped_column(String(50), nullable=False)
    cnpj = mapped_column(String(18), nullable=False)
    ticker = mapped_column(String(10), nullable=False)
    foundation_year = mapped_column(Integer, nullable=True)
    sector = mapped_column(String(50), nullable=True)
    segment = mapped_column(String(50), nullable=True)

    stock_prices: Mapped[List["StockPrice"]] = relationship(
        back_populates="stock", cascade="all, delete-orphan"
    )

    stock_statistics: Mapped[List["StockStatistics"]] = relationship(
        back_populates="stock", cascade="all, delete-orphan"
    )
