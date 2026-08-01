import numpy as np
import pandas as pd
import plotly.express as px


def main():
    dates = pd.date_range(start="2026-07-01", periods=30, freq="D")

    rng = np.random.default_rng(42)
    df = pd.DataFrame(
        {
            "Date": dates,
            "US 10Y Yield": 4.2 + rng.normal(0, 0.05, 30),
            "Implied Volatility": 18.5 + rng.normal(0, 0.8, 30),
        }
    )

    df_long = df.melt(id_vars="Date", var_name="Metric", value_name="Value")

    fig = px.line(
        df_long,
        x="Date",
        y="Value",
        color="Metric",
        title="Capstone Rates Monitor: US 10Y Yield vs Implied Volatility",
        labels={"Date": "Trading Date", "Value": "Level (%)", "Metric": "Series"},
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0d1117",
        plot_bgcolor="#161b22",
        font=dict(family="Arial, sans-serif", color="#e6edf3"),
        title=dict(x=0.5, xanchor="center", font=dict(size=20)),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            bgcolor="rgba(0,0,0,0)",
        ),
        hovermode="x unified",
        xaxis=dict(showgrid=True, gridcolor="#30363d", title="Trading Date"),
        yaxis=dict(showgrid=True, gridcolor="#30363d", title="Level (%)"),
    )

    fig.update_traces(line=dict(width=2.5))
    fig.write_html("rates_chart.html", auto_open=True)


if __name__ == "__main__":
    main()
