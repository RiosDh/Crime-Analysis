#import packages

#from dbm import _Database
from typing import Container
from xmlrpc.client import DateTime
import altair as alt
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from datetime import datetime as dt, timedelta, timezone, date
import calendar
from dateutil.relativedelta import relativedelta
from PIL import Image

from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, ColumnsAutoSizeMode

import os
#from dotenv import load_dotenv
#load_dotenv()

#Page Setting

st.set_page_config(
    page_title="TOEX Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
    ) 


df = pd.read_csv('full.csv') 
maps = pd.read_csv('maps.csv')
maps = maps.dropna()

gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
gb.configure_side_bar() #Add a sidebar

gridOptions = gb.build()


# Main Content

c = st.container()

with c:
    st.image(Image.open('toex_logo.png'), use_column_width=False, width=400)

tab1, tab2 = st.tabs(["Dashboard", "Geo Analysis"])

#Row A
with tab1:
     a1, a2, a3 = st.columns(3)
     a1.metric("Total Number of Offences", "39,324,728") #selector
     a2.metric("Average crimes per year", "4,915,591") #selector
     a3.metric("Number of crimes this year", "x", "4%")  #slider

con2 = st.container()

with con2:
    
    # st.title('Clients')
        grid_response = AgGrid(
            df,
            gridOptions=gridOptions,
            fit_columns_on_grid_load=True,
            height=1000000, 
            width="50%",
            reload_data=True,
            columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS
        )

with tab2:
    con3 = st.container()

    with con3:
        
        locations = maps[["lon","lat"]]

        st.map(locations, use_container_width=True)
