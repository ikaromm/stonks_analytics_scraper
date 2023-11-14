from stonks_analytics_scraper.db.entity.base import Base

from sqlalchemy import BigInteger, DateTime, Double, ForeignKey, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class FiiPrice(Base):
    __tablename__ = "fii_price"
    fii_id = mapped_column(ForeignKey("fii.id"), nullable=False)
    timestamp = mapped_column(DateTime, nullable=False)
    value = mapped_column(Double, nullable=False)
    fii: Mapped["Fii"] = relationship(back_populates="fii_prices")
