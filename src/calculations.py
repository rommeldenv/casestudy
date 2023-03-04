import polars as pl
import datetime
# from functools import lru_cache

FILE_PATH = "./data/Stocks/"


class AllCalcualtions:
    """"""

    emptyDataFram = pl.DataFrame()

    # @lru_cache
    def calculate_individual_trading_volumn(stockFile):
        """"""

        plStockFile = pl.read_csv(
            FILE_PATH + str(stockFile),
            columns=["Date", "High", "Low", "Volume"],
            dtypes={
                "Date": pl.Date,
                "High": pl.Float64,
                "Low": pl.Float64,
                "Volume": pl.Float64,
            },
            encoding="Utf8",
        )

        plStockFile = plStockFile.with_columns(
            [
                pl.struct(["High", "Low", "Volume"])
                .apply(lambda x: ((x["High"] + x["Low"]) / 2) * x["Volume"])
                .alias(f"{str(stockFile)} Trading Volume")
            ]
        )

        tradingVolume = plStockFile.select(
            [pl.col("Date"), pl.col(f"{str(stockFile)} Trading Volume")]
        )

        return tradingVolume

    # @lru_cache
    def calculate_average_trading_volume(tradingVolume):
        """"""

        tradingVolume = tradingVolume.select(
            [
                pl.col("*"),
                tradingVolume.select(pl.col("*"))
                .mean(axis=1)
                .alias("Average Trading Volume"),
            ]
        )

        return tradingVolume

    def calculate_non_investment_grade(tradingVolume):
        """"""

        lastSixtyDays = tradingVolume.filter(
            pl.col("Date") >= datetime.date(2017, 10, 8)
        )

        return lastSixtyDays
