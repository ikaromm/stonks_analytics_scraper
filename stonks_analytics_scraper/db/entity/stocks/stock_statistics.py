from stonks_analytics_scraper.db.entity.base import Base


class StockStatistics(Base):
    __tablename__ = 'stock_statistics'

    stock_id = mapped_column(BigInteger, nullable=False)

    net_revenue = mapped_column(Double, nullable=True)
    ebitda = mapped_column(Double, nullable=True)
    ebit = mapped_column(Double, nullable=True)
    tax = mapped_column(Double, nullable=True)
    gross_debt = mapped_column(Double, nullable=True)
    gross_profit = mapped_column(Double, nullable=True)
    gross_margin = mapped_column(Double, nullable=True)
    net_debt = mapped_column(Double, nullable=True)
    net_profit = mapped_column(Double, nullable=True)
    net_margin = mapped_column(Double, nullable=True)
    cost = mapped_column(Double, nullable=True)
    roe = mapped_column(Double, nullable=True)
    roa = mapped_column(Double, nullable=True)
    roic = mapped_column(Double, nullable=True)
    dy = mapped_column(Double, nullable=True)
    pvp = mapped_column(Double, nullable=True)
    pl = mapped_column(Double, nullable=True)
    vpa = mapped_column(Double, nullable=True)
    lpa = mapped_column(Double, nullable=True)
    tag_along = mapped_column(Double, nullable=True)
    free_float = mapped_column(Double, nullable=True)
    cagr_revenue = mapped_column(Double, nullable=True)
    cagr_profit = mapped_column(Double, nullable=True)
    debt_to_equity = mapped_column(Double, nullable=True)
    passives_to_actives = mapped_column(Double, nullable=True)

    stock: Mapped["Stock"] = relationship(back_populates="stock_statistics")