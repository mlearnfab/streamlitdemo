
# import libraries
import streamlit as st
import pandas as pd

# create title for web page
st.title(" \U0001F37D Lunch Order App ")

st.divider()

# create form

with st.form(key='my_form'):
    name = st.text_input(label='Enter your name')          #input name

    st.divider()


    col1, col2 = st.columns(2)

    with col1:
        appetizer = st.selectbox('Appetizers', ['Salad', 'Wings', 'Fries'])     # input appetizer
        main_course = st.selectbox('Main Course', ['Steak', 'Salmon', 'Tofu'])  # input main course

    with col2:
        dessert = st.selectbox('Dessert', ['Ice Cream', 'Cake', 'Pie'])         # input dessert
        drink = st.selectbox('Drinks', ['Soda', 'Tea', 'Water'])                # input drink

    submit_button = st.form_submit_button(label='Submit')


# store order in a dictionary
order = {'Name': name, 'Appetizer': appetizer, 'Main Course': main_course, 'Dessert': dessert, 'Drink': drink}

# create a dictionary of prices
prices = {'Salad': 5.50, 'Wings': 7.50, 'Fries': 6.50, 'Steak': 25, 'Salmon': 15, 
          'Tofu': 10, 'Ice Cream': 5, 'Cake': 6, 'Pie': 7, 'Soda': 2, 'Tea': 1.50, 'Water': 1}

# calculate the total price
total = 0
for item in order:
    if order[item] in prices:
        total += prices[order[item]]    

# create a Pandas DataFrame from the order dictionary
        
order = pd.DataFrame.from_dict(order, orient='index', columns=['Order'])

# display the order summary

st.subheader("Your Order Summary")  
st.table(order)

# display the total

st.markdown(f"#### Order Total: ${total} ####")

st.write("Would you like to leave a tip?")

with st.form(key='tip_form'):
    tip_pctg = st.selectbox('Tip Percentage', ['0%', '10%', '15%','20%'])
    submit_button = st.form_submit_button(label='Submit')

    if tip_pctg =='10%':
        total = total + total*.1
    elif tip_pctg =='20%':
        total = total + total*.2
    elif tip_pctg =='15%':
        total = total + total*.15


st.markdown(f"#### Total = ${total} ####")


st.write("Thank you for your order! Please come again!")   # display a thank you message