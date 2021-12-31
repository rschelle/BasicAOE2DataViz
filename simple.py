import pandas as pd
import plotly.express as px

import streamlit as st

def getplayersgroupby(column):
    """
    A helper funtion that is used to help query aggregate statistics 
    about coolumns of the players dataframe that aren't to do with the 
    token or matchid
    """
    return playersdf.drop(labels = ["token","match","team"],axis = 1).groupby(column)


def read_players():
    """
    A helper function to read in the players csv data
    """
    df = pd.read_csv("data/match_players.csv")
    df["win"] = pd.Series(data = (df["winner"] == 1), dtype = "int")
    return df


def createplot1(total_games_by_civ,streamlit_width):
    """
    A helper function that returns a plotly barchart of the number of games 
    played by the top 10 most popular civilizations. If had time, would reorder
    the columns to be in decreasing order
    """
    games_by_civ_df = pd.DataFrame(total_games_by_civ)
    games_by_civ_df["civ"] = games_by_civ_df.index
    top10df = games_by_civ_df.loc[ games_by_civ_df["win"] > 130000] ##this is the top 10. I picked 130000 manually
    return px.bar(top10df, y = "win", labels = {"win": "Total Games Played"}, title = "Number of Games played by the 10 Most Popular Civs", width = 250*streamlit_width, height = 250*streamlit_width)

def createplot2(total_games_by_civ,streamlit_width):
    """
    A helper function that returns a plotly barchart of the number of games 
    played by the top 10 least popular civilizations. If had time, would reorder
    the columns to be in decreasing order
    """
    games_by_civ_df = pd.DataFrame(total_games_by_civ)
    games_by_civ_df["civ"] = games_by_civ_df.index
    top10df = games_by_civ_df.loc[ games_by_civ_df["win"] < 64500] ##This is the bottom 10. I picked 64500 manually
    return px.bar(top10df, y = "win", labels = {"win": "Total Games Played"}, title = "Number of Games played by the 10 Least Popular Civs", width = 250*streamlit_width, height = 250*streamlit_width)

def createplot5(total_games_by_color,streamlit_width):
    """
    A helper function that returns a plotly piechart of the number of games 
    played with each color
    """
    color_df = pd.DataFrame(total_games_by_color)
    color_df["color"] = color_df.index
    return px.pie(color_df, values = 'win', color = "color", color_discrete_map ={"Blue":"darkblue","Red":"red","Grey":"grey","Orange":"orange","Purple":"purple","Cyan":"cyan","Yellow":"yellow","Green":"green"}, title = "Percentage of Games Played With Each In-Game Color", width = 250*streamlit_width, height = 250*streamlit_width)

def createplot6(win_rate_by_color,streamlit_width):
    """
    A helper function that returns a plotly barchart of winrate of choosing
    each of the ingame colors . If had time, would reorder the columns to be in     
    decreasing order
    """
    color_df = pd.DataFrame(win_rate_by_color)
    color_df["color"] = color_df.index
    return px.bar(color_df, y = "win", color = "color", labels = {"win":"Winrate"}, color_discrete_map ={"Blue":"darkblue","Red":"red","Grey":"grey","Orange":"orange","Purple":"purple","Cyan":"cyan","Yellow":"yellow","Green":"green"}, title = "Winrate By Color", width = 250*streamlit_width, height = 250*streamlit_width)


playersdf = read_players()
win_rate_by_civ = getplayersgroupby("civ")["win"].mean()
total_games_by_civ = getplayersgroupby("civ")["win"].count()
total_wins_by_civ = getplayersgroupby("civ")["win"].sum()
win_rate_by_color = getplayersgroupby("color")["win"].mean()
total_games_by_color = getplayersgroupby("color")["win"].count()
total_wins_by_color = getplayersgroupby("color")["win"].sum()


st.write("""# Rudamentary Analysis of Age of Empires 2: Definitive Edition
            Here's the dataset: https://www.kaggle.com/kerneler/starter-age-of-empires-ii-de-match-e5e51473-6/data?select=match_players.csv""")
colwidth = 1.5
row1space1, row1col1, row1space2, row1col2, row1space3 = st.columns( (0.1,colwidth,0.1,colwidth,0.1) )

row1col1.title("An Extra Title for my first plot")
with row1col1:
    st.plotly_chart( createplot1(total_games_by_civ,colwidth))

row1col2.title("An Extra Title for my second plot")
with row1col2:
    st.plotly_chart( createplot2(total_games_by_civ,colwidth))
    
row2space1, row2col1, row2space2, row2col2, row1space3 = st.columns( (0.1,colwidth,0.1,colwidth,0.1) )

row2col1.title("An Extra Title for my 5th plot")
with row2col1:
    st.plotly_chart( createplot5(total_games_by_color,colwidth))

row2col2.title("An Extra Title for my 6th plot")
with row2col2:
    st.plotly_chart( createplot6(win_rate_by_color,colwidth))

###Takeaways:
    ##st.plotly_chart for plotly charts
        ###plotly width of 250 roughly fits in a streamlit width of 1
        ###BUT, the graph titles aren't affected by width. Would need to
        ###change title font size? How? idk?
    ##st.pyplot for matplotlib (have to worry about subplots?)
    ##plotly is nice except when it is not
    ##Trying to make the linux graphical desktop was the hardest part
    
# - Robert S

