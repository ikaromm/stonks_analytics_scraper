from __future__ import annotations

from stonks_analytics_scraper.db.entity.base import Base
from stonks_analytics_scraper.db.entity.stocks import (
    Stock,
    StockPrice,
    StockStatistics,
)

from sqlalchemy import select, text
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session


class StockRepository:
    def __init__(self, engine: Engine):
        self.engine = engine

        Base.metadata.create_all(engine)

    def save_stock(self, stock: Stock):
        with Session(self.engine) as session:
            session.add(stock)
            session.commit()

            session.refresh(stock)

    def update_stock(self, stock: Stock):
        with Session(self.engine) as session:
            session.merge(stock)
            session.commit()

    def save_stock_price(self, stock_price: StockPrice):
        with Session(self.engine) as session:
            session.add(stock_price)
            session.commit()

    def save_stock_statistics(self, stock_statistics: StockStatistics):
        with Session(self.engine) as session:
            session.add(stock_statistics)
            session.commit()

    def get_stock(self, stock_ticker: str) -> Stock | None:
        with Session(self.engine) as session:
            return session.query(Stock).filter(Stock.ticker == stock_ticker).first()

    def get_stock_native(self, stock_ticker: str) -> Stock | None:
        query = text(
            """
                SELECT * FROM public.stock s WHERE s.ticker = :stock_ticker
            """
        ).params({"stock_ticker": stock_ticker})

        with Session(self.engine) as session:
            return session.scalars(select(Stock).from_statement(query)).first()

    def get_stock_price(self, stock_ticker: str) -> StockPrice:
        pass

    def get_stock_statistics(
        self, stock_ticker: str, month: int = None, year: int = None
    ) -> StockStatistics | None:
        with Session(self.engine) as session:
            query = (
                session.query(StockStatistics)
                .join(Stock)
                .filter(Stock.ticker == stock_ticker)
            )
            if month:
                query = query.filter(StockStatistics.month == month)
            if year:
                query = query.filter(StockStatistics.year == year)

            return query.first()

    def get_stock_statistics_native(
        self, stock_ticker: str, month: int = None, year: int = None
    ) -> StockStatistics | None:
        params = {"stock_ticker": stock_ticker}
        if month:
            params["month"] = month
        if year:
            params["year"] = year

        query = text(
            f"""
                SELECT ss.* 
                  FROM public.stock_statistics ss 
                  join public.stock s on ss.stock_id = s.id
                 WHERE s.ticker = :stock_ticker
                 {'and ss.month = :month' if month else ''}
                 {'and ss.year = :year' if year else ''}
            """
        ).params(params)

        with Session(self.engine) as session:
            return session.scalars(
                select(StockStatistics).from_statement(query)
            ).first()
