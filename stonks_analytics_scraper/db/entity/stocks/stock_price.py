from stonks_analytics_scraper.db.entity.base import Base
from sqlalchemy import Integer, Double, BigInteger, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class StockPrice(Base):
    __tablename__ = 'stock_price'

    stock_id = mapped_column(BigInteger, nullable=False)
    timestamp = mapped_column(DateTime, nullable=False)
    value = mapped_column(Double, nullable=False)

    stock: Mapped["Stock"] = relationship(back_populates="stock_prices")