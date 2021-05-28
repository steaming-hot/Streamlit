
# -*- coding: utf-8 -*-
"""
Created on Thu May  2021
@author: Alex https://github.com/alexcasella
"""
import streamlit as st

def page_introduction():
  
    
    # Space so that 'About' box-text is lower
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    
    st.markdown("<h2 style='text-align: center;'> Welcome To </h2>", 
                unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'> The Steaming Hot App</h1>", 
                unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: left;'> By Alex Casella, Eduardo Medina, Joseph Leung, Kanishk Jain, Ling Zhou and Rohit Sajita.</h4>", 
                unsafe_allow_html=True)
    
    def make_line():
        """ Line divider between images. """
            
        line = st.markdown('<hr style="border:1px solid gray"> </hr>',
                unsafe_allow_html=True)

        return line

    make_line()

    st.info("""
            There are two main algorithms: \n
            - Time Comparison
            - Feature Score
            - Owners Prediction \n
            $←$ To start playing with the app, select an option on the 
            left sidebar.
            """)



    # Images and brief explanations.

    make_line()

    
    st.markdown("<h2 style='text-align: center;'> Time Comparison </h2>", 
                unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: left;'> Developed by Joseph </h4>", 
                unsafe_allow_html=True)
    st.info("""
                This algorithm comparese the average number of players (per day) of the chosen game
                (in the first 12 months) with all other games in the database. Based on this comparison, the algorithm
                makes a prediction on the next few months of the chosen game.
                Moreover, it underlines the three closest games, from which a developer can take inspiration from.
            """)
    
    make_line()

    st.markdown("<h2 style='text-align: center;'> Feature Score </h2>", 
                unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: left;'> Developed by Rohit </h4>", 
                unsafe_allow_html=True)
    st.info("""
                This algorithm allows you to compare the relevance of a set of features in a chosen popularity class. \n
                The popularity class of a game is:
                - 1: _if the average number of players per day is less than 10_
                - 2: _if the average number of players per day is between 10 and 100_
                - 3: _if the average number of players per day is between 100 and 1000_
                - 4: _if the average number of players per day is between 1000 and 10000_
                - 5: _if the average number of players per day is more than 10000_ \n
                The relevance of a feature F in a given class C is determined by its:
                #### - Importance Score:
                _This is the number of games in class C with feature F, over the total number of games in class C_.
                #### - Relative Importance Score:
                _This is the importance score of feature F in class C, divided by the sum over all classes of all importance scores of feature F in each class._
                #### - Benefit Score:
                _This is the number of games in class C with feature F, over the total number of games with feature F._
                #### - Relative Benefit and Importance Score:
                _This is the importance score of feature F in class C, multiplied by the benefit score of feature F in class C._
                """)
    
    make_line()
    
    st.markdown("<h2 style='text-align: center;'> Owners Prediction </h2>", 
                unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: left;'> Developed by Kanishk </h4>", 
                unsafe_allow_html=True)
    st.info("""
                This algorithm allows you to predict the number of owners of a game having the following features in its store page:
                - PackageCount: _the number of package deals the game is part of_
                - MovieCount: _the number of videos about the game_
                - ScreenshoCount: _the number of screenshots of the game_
                - AchievementCount: _the number of achievements available for the players_
                - PriceMean: _the average between the inital and final price_
                The output is a monthly sale prediction of the game.
                """)
    
    make_line()
    
    return
