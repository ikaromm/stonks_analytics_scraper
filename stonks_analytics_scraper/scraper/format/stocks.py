from stonks_analytics_scraper.utils.data_type import DataType

STOCK_FORMAT = [
    {
        "name": "company_name",
        "path": '//*[@id="header_action"]/div[1]/div[2]/h2',
        "type": DataType.STRING,
    },
    {
        "name": "cnpj",
        "path": '//*[@id="data_about"]/div[2]/div/div[1]/table/tbody/tr[2]/td[2]',
        "type": DataType.STRING,
    },
    {
        "name": "net_revenue",
        "path": '//*[@id="table-balance-results"]/tbody/tr[2]/td[2]/div[1]',
        "type": DataType.NUMERIC,
    }
]
