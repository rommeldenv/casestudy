import polars as pl
import plotly.express as px

END_DATE = "2017-11-10"


class CreateGraphics:
    """"""

    def create_graphics(averageTradingVolume):
        """"""

        averageTradingVolume = averageTradingVolume.sort("Date")

        fig = px.line(
            x=averageTradingVolume.select(pl.col("Date")).to_series(),
            y=averageTradingVolume.select(pl.col("Average Trading Volume")).to_series(),
        )

        return fig.write_html("./graph/graph.html")
