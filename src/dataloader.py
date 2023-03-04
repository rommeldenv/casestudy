import os
from calculations import AllCalcualtions

FILE_PATH = "./data/Stocks/"


class DataLoader:
    """ """

    def data_loader():
        """ """

        notEmptyFiles = DataLoader.file_checker()

        i = 0

        for file in notEmptyFiles:
            individualTradingVolume = (
                AllCalcualtions.calculate_individual_trading_volumn(stockFile=file)
            )

            individualTradingVolume = individualTradingVolume.sort("Date")

            if i == 0:
                dfIndividualTradingVolume = individualTradingVolume
            else:
                dfIndividualTradingVolume = dfIndividualTradingVolume.join(
                    individualTradingVolume, on="Date", how="outer"
                )

            i += 1

        sortedDataFrame = dfIndividualTradingVolume.sort("Date")

        return sortedDataFrame

    def file_checker():
        """ """

        notEmptyFiles = []
        emptyFiles = []

        for file in os.listdir(FILE_PATH):
            if os.path.getsize(FILE_PATH + file) > 0:
                notEmptyFiles.append(file)
            else:
                emptyFiles.append(file)

        return notEmptyFiles
