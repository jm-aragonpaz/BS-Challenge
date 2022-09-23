import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def main_graph(df: pd.DataFrame):
    fig = px.scatter(df,
                    x='tvl',
                    y='apy',
                    color="class",
                    hover_data=["chain","protocol"],
                    labels={
                        "class":"Pool Class",
                        "tvl": "Total Volume Locked",
                        "apy": "Annual Percentage Yield",
                        "chain": "Blockchain",
                        "protocol":"Protocol"
                    },
                    color_discrete_sequence=px.colors.qualitative.T10,
                    log_x=True,
                    log_y=True
                    )

    fig.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })

    fig.update_traces(marker=dict(size=13,
                                line=dict(width=0.6,
                                            color='White')),
                    selector=dict(mode='markers'))

    fig.update_layout(
                xaxis=dict(title_text="(-) «──────────── TVL ────────────» (+)", showgrid=False, showticklabels=False, rangemode='tozero', mirror=True, linewidth=2),
                yaxis=dict(title_text="(-) «──────── APY ────────» (+)", showgrid=False, showticklabels=False, rangemode='tozero', mirror=True, linewidth=2),
    )
    # fig.update_xaxes(
    #     range=[-100000,120000000],
    #     constrain="domain",
    # )
    # fig.update_yaxes(
    #     range=[-0.05,110]
    # )
    fig.update_layout(width=1000, height=500)

    return fig

def lp_insights(df_lp: pd.DataFrame)-> go.Figure:
    
    fig = go.Figure()
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
        go.Bar(
            x=df_lp["date"],
            y=df_lp["tvl"],
            name="TVL",
        ),
        secondary_y=True,
    )
    fig.update_traces(
        marker_color="rgb(252,149,79)",
        marker_line_color="rgb(20,76,157)",
        marker_line_width=0.5,
        opacity=0.4,
    )
    fig.add_trace(
        go.Scatter(
            x=df_lp["date"],
            y=df_lp["base"],
            name="Base APY",
        ),
    secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(
            x=df_lp["date"],
            y=df_lp["reward"],
            name="Reward Token",
        ),
    secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(
            x=df_lp["date"],
            y=df_lp["apy"],
            name="Total APY",
        ),
    secondary_y=False,
    )
    fig.update_layout(
        legend=dict(
            orientation="h",
            y=-0.1,
            x=0.25,
        )
    )
    fig.update_yaxes(showgrid=False, tickformat='0%',title_text="Base APY & Reward Token", secondary_y=False)
    fig.update_yaxes(showgrid=False, title_text="TVL", secondary_y=True)
    fig.update_layout(width=1000, height=500, plot_bgcolor="rgb(255,255,255)")

    return fig

def reward_token_insights(reward_token_timeseries)-> go.Figure:

    fig = go.Figure()
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
        go.Bar(
            x=reward_token_timeseries['date'],
            y=reward_token_timeseries['market_cap'],
            name="Market Cap",
        ),
        secondary_y=True,
    )
    fig.update_traces(
        marker_color="rgb(252,149,79)",
        marker_line_color="rgb(20,76,157)",
        marker_line_width=0.5,
        opacity=0.4,
    )
    fig.add_trace(
        go.Scatter(
            x=reward_token_timeseries['date'],
            y=reward_token_timeseries['price'],
            name="Price",
        ),
    secondary_y=False,
    )
    fig.update_layout(
        legend=dict(
            orientation="h",
            y=-0.1,
            x=0.25,
        )
    )
    fig.update_yaxes(showgrid=False, title_text="Price", secondary_y=False)
    fig.update_yaxes(showgrid=False, title_text="Market Cap", secondary_y=True)
    fig.update_layout(width=1000, height=500, plot_bgcolor="rgb(255,255,255)")
    return fig

def pie(df: pd.DataFrame)-> go.Figure:
    clases=df['class'].value_counts()
    values=[clases['A'],clases['B'],clases['C']]
    labels=['Class A','Class B','Class C']
    fig=go.Figure(data=[go.Pie(labels=labels,values=values,hole=.3)])
    fig.update_layout(
    title_text="Stable Coin Pools distribution"
    )
    return fig