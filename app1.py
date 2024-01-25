import streamlit as st

st.title('Lunch Order App')

with st.form(key='my_form'):
    name = st.text_input(label='Enter your name')

    appetizer = st.selectbox('Select Appetizer', ['Salad', 'Fries', 'Wings'])
    main_course = st.selectbox('Select Main Course', ['Steak', 'Salmon', 'Tofu'])
    dessert = st.selectbox('Select Dessert', ['Ice Cream', 'Cake', 'Pie'])
    drinks = st.selectbox('Select Drink', ['Soda', 'Coffee', 'Tea'])


    submit_button = st.form_submit_button(label='Submit')



order = {'Name': name, 'Appetizer': appetizer, 'Main Course': main_course, 
             'Dessert': dessert, 'Drink': drinks}

st.write('Your order is:', order)

prices = {'Salad': 5, 'Fries': 3, 'Wings': 7, 'Steak': 15, 'Salmon': 12, 'Tofu': 10,
              'Ice Cream': 4, 'Cake': 5, 'Pie': 5, 'Soda': 2, 'Coffee': 3, 'Tea': 2}

total = 0
for item in order:
    if order[item] in prices:
        total += prices[order[item]]
st.write('Your total is: $', total)