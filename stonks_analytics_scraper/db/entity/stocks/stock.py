from stonks_analytics_scraper.db.entity.base import Base
from sqlalchemy import String, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Stock(Base):
    __tablename__ = 'stock'

    name = mapped_column(String(50), nullable=False)
    cnpj = mapped_column(String(18), nullable=False)
    ticker = mapped_column(String(10), nullable=False)
    foundation_date = mapped_column(Date, nullable=True)
    sector = mapped_column(String(50), nullable=True)
    subsector = mapped_column(String(50), nullable=True)

    stock_prices: Mapped[List["StockPrice"]] = relationship(
        back_populates="stock", cascade="all, delete-orphan"
    )

    stock_statistics: Mapped[List["StockStatistics"]] = relationship(
        back_populates="stock", cascade="all, delete-orphan"
    )