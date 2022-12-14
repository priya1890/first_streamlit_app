
import streamlit
streamlit.title("My Healthy Diner")
streamlit.header("Breakfast Menu")
streamlit.text("Coffee")
streamlit.text("๐ฅ๐Sandwich")
streamlit.text("Idli")
streamlit.header('๐๐ฅญ Build Your Own Fruit Smoothie ๐ฅ๐')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits: ",my_fruit_list.index)
streamlit.dataframe(my_fruit_list)

#Adding pick list
fruits_selected = streamlit.multiselect("Pick some fruits: ",my_fruit_list.index,['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
