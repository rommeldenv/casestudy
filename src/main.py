from dataloader import DataLoader
from calculations import AllCalcualtions
from graphics import CreateGraphics


def main():
    sortedData = DataLoader.data_loader()

    averageTradingVolume = AllCalcualtions.calculate_average_trading_volume(sortedData)

    return CreateGraphics.create_graphics(averageTradingVolume=averageTradingVolume)


if __name__ == "__main__":
    main()
