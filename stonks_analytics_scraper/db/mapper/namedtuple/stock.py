from collections import namedtuple

StockTuple = namedtuple(
    "ParsedData",
    [
        "stock",
        "stock_price",
        "stock_statistics",
    ],
)
