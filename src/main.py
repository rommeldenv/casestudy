from dataloader import DataLoader
from calculations import AllCalcualtions
# from graphics import CreateGraphics


def main():
    sortedData = DataLoader.data_loader()

    tradingVolume = AllCalcualtions.calculate_average_trading_volume(sortedData)

    lastSixtyDays = AllCalcualtions.calculate_non_investment_grade(tradingVolume=tradingVolume) 

    return print(lastSixtyDays)


if __name__ == "__main__":
    main()
