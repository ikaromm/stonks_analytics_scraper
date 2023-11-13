from sqlalchemy import ForeignKey, Double, String
from sqlalchemy.orm import mapped_column, relationship, Mapped

from stonks_analytics_scraper.db.entity.base import Base

from stonks_analytics_scraper.db.entity.fiis.fii import Fii

class FiiStatistics(Base):
 
    __tablename__ = 'fii_statistics'

    fii_id = mapped_column(ForeignKey("fii.id"), nullable=False)
    
    dy12m = mapped_column(Double, nullable=True)
    pvp = mapped_column(Double, nullable=True)
    target_public = mapped_column(String(50), nullable=True)
    mandate = mapped_column(String(50), nullable=True)
    duration = mapped_column(String(50), nullable=True)
    amd_fee = mapped_column(String(50), nullable=True)
    dy5y = mapped_column(Double, nullable=True)
    vacancy = mapped_column(Double, nullable=True)
    asset_value = mapped_column(Double, nullable=True)
    last_income = mapped_column(Double, nullable=True)
    #properties = mapped_column(Double, nullable=True)





    fii: Mapped["Fii"] = relationship(back_populates="fii_statistics")