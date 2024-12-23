# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(":cup_with_straw: Customize Your Smoothie! :cup_with_straw:")
st.write(
    """Choose the fruits you want in your custom smoothie!
    """)
#option=st.selectbox('what is you favourite fruit?'
#('banana','strawberries','peaches')
#)
#st.write('your favourite fruit is :', option )
session=get_active_session()

#adding atext input box
name_on_order = st.text_input('Name on smoothie')
st.write("The name on your smoothie will be : ", name_on_order)


my_dataframe=session.table('smoothies.public.fruit_options').select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe,use_container_width=True)

#MULTISELECT 
ingredient_list=st.multiselect('choose upto 5 ingredients:', my_dataframe,max_selections=5)
if ingredient_list:
    #st.write(ingredient_list)
    #st.text(ingredient_list) #gives text written
    ingredients_string=''
    for fruit in ingredient_list:
        ingredients_string=ingredients_string+fruit+' '
    st.write(ingredients_string)
    
my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingredients_string + """','""" + name_on_order + """')"""


#if ingredients_string:
 #   session.sql(my_insert_stmt).collect()
  #  st.success('Your Smoothie is ordered!', icon="✅") this code gives values in different lines

time_to_insert=st.button('Submit Order')
if time_to_insert:
    session.sql(my_insert_stmt).collect()
    st.success('Your Smoothie is ordered!', icon="✅")
st.write(my_insert_stmt)
st.stop()


