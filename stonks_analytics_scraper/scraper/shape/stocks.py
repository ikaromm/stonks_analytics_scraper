from stonks_analytics_scraper.utils.data_type import DataType

STOCK_SHAPE = [
    {
        "name": "name",
        "path": '//*[@id="header_action"]/div[1]/div[2]/h2',
        "type": DataType.STRING,
    },
    {
        "name": "cnpj",
        "path": '//*[@id="data_about"]/div[2]/div/div[1]/table/tbody/tr[2]/td[2]',
        "type": DataType.STRING,
    },
    {
        # Ano de criação
        "name": "foundation_date",
        "path": '//*[@id="data_about"]/div[2]/div/div[1]/table/tbody/tr[5]/td[2]',
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
        "name": "gross_debt",
        "path": '//*[@id="table-balance-results"]/tbody/tr[9]/td[2]/div[1]',
        "type": DataType.NUMERIC,
    },
    {
        # Lucro Bruto
        "name": "gross_profit",
        "path": '//*[@id="table-balance-results"]/tbody/tr[4]/td[2]/div[1]',
        "type": DataType.NUMERIC,
    },
    {
        # Margem Bruta
        "name": "gross_margin",
        "path": '//*[@id="table-balance-results"]/tbody/tr[11]/td[2]',
        "type": DataType.NUMERIC,
    },
    {
        # Divida liquida
        "name": "net_debt",
        "path": '//*[@id="table-balance-results"]/tbody/tr[10]/td[2]/div[1]',
        "type": DataType.NUMERIC,
    },
    {
        # Lucro liquido
        "name": "net_profit",
        "path": '//*[@id="table-balance-results"]/tbody/tr[5]/td[2]/div[1]',
        "type": DataType.NUMERIC,
    },
    {
        # Margem Líquida
        "name": "net_margin",
        "path": '//*[@id="table-balance-results"]/tbody/tr[13]/td[2]',
        "type": DataType.NUMERIC,
    },
    {
        # Margem Ebita
        "name": "ebitda_margin",
        "path": '//*//*[@id="table-balance-results"]/tbody/tr[12]/td[2]',
        "type": DataType.NUMERIC,
    },
    {
        # Custo
        "name": "cost",
        "path": '//*[@id="table-balance-results"]/tbody/tr[3]/td[2]/div[1]',
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
    {  
        # CAGR receita
        "name": "cagr_revenue",
        "path": '//*[@id="table-indicators"]/div[30]/div[1]/span',
        "type": DataType.NUMERIC,
    },
    {
        # CAGR lucro 
        "name": "cagr_profit",
        "path": '//*[@id="table-indicators"]/div[30]/div[1]/span',
        "type": DataType.NUMERIC,
    },
    {
        # divida bruta / patrimonio
        "name": "debt_to_equity",
        "path": '//*[@id="table-indicators"]/div[26]/div[1]/span',
        "type": DataType.NUMERIC,
    },
    {
        # passivos / ativos
        "name": "passives_to_actives",
        "path": '//*[@id="table-indicators"]/div[28]/div[1]/span',
        "type": DataType.NUMERIC,
    }
]
