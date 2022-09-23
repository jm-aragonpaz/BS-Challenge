import streamlit as st
import pandas as pd
import json
import plotly as pl
from plot import main_graph, lp_insights, reward_token_insights, pie


st.set_page_config(layout="wide",
                    page_title="Blueswan DS challenge",
                    page_icon="🧊",
)
st.title("Blueswan DS challenge")

st.header(
    "An allocation strategy for maximize the Projected Weighted APY."
)

df=pd.read_csv('pools.csv')



df['APY']=df['apy']*100

st.header(
    "Stable Coin Pools available on Coindix Dataset"
)
st.markdown(
    "Pools have been clasified according to the following rules:\n"
    "- Pools A: Has a TVL of more than \$50MUSD\n"
    "- Pools B: Has a TVL of less than \$50MUSD but more of $10MUSD\n"
    "- Pools C: Has a TVL of less than \$10MUSD"
)
st.subheader("Stable Coin Pools distribution by Class")
st.plotly_chart(
    pie(df)
)
st.subheader("Stable Coin Pools TVL vs. APY")
st.plotly_chart(
    main_graph(df)
)