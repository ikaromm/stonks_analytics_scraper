from stonks_analytics_scraper.utils.data_type import DataType

FII_SHAPE = [
    {
        "name": "fii_name",
        "path": '//*[@id="header_action"]/div[1]/div[2]/h1',
        "type": DataType.STRING,
    },
    {
        "name": "dy12m",
        "path": '//*[@id="cards-ticker"]/div[2]/div[2]/div/span',
        "type": DataType.NUMERIC,
    },
    {
        "name": "pvp",
        "path": '//*[@id="cards-ticker"]/div[3]/div[2]/span',
        "type": DataType.NUMERIC,
    },
    {
        "name": "target_public",
        "path": '//*[@id="table-indicators"]/div[3]/div[2]/div/span',
        "type": DataType.STRING,
    },
    {
        "name": "mandate",
        "path": '//*[@id="table-indicators"]/div[4]/div[2]/div/span',
        "type": DataType.STRING,
    },
    {
        "name": "segment",
        "path": '//*[@id="table-indicators"]/div[5]/div[2]/div/span',
        "type": DataType.STRING,
    },
    {
        "name": "fii_type",
        "path": '//*[@id="table-indicators"]/div[6]/div[2]/div/span',
        "type": DataType.STRING,
    },
    {
        "name": "duration",
        "path": '//*[@id="table-indicators"]/div[7]/div[2]/div/span',
        "type": DataType.STRING,
    },
    {
        "name": "management",
        "path": '//*[@id="table-indicators"]/div[8]/div[2]/div/span',
        "type": DataType.STRING,
    },
    {
        "name": "amd_fee",
        "path": '//*[@id="table-indicators"]/div[9]/div[2]/div/span',
        "type": DataType.STRING,
    },
    {
        "name": "dy5y",
        "path": '//*[@id="dividends-section"]/div[1]/div[1]/span[2]/text()',
        "type": DataType.NUMERIC,
    },
    {
        "name": "vacancy",
        "path": '//*[@id="table-indicators"]/div[9]/div[2]/div/span',
        "type": DataType.NUMERIC,
    },
    {
        "name": "asset_value",
        "path": '//*[@id="table-indicators"]/div[14]/div[2]/div/span',
        "type": DataType.NUMERIC,
    },
    {
        "name": "last_income",
        "path": '//*[@id="table-indicators"]/div[15]/div[2]/div/span',
        "type": DataType.NUMERIC,
    },
    # {
    #     "name": "properties",
    #     "path":
    #             try:
    #                 num_rows = 15
    #                 imv_values = []
    #                 for i in range(1, num_rows + 1):
    #                     xpath = (
    #                         f'//*[@id="properties-index-table"]/tbody/tr[{i}]/td[2]/span'
    #                     )
    #                     imv = extract_numeric_from_xpath(xpath, browser)
    #                     imv_values.append(imv)
    #             except:
    #                 imv_values = sum(imv_values)
    #     "type": DataType.NUMERIC
    # }
]
