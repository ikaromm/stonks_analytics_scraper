from sqlalchemy import BigInteger, Double
from sqlalchemy.orm import DeclarativeBase, mapped_column, reconstructor
from sqlalchemy.schema import UniqueConstraint


class Base(DeclarativeBase):
    id = mapped_column(BigInteger, primary_key=True)
