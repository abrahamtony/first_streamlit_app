import streamlit
import pandas
streamlit.title('My parents healthy diner \U0001F601')
streamlit.header('Breafast Menu')
streamlit.text('Omega 3 & Blueberry Oat meal ')
streamlit.text('Kale, Spinach & Rocket Smothie')
streamlit.text('\N{chicken}Hard-boiled  Free-Range Egg')
my_fruits_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect("Pick some fruits", streamlit.list(my_fruits_list.index)
streamlit.dataframe(my_fruits_list)
