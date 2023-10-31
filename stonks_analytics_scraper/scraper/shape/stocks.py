from stonks_analytics_scraper.utils.data_type import DataType

STOCK_SHAPE = [
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
        # net revenue = receita liquida
        "name": "net_revenue",
        "path": '//*[@id="table-balance-results"]/tbody/tr[2]/td[2]/div[1]',
        "type": DataType.NUMERIC,
    },
    {
        # EBITA
        "name": "ebitda",
        "path": '//*[@id="table-balance-results"]/tbody/tr[7]/td[2]/div[1]',
        "type": DataType.NUMERIC,
    },
    {
        # EBIT
        "name": "ebit",
        "path": '//*[@id="table-balance-results"]/tbody/tr[6]/td[2]/div[1]',
        "type": DataType.NUMERIC,
    },
    {
        # Imposto
        "name": "tax",
        "path": '//*[@id="table-balance-results"]/tbody/tr[8]/td[2]/div[1]',
        "type": DataType.NUMERIC,
    },
    {
        # Divida Bruta
        "name": "gross debt",
        "path": '//*[@id="table-balance-results"]/tbody/tr[9]/td[2]/div[1]',
        "type": DataType.NUMERIC,
    },
    {
        # Divida liquida
        "name": "net debt",
        "path": '//*[@id="table-balance-results"]/tbody/tr[10]/td[2]/div[1]',
        "type": DataType.NUMERIC,
    },
    {
        # Lucro liquido
        "name": "net revenue",
        "path": '//*[@id="table-balance-results"]/tbody/tr[5]/td[2]/div[1]',
        "type": DataType.NUMERIC,
    },
    {
        # Lucro Bruto
        "name": "gross profit",
        "path": '//*[@id="table-balance-results"]/tbody/tr[4]/td[2]/div[1]',
        "type": DataType.NUMERIC,
    },
    {
        # Custo
        "name": "cost",
        "path": '//*[@id="table-balance-results"]/tbody/tr[3]/td[2]/div[1]',
        "type": DataType.NUMERIC,
    },
    {
        # Margem Bruta
        "name": "gross margin",
        "path": '//*[@id="table-balance-results"]/tbody/tr[11]/td[2]',
        "type": DataType.NUMERIC,
    },
    {
        # Margem Ebita
        "name": "ebitda margin",
        "path": '//*//*[@id="table-balance-results"]/tbody/tr[12]/td[2]',
        "type": DataType.NUMERIC,
    },
    {
        # Margem Líquida
        "name": "net margin",
        "path": '//*[@id="table-balance-results"]/tbody/tr[13]/td[2]',
        "type": DataType.NUMERIC,
    },
    {
        # ROE
        "name": "roe",
        "path": '//*[@id="table-balance-results"]/tbody/tr[14]/td[2]',
        "type": DataType.NUMERIC,
    },
    {
        # ROA
        "name": "roa",
        "path": '//*[@id="table-indicators"]/div[22]/div[1]/span',
        "type": DataType.NUMERIC,
    },
    {
        # ROIC
        "name": "roic",
        "path": '//*[@id="table-balance-results"]/tbody/tr[15]/td[2]',
        "type": DataType.NUMERIC,
    },
    {
        # DY
        "name": "dy",
        "path": '//*[@id="cards-ticker"]/div[5]/div[2]/span',
        "type": DataType.NUMERIC,
    },
    {
        # P/VP
        "name": "pvp",
        "path": '//*[@id="cards-ticker"]/div[4]/div[2]/span',
        "type": DataType.NUMERIC,
    },
    {
        # PL
        "name": "pl",
        "path": '//*[@id="cards-ticker"]/div[3]/div[2]/span',
        "type": DataType.NUMERIC,
    },
    {
        # CNPJ
        "name": "cnpj",
        "path": '//*[@id="data_about"]/div[2]/div/div[1]/table/tbody/tr[2]/td[2]',
        "type": DataType.STRING,
    },
    {
        # Ano de criação
        "name": "year",
        "path": '//*[@id="data_about"]/div[2]/div/div[1]/table/tbody/tr[5]/td[2]',
        "type": DataType.DATE,
    },
    {
        # VPA
        "name": "vpa",
        "path": '//*[@id="table-indicators"]/div[17]/div[1]/span',
        "type": DataType.NUMERIC,
    },
    {
        # LPA
        "name": "lpa",
        "path": '//*[@id="table-indicators"]/div[18]/div[1]/span',
        "type": DataType.NUMERIC,
    },
    {
        # Setor
        "name": "sector",
        "path": '//*[@id="table-indicators-company"]/div[14]/a/span[2]',
        "type": DataType.STRING,
    },
    {
        # Segmento
        "name": "segment",
        "path": '//*[@id="table-indicators-company"]/div[15]/a/span[2]',
        "type": DataType.STRING,
    },
    {
        # Tag Along
        "name": "tag_along",
        "path": '//*[@id="table-indicators-company"]/div[12]/span[2]',
        "type": DataType.NUMERIC,
    },
    {
        # Free Float
        "name": "free_float",
        "path": '//*[@id="table-indicators-company"]/div[11]/span[2]',
        "type": DataType.NUMERIC,
    },
]
